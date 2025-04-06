from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [episode.to_dict() for episode in episodes], 200


class EpisodeById(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200



class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200


class AppearancePost(Resource):
    def post(self):
        data = request.get_json()
        
        if "rating" not in data or not (1 <= data["rating"] <= 5):
            return {"errors": ["Rating must be between 1 and 5"]}, 400
        
        episode = Episode.query.get(data["episode_id"])
        guest = Guest.query.get(data["guest_id"])
        
        if not episode or not guest:
            return {"errors": ["Invalid episode_id or guest_id"]}, 400
        
        new_appearance = Appearance(
            rating=data["rating"],
            episode_id=data["episode_id"],
            guest_id=data["guest_id"]
        )
        db.session.add(new_appearance)
        db.session.commit()

        return new_appearance.to_dict(), 201

# Register API Resources
api.add_resource(EpisodeList, "/episodes")
api.add_resource(EpisodeById, "/episodes/<int:id>")
api.add_resource(GuestList, "/guests")
api.add_resource(AppearancePost, "/appearances")

if __name__ == "__main__":
    app.run(debug=True)
