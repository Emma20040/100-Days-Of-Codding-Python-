from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

POST = {
    'post1': {'topic': 'Google is rolling out Gemini 2.5(exp) to free users'},
    'post2': {'topic': 'what is the "specail" needed to unlock AGI within current models? '},
    'post3': {'topic': 'How to write blog post that developers read'},
    'post4': {'topic': 'A web framework for building product with Python'},
    'post5': {'topic': 'Self-contained Python Scripts with uv'},

}


def abort_if_post_doesnt_exist(post_id):
    if post_id not in POST:
        abort(404, message="Post {} doesn't exist".format(post_id))

parser = reqparse.RequestParser()
parser.add_argument('topic')


# Todo
# shows a single todo item and lets you delete a todo item
class POSTS(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        return POST[post_id]

    def delete(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        del POST[post_id]
        return '', 204

    def put(self, post_id):
        args = parser.parse_args()
        topic = {'topic': args['topic']}
        POST[post_id] = topic
        return topic, 201
    
# POSTSList
# shows a list of all POST, and lets you POST to add new topics
class POSTSList(Resource):
    def get(self):
        return POST

    def post(self):
        args = parser.parse_args()
        post_id = int(max(POST.keys()).lstrip('post')) + 1
        post_id = 'post%i' % post_id
        POST[post_id] = {'topic': args['topic']}
        return POST[post_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(POSTSList, '/blogs')
api.add_resource(POSTS, '/blog/<post_id>')