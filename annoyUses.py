from annoy import AnnoyIndex
from connect_RDS import get_secret

conn, cursor = get_secret()

def make_input(score1, score2, score3, sen_1, sen_2, sen_3, score):

    labels = {'혐오': 0, '분노': 1, '공포': 2, '슬픔': 3, '놀람': 4, '중립': 5, '행복': 6}
    weights = {'혐오': 1, '분노': 1, '공포': 3, '슬픔': 4, '놀람': 5, '중립': 7, '행복': 10}
    x = labels[sen_1]

    tmp = score1 * weights[sen_1] + score2 * weights[sen_2] + score3 * weights[sen_3]
    y = 0.1 * tmp
    z = score

    return [x, y, z]

def SpotifyRecommend():
    query = """
            SELECT score_1, score_2, score_3, sen_1,
            sen_2, sen_3, cnn_score
            FROM predict
            WHERE id IN (
                SELECT MAX(id) FROM predict
            );
            """
    cursor.execute(query)
    result= cursor.fetchone()

    length_of_vector = 3
    new_annoy_index = AnnoyIndex(length_of_vector, 'dot')
    new_annoy_index.load('musics.annoy')

    n = 3 # 3개의 노래
    input = make_input(result[0], result[1],result[2],result[3],result[4],result[5],result[6])

    print(new_annoy_index.get_nns_by_vector(input, n))

    # 음악 인덱스 세개 뱉어냄
    return (new_annoy_index.get_nns_by_vector(input, n))


