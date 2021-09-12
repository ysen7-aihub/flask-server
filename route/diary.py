from flask_restx import Resource, Api, Namespace, fields
from flask import Blueprint, request, jsonify, flash, Flask, redirect, url_for
from werkzeug.utils import secure_filename
from annoyUses import SpotifyRecommend
from connect_RDS import get_secret
import os
import requests
import time

conn, cursor = get_secret()
img = {}
txt = {}
count = 1

UPLOAD_FOLDER = "./uploaded_img"

Diary = Namespace(name='Diary',
                  description="Diary의 이미지와 텍스트 리스트를 작성하기 위해 사용하는 API")

diary_txt = Diary.model('Diary', {
    'txt': fields.String(description='txt', required=True, example="수요일은 특식 데이이다. 학교 급식에서 잔반 없는 날...")
})

diary_img = Diary.model('Diary', {
    'img': fields.String(description='img', required=True,
                         example="https://image.rocketpunch.com/company/5466/naver_logo.png?s=400x400&t=inside"),

})

diary_txt_with_id = Diary.inherit('Diary With ID', diary_txt, {
    'diary_id': fields.Integer(description='a unique diary ID')
})

diary_img_with_id = Diary.inherit('Diary With ID', diary_img, {
    'diary_id': fields.Integer(description='a unique diary ID')  #
})


@Diary.route('/txt')
class DiaryPost(Resource):
    @Diary.expect(diary_txt)
    @Diary.response(201, 'Success', diary_txt_with_id)
    @Diary.response(400, 'Fail')
    def post(self):
        """서버에 Diary 텍스트 등록"""
        global txt

        txt = request.json.get('txt');
        print(txt)
        return 202

@Diary.route('/img')
class DiaryPost(Resource):
    @Diary.expect(diary_img)
    @Diary.response(201, 'Success', diary_img_with_id)
    @Diary.response(400, 'Fail')
    def post(self):
        """서버에 Diary 이미지 등록"""
        global count
        global img
        global txt
        count += 1

        img = request.files['img']
        print(img.filename)

        if img.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(img.filename)
        img.save(os.path.join(UPLOAD_FOLDER, filename))

        query = """
                INSERT INTO moodmaker.diary (txt, img)
                VALUES ('{0}','{1}');""".format(txt, UPLOAD_FOLDER + '/' + filename)
        cursor.execute(query)
        conn.commit()


        try:
            cnn = requests.post('http://13.125.225.154/predict/img', files=img)

            nlp = requests.post('http://3.34.91.153/predict/txt', txt=txt).json()

            query = """
                    INSERT INTO moodmaker.predict (sen_1, sen_2, sen_3, score_1, score_2, score_3, cnn_score)
                    VALUES ('{0}','{1}','{2}','{3}','{4}','{5}');""".format(nlp.sen_1,
                                                                            nlp.sen_2, nlp.sen_3, nlp.score_1,
                                                                            nlp.score_2, nlp.score_3, cnn.score2)
            cursor.execute(query)

            conn.commit()

            return 202
        except Exception as e:
            return "fail!"


"""
@Diary.route('/<int:diary_id>')
@Diary.doc(params={'diary_id': 'A Unique ID'}) # 설명 추가
class DiarySimple(Resource): # 이름 수정
    @Diary.response(201, 'Success', diary_fields_with_id) # 특정 스키마가 반환된다.
    def get(self, diary_id):
        Diary 리스트에 id와 일치하는 ID를 가진 값을 반환
        return {
            'diary_id': diary_id,
            'img': img[diary_id],
            'txt': txt[diary_id]
        }
    @Diary.doc(response={202:'Success'})
    @Diary.doc(response={500:'Failed'})
    def put(self, diary_id):
        Diary 리스트에 id와 일치하는 ID를 찾아 내용을 수정
        img[diary_id] = request.json.get('img')
        txt[diary_id] = request.json.get('txt')
        return {
            'diary_id': diary_id,
            'img': img[diary_id],
            'txt': txt[diary_id]
        }, 202

    def delete(self, diary_id):
        Diary 리스트에 id와 일치하는 ID를 가진 내용을 삭제
        del txt[diary_id]
        del img[diary_id]
        return {
            "delete": "success"
        }, 202

"""
