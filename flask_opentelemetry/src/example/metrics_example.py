from flask import Flask, request, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from opentelemetry import trace
from opentelemetry import metrics
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

tracer = trace.get_tracer("task.tracer")
meter = metrics.get_meter("task.meter")

request_counter = meter.create_counter(
    "flask_app_requests_total",
    description="Total number of requests",
)

task_counter = meter.create_counter(
    "flask_app_tasks_total",
    description="Total number of tasks created",
)

class Task(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    description: Mapped[str] = mapped_column(db.String(256), nullable=False)

# Initialize SQLAlchemy with the configured Flask application
db.init_app(app)

with app.app_context():
    db.create_all()

# HTML template with inline CSS
HOME_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>To-Do List</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 40px auto;
      padding: 20px;
      max-width: 600px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
    }
    form {
      margin-bottom: 20px;
    }
    input[type="text"] {
      padding: 10px;
      width: calc(100% - 22px); /* Full-width minus padding and border */
      margin-bottom: 10px;
    }
    input[type="submit"] {
      background-color: #5cb85c;
      border: none;
      color: white;
      padding: 10px 20px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      cursor: pointer;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      position: relative;
      padding: 8px;
      background-color: #fff;
      border-bottom: 1px solid #ddd;
    }
    .delete-button {
      position: absolute;
      right: 10px;
      top: 10px;
      background-color: #ff6347;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>To-Do List</h1>
  <form action="/add" method="post">
    <input type="text" name="task" placeholder="Add new task">
    <input type="submit" value="Add Task">
  </form>
  <ul>
    {% for task in tasks %}
      <li>{{ task.description }} <button class="delete-button" onclick="location.href='/delete/{{ task.id }}'">Delete</button></li>
    {% endfor %}
  </ul>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    with tracer.start_as_current_span("querying_tasks"):
        tasks = Task.query.all()
        request_counter.add(1, {"endpoint": "home"})
    return render_template_string(HOME_HTML, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_description = request.form['task']
    new_task = Task(description=task_description)
    with tracer.start_as_current_span("adding_task"):
        db.session.add(new_task)
        db.session.commit()
        task_counter.add(1)
        request_counter.add(1, {"endpoint": "add"})
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id: int):
    with tracer.start_as_current_span("deleting_task"):
        task_to_delete = Task.query.get(task_id)
        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
        request_counter.add(1, {"endpoint": "delete"})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)