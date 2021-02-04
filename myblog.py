#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on wed jan  27 22:04:10 2021

@author: pratiksha

"""
from flask import Flask,render_template

app = Flask(__name__)
List_of_posts = [
    {

        'author': 'Pratiksha Pawar',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted':'Feb 1, 2021'

    },
    {
        'author':'Aarya Rayna',
        'title': 'Blog post 1',
        'content':'First post content',
        'date_posted':'Feb 2, 2021'

    }
]

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', List_of_posts = List_of_posts)

@app.route("/about")
def about():
    return render_template('about.html',title ='About')


if __name__=="__main__":
    app.run(debug=True)
