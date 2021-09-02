import datetime
from pytz import timezone
from flask import request
from flask_restx import Resource, Api, Namespace, fields
from flask import Blueprint, request,jsonify
from models import db

from models import Diary, Music

img = {}
txt = {}
count = 1

Diary = Namespace(name='Diary',
                 description="Diary의 이미지와 텍스트 리스트를 작성하기 위해 사용하는 API")

diary_fields = Diary.model('Diary', {
    # diary list Model 객체 생성
    'img': fields.String(description='img', required=True, example="https://image.rocketpunch.com/company/5466/naver_logo.png?s=400x400&t=inside"),# TODO: 이미지 예시 넣기
    'txt': fields.String(description='txt', required=True, example="수요일은 특식 데이이다. 학교 급식에서 잔반 없는 날...")
})

diary_fields_with_id = Diary.inherit('Diary With ID', diary_fields, {  # diary_fields 상속 받음
    'diary_id': fields.Integer(description='a unique diary ID') # 고유값
})

@Diary.route('/')
class DiaryPost(Resource):
    @Diary.expect(diary_fields) # diary_fields 스키마가 들어올거라고 예상한다. 모델 등록
    @Diary.response(201, 'Success', diary_fields_with_id) # 특정 스키마가 반환된다.
    @Diary.response(400, 'Fail')
    def post(self):
        """서버에 Diary 리스트를 등록"""
        global count
        global diary

        idx = count
        count += 1
        img = request.json.get('img')
        txt = request.json.get('txt')
        print(img, txt)

        # DB에 저장
        try:
            data = Diary(
                id =5,
                img = img,
                txt = txt,
                # created_at=datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None),
                # updated_at=datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None)
            )
            Diary.db.session.add(data)
            Diary.db.session.commit()
            Diary.db.session.remove()
            return "success!"
        except Exception as e:
            return "fail!"


@Diary.route('/<int:diary_id>')
@Diary.doc(params={'diary_id': 'A Unique ID'}) # 설명 추가
class DiarySimple(Resource): # 이름 수정
    @Diary.response(201, 'Success', diary_fields_with_id) # 특정 스키마가 반환된다.
    def get(self, diary_id):
        """Diary 리스트에 id와 일치하는 ID를 가진 값을 반환"""
        return {
            'diary_id': diary_id,
            'img': img[diary_id],
            'txt': txt[diary_id]
        }
    @Diary.doc(response={202:'Success'})
    @Diary.doc(response={500:'Failed'})
    def put(self, diary_id):
        """Diary 리스트에 id와 일치하는 ID를 찾아 내용을 수정"""
        img[diary_id] = request.json.get('img')
        txt[diary_id] = request.json.get('txt')
        return {
            'diary_id': diary_id,
            'img': img[diary_id],
            'txt': txt[diary_id]
        }, 202

    def delete(self, diary_id):
        """Diary 리스트에 id와 일치하는 ID를 가진 내용을 삭제"""
        del txt[diary_id]
        del img[diary_id]
        return {
            "delete": "success"
        }, 202

