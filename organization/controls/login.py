# coding: UTF-8
from flask import render_template

def login():
    return render_template('/login.html')