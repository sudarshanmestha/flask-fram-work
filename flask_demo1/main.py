### Intergrate HTML with Flask
### HTTP verb GET and POST

#jinja2 template engine
"""
{%....%} condition, for loop
{{     }} expression to print output
{#.....#} this is for comments
"""
from flask import Flask, redirect, url_for, render_template, request
### WSGI APPLICATION
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score, 'res':res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has Fail and marks is "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="pass"
    else:
        result="fail"
    return redirect(url_for(result, score=marks))
####result checker HTML page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    return redirect(url_for('success', score=total_score))




if __name__=='__main__':
    app.run(debug=True)
