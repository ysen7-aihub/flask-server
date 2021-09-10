from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class Diary(db.Model):
    __table_name__ = 'diary'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    txt = db.Column(db.String(1000), nullable=False) 
    img = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"<Diary('{self.id}', '{self.txt}', '{self.img}')>"

class Music(db.Model):
    __table_name__ = 'Music'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True) 
    name = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False) 
    spotify_id = db.Column(db.Integer, nullable=False) 

    def __repr__(self):
        return f"<Diary('{self.id}', '{self.txt}', '{self.img}')>"

class Predict(db.Model):
    __table_name__ = 'predict'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    score1 = db.Column(db.Float(30), nullable=False)
    score2 = db.Column(db.String(30), nullable=False) 
    label = db.Column(db.String, nullable=True)


    def __repr__(self):
        return f"<Predict('{self.id}', '{self.score1}', '{self.score2}',  '{self.label}')>"
