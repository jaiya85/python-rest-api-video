from flask import *
from flask_restful import *
from flask_sqlalchemy import *
from dataclasses import dataclass


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vd.db'
db = SQLAlchemy(app)



@dataclass()
class VideoModel(db.Model):
    id: int
    name: str
    views: int
    likes: int

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"


#db.create_all()


class Video(Resource):

    @app.route('/video/<int:v_id>', methods=['GET'])
    def get(v_id):
        result = VideoModel.query.filter_by(id=v_id).first()
        if not result:
            abort(404, "not found")
        return jsonify(result)


    @app.route('/video/<int:video_id>', methods=['PUT'])
    def put(video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, "found")
            #abort(409, message="Video id taken...")
        v = VideoModel(id=video_id, name=request.form["name"], views=request.form["views"], likes=request.form["likes"])
        db.session.add(v)
        db.session.commit()
        return jsonify({"added": "success"})

    @app.route('/video/del/<int:v_id>', methods=['DELETE'])
    def delete(v_id):
        result = VideoModel.query.filter_by(id=v_id).first()
        if result is None:
            abort(404, "video id not found")
        db.session.delete(result)
        db.session.commit()
        return jsonify({"deleted": "success"})

    @app.route('/video/patch/<int:v_id>', methods=['PATCH'])
    def patch(v_id):
        result = VideoModel.query.filter_by(id=v_id).first()
        if result is None:
            abort(404, "video id not found")
        if request.form.get("name"):
            result.name = request.form["name"]
        if request.form.get("views"):
            result.views = request.form["views"]
        if request.form.get("likes"):
            result.likes = request.form["likes"]
        db.session.commit()
        return jsonify({"updated": "success"})



if __name__ == '__main__':
    app.run(debug=True)
