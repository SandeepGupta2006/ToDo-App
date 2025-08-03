from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("db_uri")
app.config['SESSION_PERMANENT'] = True
db = SQLAlchemy(app)


@app.before_request
def set_user_id():
    session.permanent = True
    if "user_id" not in session:
        session["user_id"] = uuid4().hex


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False)
    task = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Integer, default=0)


@app.route('/', methods=['GET', 'POST'])
def todo_list():
    user_id = session["user_id"]
    data = Todo.query.filter_by(user_id=user_id).order_by(Todo.id.desc()).all()

    if request.method == 'POST':

        if request.form['act'] == 'create':
            new_task = request.form['new_task']
            if new_task:
                new_data = Todo(task=new_task, user_id=user_id)
                db.session.add(new_data)
                db.session.commit()
                return redirect("/")

        else:
            id = request.form['id']
            tr = Todo.query.get(id)

            if request.form['act'] == 'update':
                return render_template("index.html", data=data, to_update_id=id)

            elif request.form['act'] == 'save_update_task':
                updated_task = request.form['updated_task']
                if updated_task:
                    tr.task = updated_task
                    db.session.commit()
                    return redirect("/")

            elif request.form['act'] == "click_complete":
                tr.completed = 1 if 'complete' in request.form else 0

                db.session.commit()
                return redirect("/")

            elif request.form['act'] == 'delete':
                db.session.delete(tr)
                db.session.commit()
                return redirect("/")

    return render_template("index.html", data=data, to_update_id=None)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()
