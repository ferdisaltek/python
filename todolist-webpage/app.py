from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_index>')
def delete(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
