import pandas as pd
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Calcs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_x = db.Column(db.String(30), nullable=False, default='0')
    content_y = db.Column(db.String(30), nullable=False, default='0')
    content_z = db.Column(db.String(30), nullable=False, default='0')
    logic_number = db.Column(db.String(30), nullable=False, default='1')
    content_x_out = db.Column(db.String(30), nullable=False, default='0')
    content_y_out = db.Column(db.String(30), nullable=False, default='0')
    content_z_out = db.Column(db.String(30), nullable=False, default='0')
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content_x_in = request.form['content1']
        content_y_in = request.form['content2']
        content_z_in = request.form['content3']
        logic = request.form['content4']

        logic_num = logics.logic_selector(int(logic))
        print(logic_num)

        # TODO: float mezőknél a vesszőt is fogadja el!

        deltax_in, deltay_in, deltaz_in, pitch_in, roll_in, yaw_in, resize_x_in, resize_y_in, resize_z_in = \
            logics.logic_selector(int(logic))
        # print(pitch_in, roll_in)

        x, y, z = logics.logic_calc(float(content_x_in), float(content_y_in), float(content_z_in),
                                    deltax_in, deltay_in, deltaz_in, pitch_in, roll_in, yaw_in,
                                    resize_x_in, resize_y_in, resize_z_in, int(logic))
        print(x, y, z, logic)

        new_task = Calcs(content_x=content_x_in,
                         content_y=content_y_in,
                         content_z=content_z_in,
                         logic_number=logic,
                         content_x_out=x,
                         content_y_out=y,
                         content_z_out=z)

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

        if request.form['content4'] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            task.logic_number = request.form['content4']
        else:
            return '<h2> bazzz </h2>'

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