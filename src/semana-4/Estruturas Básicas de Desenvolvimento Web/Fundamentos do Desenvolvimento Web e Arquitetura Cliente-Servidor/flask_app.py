from flask import Flask, Response, request, jsonify
from uuid import uuid4

app = Flask(__name__)


users = []

class User:
    def __init__(self, name, age):
        self.id = uuid4()
        self.name = name
        self.age = age

@app.post("/users")
def create_user():
    user = User(
        name=request.json["name"],
        age=request.json["age"]
    )
    users.append(user)
    return Response("Created", status=201)

@app.put("/users/<user_id>")
def update_user(user_id):
    for user in users:
        if str(user.id) == user_id:
            user.name = request.json["name"]
            user.age = request.json["age"]
            return Response("Updated", status=200)
    return Response("Not exist", status=400)

@app.patch("/users/<user_id>")
def update_user_with_patch(user_id):
    for user in users:
        if str(user.id) == user_id:
            if "name" in request.json:
                user.name = request.json["name"]
            if "age" in request.json:
                user.age = request.json["age"]
            return Response("Updated", status=200)
    return Response("Not exist", status=400)

@app.get("/users/<user_id>")
def get_user(user_id):
    for user in users:
        if str(user.id) == user_id:
            return jsonify({"id": user.id, "name": user.name, "age": user.age})
    return Response("User not exist", status=400)

@app.get("/users")
def get_users():
    return jsonify(list(map(lambda user: {
        "id": user.id,
        "name": user.name,
        "age": user.age
    }, users)))
    
@app.delete("/users/<user_id>")
def remove_users(user_id):
    for user in users:
        if str(user.id) == user_id:
            users.remove(user)
            return Response("No Content", status=204)
    return Response("User not exist", status=400)

if __name__ == '__main__':
  app.run()