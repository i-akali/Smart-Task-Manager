
#Helps in generating the Flask app
from flask import Flask, render_template, request, redirect

from models import create_tasks_tables, get_all_tasks, add_task, mark_task_completed, delete_task, get_all_completed_tasks, update_task , get_task

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

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    mark_task_completed(task_id)
    return redirect("/tasks")

@app.route("/delete/<int:task_id>")
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect("/tasks")

@app.route("/completed")
def completed_tasks_page():
    completed_tasks= get_all_completed_tasks() #Fetches all completed tasks
    return render_template("completed_tasks.html", tasks=completed_tasks)

@app.route("/edit/<int:task_id>")
def edit_task(task_id):
    task = get_task(task_id)
    return render_template("edit_task.html", task=task)

@app.route("/edit/<int:task_id>", methods = ["POST"])
def save_task(task_id): #Creates a form to update task specifics
    title = request.form["title"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    category = request.form["category"]
    priority = request.form["priority"]

    #Updates task with new information
    update_task(task_id, title, description, due_date, category, priority)

    return redirect("/tasks") #Redirects to home page


if __name__ == '__main__':
    app.run(debug=True) 