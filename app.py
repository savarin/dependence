import os
import subprocess
from html import escape

from flask import Flask, render_template, request, url_for
from markupsafe import Markup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    svg_image_url = None
    svg_content = None
    url_text = ""

    if request.method == "POST":
        url_text = escape(request.form["urlInput"])

        # Clone the GitHub repo (you may need to handle authentication here)
        # subprocess.run(['git', 'clone', 'https://github.com/jxnl/instructor.git'])

        # Run pydeps to generate the SVG file
        # subprocess.run(['pydeps', 'instructor/instructor'], check=True)

        # Move the SVG file to the static directory and rename it (you can choose an appropriate name)
        # subprocess.run(['mv', 'instructor.svg', 'static/instructor_deps.svg'], check=True)

        # Create the URL for the SVG image
        svg_path = 'static/instructor_deps.svg'

        if os.path.isfile(svg_path):
            with open(svg_path, 'r') as svg_file:
                svg_content = Markup(svg_file.read())

    return render_template("index.html", svg_content=svg_content, url_text=url_text)


if __name__ == "__main__":
    app.run(debug=True)