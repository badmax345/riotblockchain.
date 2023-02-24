from flask import Blueprint, render_template

views = Blueprint ( __name__, "view" )


@main.route('/')
def home ():
    return render_template("index.html")