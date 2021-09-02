from flask import Flask
from flask_restx import Api
from route.todo import Todo
from route.auth import Auth
from route.diary import Diary
from route.music import Music
import os
from models import db
# import pymysql

# ---- sqlite 용
# 현재있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app = Flask(__name__)

# SQLAlchemy 설정
app.config['SECRET_KEY'] = 'this is secret'

# MySQL dB 연결
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:111111@localhost:3306/moodmaker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

# Api 객체의 생성자 파라미터 수정
api = Api(
    app,
    version='0.1',
    title="Moodmaker's API Server",
    description="Moodmaker's API Server",
    terms_url="/",
    contact="cdnnnl@ewhain.net",
    license="MIT"
)


api.add_namespace(Todo, '/todos')

api.add_namespace(Auth, '/auth')

api.add_namespace(Music, '/music')

api.add_namespace(Diary, '/diary')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)