from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def print_answers():
    css = url_for('static', filename='css/style.css')
    title, surname, name, education, profession, sex, motivation, ready = ("Анкета", "Wathy", "Mark", "выше среднего", "штурман марсоход", "male", "всегда мечтал застрять на марсе!", "True")
    return render_template('auto_answer.html', css=css, title=title, surname=surname, name=name,
                           education=education, profession=profession, sex=sex, motivation=motivation, ready=ready)


@app.route('/distribution')
def print_list():
    css = url_for('static', filename='css/style.css')
    names = ["ghntihgurhut", "rmjrg"]
    return render_template("cabin_list.html", names=names)


@app.route('/table/<sex>/<age>')
def show_cabin(sex, age):
    css = url_for('static', filename='css/style.css')
    if sex == "male":
        img_1 = url_for('static', filename='img/male.jpg')
    else:
        img_1 = url_for('static', filename='img/female.jpg')
    if int(age) < 21:
        img_2 = url_for('static', filename='img/young.jpg')
    else:
        img_2 = url_for('static', filename='img/old.jpg')
    return render_template("cabin_look.html", img_1=img_1, img_2=img_2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')