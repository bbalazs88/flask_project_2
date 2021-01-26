import pandas as pd
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logics

x, y, z = logics.logic_a(2, 2, 2)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Calcs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_x = db.Column(db.String(30), nullable=False, default='0')
    content_y = db.Column(db.String(30), nullable=False, default='0')
    content_z = db.Column(db.String(30), nullable=False, default='0')
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content_x_in = request.form['content1']
        content_y_in = request.form['content2']
        content_z_in = request.form['content3']

        new_task = Calcs(content_x=content_x_in, content_y=content_y_in, content_z=content_z_in)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding the task.'
    else:
        tasks = Calcs.query.order_by(Calcs.date_created).all()  # tasks holds all the records
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Calcs.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a deleting problem.'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Calcs.query.get_or_404(id)

    if request.method == 'POST':
        task.content_x = request.form['content1']
        task.content_y = request.form['content2']
        task.content_z = request.form['content3']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the task.'
    else:
        return render_template('update.html', task=task)

# Ctrl + Shift + R - css modifications will reload (cache cleared reload)
if __name__ == "__main__":
    app.run(debug=True)