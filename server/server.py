from flask import Flask
from flask_restful import Api, Resource
from newsScraper import initNews
import time

app = Flask(__name__)
api = Api(app)

names = {
            'Khadar': {
                'city': 'Tuskegee', 
                'state': 'Alabama',
                'id': '0'
            },
            'Philip': {
                'city': 'Anaheim', 
                'state': 'California',
                'id': '1'
            },
            'Skem': { 
                'city': '',
                'state': 'Romania',
                'id': '2'
            },
            'Fredrick': { 
                'city': 'Charlottesville',
                'state': 'Virginia',
                'id': '3'
            },
            'Hamel': { 
                'city': 'Bucharest',
                'state': 'Romania',
                'id': '4'
            }
        }

# Profile RESTful API Route
class Profile(Resource):
    def get(self, name):
        profile = names[name]

class Profiles(Resource):
    def get(self):
        listOfNames = [names]
        return listOfNames


# News RESTful API Route
class News(Resource):
    def get(self, name):
        news = initNews(names[name]['city'], names[name]['state'], time, name)
        if news is not None:
            return {'news': news}
    def post(self, name):
        return {'newNews': ['Posted']}


api.add_resource(Profiles, '/profiles')
api.add_resource(Profile, '/profile/<string:name>')
api.add_resource(News, '/news/<string:name>')

api.init_app(app)

# Dev Run Setting
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)