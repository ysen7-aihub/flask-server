from flask import request
from flask_restx import Resource, Namespace, fields
from annoyUses import SpotifyRecommend
import json
from connect_RDS import get_secret

conn, cursor = get_secret()

Predict = Namespace(name='Predict',
                 description="예측 결과를 반환하는 API")

predict_fields = Predict.model('Predict', {
    'name1': fields.String(description='감정1', required=True, example="행복"),
    'name2': fields.String(description='감정2', required=True, example="공포"),
    'name3': fields.String(description='감정3', required=True, example="분노"),
})

predict_fields_with_id = Predict.inherit('Predict With ID', predict_fields, {
    'predict_id': fields.Integer(description='a unique predict ID')
})

@Predict.route('/')
class PredictSimple(Resource):
    @Predict.response(201, 'Success')
    @Predict.response(400, 'Fail')
    def get(self):
        """음악 추천 결과 3개 반환"""

        result = SpotifyRecommend()

        query = "SELECT name, artist FROM music WHERE id = {0} OR id = {1} OR id = {2}".format(result[0], result[1], result[2])
        cursor.execute(query)
        result = cursor.fetchall()

        query = "SELECT sen_1, score_1, sen_2, score_2, sen_3, score_3, cnn_score " \
                "FROM predict WHERE id IN (SELECT MAX(id) FROM predict);"
        cursor.execute(query)
        sen = cursor.fetchall()

        data = [
            {"name": result[0][0], "artist": result[0][1]},
            {"name": result[1][0], "artist": result[1][1]},
            {"name": result[2][0], "artist": result[2][1]},
            {
                "sentiment": sen[0][0],
                "일기": sen[0][1],
                "이미지": 0
            },
            {
                "sentiment": sen[0][2],
                "일기":sen[0][3],
                "이미지": 0
            },
            {
                "sentiment": sen[0][4],
                "일기": sen[0][5],
                "이미지": 0
            },
            {
                "sentiment": "긍정지수",
                "일기": 0,
                "이미지": sen[0][6]
            }
        ]

        return data, 202



@Predict.route('/label')
class PredictSimple(Resource):
    @Predict.response(201, 'Success')
    @Predict.response(400, 'Fail')
    def post(self):
        """사용자가 입력한 정답(7개 감정 중 하나) db에 등록"""

        label = request.json.get('label');
        query = """
            update predict set label='{0}' order by id desc limit 1;
                """.format(label)

        cursor.execute(query)
        conn.commit()

        return 202
