from flask import Blueprint, jsonify


api = Blueprint('api', __name__, url_prefix='/api/v1')

# original text
# @api.route('/health')
# def health():
#     return "ok"

@api.route('/health')
def health():
    return jsonify({'status': 'ok'})

# @api.route('/todos',methods=['GET'])
# def get_todos():
#     return jsonify([])

@api.route('/todos',methods=['GET'])
def get_todos():
    return jsonify([{
        "id":1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"   
        }])

@api.route('/todos/<int:id>',methods=['GET'])
def get_todos(id):
    return jsonify([{
        "id":1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"   
        }])

# create (POST)
@api.route('/todos',methods=['POST'])
def create_todo():
    return jsonify({
        "id":1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,

        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }), 201

# update    (PUT)
@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        })

# delete
@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
    "id": id,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2023-02-27T00:00:00",
    "created_at": "2023-02-20T00:00:00",
    "updated_at": "2023-02-20T00:00:00"
})
