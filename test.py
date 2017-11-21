from flask import Flask, render_template, url_for
app = Flask(__name__)

#Unused route. Just tells user where content is
@app.route("/")
def root():
    return "Hello friends. localhost:5000/main is the site you are looking for"

#Defines route to the 'Main menu' for this project
@app.route('/main/')
def types():
    return render_template("templates.html")

#Puts the project online
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
