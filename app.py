
#Helps in generating the Flask app
from flask import Flask, render_template, request, redirect

from models import create_tasks_tables, get_all_tasks, add_task, mark_task_completed, delete_task   

create_tasks_tables()  # Ensure the database and tables are created at startup
app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route("/tasks")
def tasks_page():
    tasks = get_all_tasks() #Fetches all taks
    return render_template('tasks.html', tasks=tasks) #Renders the tasks.html template with the tasks data


@app.route("/add", methods =["GET"])
def add_page():
    #Shows the add page to user
    return render_template("add_task.html")

@app.route("/add", methods=["POST"])
def add_task_submit():
    #Shows the user a page of their sumbited task
    title = request.form["title"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    category = request.form["category"]
    priority = float(request.form["priority"])

    #Adds task to database
    add_task(title, description, due_date, category, priority)

    #Return user to home page
    return redirect("/tasks")

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    mark_task_completed(task_id)
    return redirect("/tasks")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect("/tasks")

if __name__ == '__main__':
    app.run(debug=True) 