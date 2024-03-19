from flask import Flask, render_template
import requests
from post import Post

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
posts_json = response.json()
post_obj_list = [Post(post["title"], post["subtitle"], post["body"], post["id"]) for post in posts_json]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", post_objects=post_obj_list)


@app.route('/post/<index>')
def get_post(index):
    for post in post_obj_list:
        # For some reason, index parameter passed from index.html using url_for() returns as a string.
        if post.id == int(index):
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
