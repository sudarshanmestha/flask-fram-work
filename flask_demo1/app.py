### Building Url Dynamically
#### variable Rules And URL Building


from flask import Flask, redirect, url_for
### WSGI APPLICATION
app = Flask(__name__)



@app.route('/')
def welcome():
    return'Welcome to my youtube channel'


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>result is pass</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has Fail and marks is "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result, score=marks))




if __name__=='__main__':
    app.run(debug=True)

