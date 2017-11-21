from flask import Flask, render_template, url_for
app = Flask(__name__)

#Unused route. Just tells user where content is
@app.route("/")
def root():
    return "Hello friends. localhost:5000/main is the site you are looking for"

#Defines route to the 'Main menu' for this project
@app.route('/main/')
def main():
    return render_template("templates.html")

#Defines route to Ekans 
@app.route('/ekans')
def ekans():
    return render_template("ekans.html")

#Defines route to Magnemite 
@app.route('/magnemite')
def mag():
    return render_template("magnemite.html")

#Defines route to Trumbeak 
@app.route('/trumbeak')
def tru():
    return render_template("trumbeak.html")

#Defines route to Rockruff 
@app.route('/rockruff')
def rock():
    return render_template("rockruff.html")

#Defines route to Torracat 
@app.route('/torracat')
def torr():
    return render_template("torracat.html")

#Defines route to Gastly 
@app.route('/gastly')
def gast():
    return render_template("gastly.html")

#Puts the project online
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
