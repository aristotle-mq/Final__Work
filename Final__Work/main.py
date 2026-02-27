from flask import Flask, render_template
from register import MyRegisterForm, MyAuthorizationForm


app = Flask(__name__)
with open('token.config', 'r', encoding='utf-8') as file:
    TOKEN = file.read()
app.config['SECRET_KEY'] = TOKEN


@app.route('/', methods=['GET', 'POST'])
def index():
    form_reg = MyRegisterForm()
    form_auth = MyAuthorizationForm()
    if form_reg.validate_on_submit() and form_reg.submit_reg.data:
        print(f"Registration: {form_reg.data}")
        # TODO: сохранить пользователя в БД
        print('Registration is successful')

    if form_auth.validate_on_submit() and form_auth.submit_auth.data:
        print(f"Authorization: {form_auth.data}")
        # TODO: вход пользователя (Flask-login)
        print('Authorization is successful')

    return render_template('index.html', title='ANALYTICS', form_reg=form_reg, form_auth=form_auth)



if __name__ == '__main__':
    app.run()