from flask import Flask, request, render_template
from stories import story


app = Flask(__name__)

@app.route("/")
def index():
    title = "Madlibs"
    prompts = story.prompts
    
    return render_template("form.html",title, prompts)

@app.route("/story")
def story():
    title = "Story"
    text = story.generate(request.args)
    return render_template("story.html",title, text)

