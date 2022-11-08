from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories


app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    title = "Madlibs"
    prompts = stories.story.prompts

    return render_template("form.html", title=title, prompts=prompts)


@app.route("/story")
def story():
    title = "Story"
    text = stories.story.generate(request.args)
    return render_template("story.html", title=title, text=text)
