from flask import Flask, render_template

app = Flask(__name__)

students:list = [
    {'idno':'1000','lastname':'oscar','firstname':'papa','course':'bsit','level':'3',},
    {'idno':'2000','lastname':'sierra','firstname':'yankee','course':'bscs','level':'4',},
    {'idno':'3000','lastname':'whiskey','firstname':'uniform','course':'bsis','level':'3',},
    {'idno':'4000','lastname':'bravo','firstname':'victor','course':'bsba','level':'2',},
    {'idno':'5000','lastname':'delta','firstname':'charlie','course':'bse','level':'2',},
]

@app.route("/")
def index()->None:
    return render_template("index.html",slist=students,pagetitle="student list")
    
if __name__=="__main__":
    app.run(debug=True)