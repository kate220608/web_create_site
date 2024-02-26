from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def print_answers():
    css = url_for('static', filename='css/style.css')
    title, surname, name, education, profession, sex, motivation, ready = ("Анкета", "Wathy", "Mark", "выше среднего", "штурман марсоход", "male", "всегда мечтал застрять на марсе!", "True")
    return render_template('auto_answer.html', css=css, title=title, surname=surname, name=name,
                           education=education, profession=profession, sex=sex, motivation=motivation, ready=ready)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')