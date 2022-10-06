from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("Read(All).html", users = users)

@app.route("/user/new")
def new_user_form():
    return render_template("Create.html")

@app.route("/user/create", methods = ["POST"])
def create_user():
    User.create_user(request.form)
    return redirect("/")

@app.route("/user/<int:id>/show")
def get_one(id):
    data = { 'id' : id }
    user = User.get_one(data)
    return render_template("Read(One).html", user = user)

@app.route("/user/<int:id>/edit")
def edit_user(id):
    data = { 'id' : id }
    user = User.get_one(data)
    return render_template("Users(Edit).html", user = user)

@app.route("/user/<int:id>/update", methods = ['POST'])
def update_user(id):
    data = { 'id' : id, 'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'email' : request.form['email'] }
    User.edit_user(data)
    return redirect("/")

@app.route("/user/<int:id>/delete")
def delete_user(id):
    data = { 'id' : id }
    User.delete_user(data)
    return redirect("/")