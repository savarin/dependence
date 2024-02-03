import os
import subprocess
from html import escape
import platform

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

        import os
        import sys
        print(f"HERE HERE HERE {os.name} {platform.system()} {platform.release()} {platform.version()} {platform.platform()}")
        sys.stderr.write(f"HERE HERE HERE {os.name} {platform.system()} {platform.release()} {platform.version()} {platform.platform()}")

        subprocess.run(['yum', 'install', 'git'])

        # Clone the GitHub repo (you may need to handle authentication here)
        subprocess.run(['git', 'clone', 'https://github.com/jxnl/instructor.git'])

        # Run pydeps to generate the SVG file
        subprocess.run(['pydeps', 'instructor/instructor'], check=True)

        # Move the SVG file to the static directory and rename it (you can choose an appropriate name)
        subprocess.run(['mv', 'instructor.svg', 'public/instructor_deps.svg'], check=True)

        # Create the URL for the SVG image
        svg_path = "public/instructor_deps.svg"

        if os.path.isfile(svg_path):
            with open(svg_path, "r") as svg_file:
                svg_content = Markup(svg_file.read())

        import sys
        sys.stderr.write(f"here {type(svg_content)}")

    return render_template("index.html", svg_content=svg_content, url_text=url_text)


if __name__ == "__main__":
    app.run(debug=True)
