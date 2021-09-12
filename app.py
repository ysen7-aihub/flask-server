from flask import Flask
from flask_cors import CORS
from flask_restx import Api
import os

app = Flask(__name__, static_folder='./frontend/moodmaker/build', static_url_path='/')
# CORS(app)

api = Api(
    app,
    version='0.1',
    title="Moodmaker's API Server",
    description="Moodmaker's API Server",
    terms_url="/",
    contact="cdnnnl@ewhain.net",
    license="MIT"
)

from route.diary import Diary
from route.music import Music
from route.predict import Predict

@app.route('/')
def index():
    return app.send_static_file('index.html')


api.add_namespace(Music, '/music')

api.add_namespace(Diary, '/diary')

api.add_namespace(Predict, '/predict')

def main():

    UPLOAD_FOLDER = "./uploaded_img"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.environ["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    return app

if __name__ == "__main__":
    main()
    app.run(debug=False, host='0.0.0.0')
