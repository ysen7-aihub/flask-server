from annoy import AnnoyIndex

length_of_vector = 3
new_annoy_index = AnnoyIndex(length_of_vector, 'dot')
new_annoy_index.load('musics.annoy')

n = 3 #3개의 노래
# TODO: nlp 결과, cnn 결과 여기에 넣기
input = [0,0.1,0.2]

# 음악 인덱스 세개 뱉어냄
print(new_annoy_index.get_nns_by_vector(input, n))

