from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <body>
                    Человечество вырастает из детства.</br>
                    Человечеству мала одна планета.</br>
                    Мы сделаем обитаемыми безжизненные пока планеты.</br>
                    И начнем с Марса!</br>
                    Присоединяйся!
                  </body>
                </html>"""


@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="secondname" placeholder="Введите фамилию" name="secondname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name"></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group form-check">
                                        </br>Какие у вас есть профессии?
                                    </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">инженер-исследователь</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">пилот</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">строитель</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">врач</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">климатолог</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">астрогеолог</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">гляциолог</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">инженер жизнеобеспечения</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">метеоролог</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">оператор марсохода</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">киберинженер</label>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">штурман</label></br>
                                        <input type="checkbox" class="form-check-input" id="profession" name="profession">
                                            <label class="form-check-label" for="acceptRules">пилот дронов</label>
                                    </div>
                                     <div class="form-group">
                                        <label for="form-check"></br>Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский</br>
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about"></br>Почему вы хотите прнять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo"></br>Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['secondname'])
        print(request.form['name'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
