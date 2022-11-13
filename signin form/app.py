from flask import Flask, render_template, request
from form import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hudi'


@app.route('/')
def home():
    return "Hello world"


@app.route('/blog')
def blog():   
    post = [ {'title':'Technology in 2019', "author":"avi" },
     {'title':'explanasion of oil in Russia', "author":"Bob" }]
    return render_template('blog.html', author="Bob", sunny=True, posts=post)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__=='__main__':
    app.run(debug=True)

