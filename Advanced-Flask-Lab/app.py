from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://scontent.ftlv21-1.fna.fbcdn.net/v/t31.18172-1/1502644_10152506946962507_2442851309927378964_o.png?stp=c49.0.148.148a_dst-png_p148x148&_nc_cat=111&ccb=1-7&_nc_sid=1eb0c7&_nc_ohc=d-R_wjIm2d8AX_NugPv&_nc_ht=scontent.ftlv21-1.fna&oh=00_AT8CSjiG8-biys_qQ9tU-yrxzJSp6HANxsz5c3mFVk-G2Q&oe=62FD0A1B"

user_bio = "this page is dedicated to birds?"

posts = {
    "static/images/thumbs/img3.jpeg": "birds again",
    "static/images/thumbs/img4.jpeg": "and again",
    "static/images/thumbs/img5.jpeg": "and again",
    "static/images/thumbs/img6.jpeg": "help"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', img=image_link, user=user_bio, posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
