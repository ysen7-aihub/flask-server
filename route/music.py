from flask import request
from flask_restx import Resource, Api, Namespace, fields
import json

from models import Diary, Music

result = [{
    'name': "라일락",
    'artist': "IU",
    'positivity': 0.6
},
{
    'name': "Dynamite",
    'artist': "BTS",
    'positivity': 0.3
},
{
    'name': "next level",
    'artist': "asepa",
    'positivity': 0.9
}]

Music = Namespace(name='Music',
                 description="음악 추천 결과를 반환하는 API")

music_fields = Music.model('Music', {
    # Music list Model 객체 생성
    'name': fields.String(description='name', required=True, example="라일락"),
    'artist': fields.String(description='artist', required=True, example="IU"),
    # 'positivity': fields.String(description='positivity', required=True, example="0.6") # 결과 : 일단 긍정지수
})

music_fields_with_id = Music.inherit('Music With ID', music_fields, {  # music_fields 상속 받음
    'music_id': fields.Integer(description='a unique music ID') # music_id 고유값
})

@Music.route('/')
class MusicGet(Resource):
    @Music.response(201, 'Success', music_fields) # 특정 스키마가 반환된다.
    @Music.response(400, 'Fail')
    def get(self, music_id):
        """음악 결과 3개 배열로 반환"""
        # TODO: 배열로 바꾸기
        return {
        'name': "라일락",
        'artist': "IU"
        }
