from flask import Flask, render_template
app = Flask(__name__)
#hello index spelling is correct
@app.route("/index")
def first_webpage():

    name = 'Flask'

    return render_template('index.html', index_variable = name)
app.run(debug=True)