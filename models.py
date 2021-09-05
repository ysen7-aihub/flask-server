from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # app.py에서 연결된 db 객체가 아닐 듯

class Diary(db.Model):
    __table_name__ = 'diary'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True) # diary 테이블의 pk
    txt = db.Column(db.String(1000), nullable=False) # 일기 내용 저장 1000자, VARCHAR
    img = db.Column(db.String(1000), nullable=False) # db에 직접 저장하는게 아니라 파일 시스템에 저장한 다음, 파일 이름만 저장할 예정

    # 사용자가 이해하는 객체의 모습을 표현한다. 출력 표현 리턴
    def __repr__(self):
        return f"<Diary('{self.id}', '{self.txt}', '{self.img}')>"

class Music(db.Model):
    __table_name__ = 'Music'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True) # music 테이블의 pk
    name = db.Column(db.String(30), nullable=False) # 곡명
    artist = db.Column(db.String(30), nullable=False) # 가수명
    spotify_id = db.Column(db.Integer, nullable=False) # spotify 고유 아이디

    # 사용자가 이해하는 객체의 모습을 표현, 출력 표현 리턴
    def __repr__(self):
        return f"<Diary('{self.id}', '{self.txt}', '{self.img}')>"

# TODO: 예측 결과 테이블 만들기
class Predict(db.Model):
    __table_name__ = 'predict'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    score1 = db.Column(db.Float(30), nullable=False) # nlp 결과
    score2 = db.Column(db.String(30), nullable=False) # cnn 결과
    # 사용자로부터 받은 label, 음악추천 모델 재학습 용도, 우선 nlp 감정 6개? 중 하나로 받을 생각이기 때문에 string으로 해놨음
    label = db.Column(db.String, nullable=True)

    # 사용자가 이해하는 객체의 모습을 표현, 출력 표현 리턴
    def __repr__(self):
        return f"<Predict('{self.id}', '{self.score1}', '{self.score2}',  '{self.label}')>"
