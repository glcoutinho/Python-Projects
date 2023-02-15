from flask import Flask, render_template
import requests

post_objects = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/contact')
def receive_data():
    return render_template("contact.html", all_posts=post_objects)


if __name__ == "__main__":
    app.run(debug=True)