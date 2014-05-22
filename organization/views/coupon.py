# coding:UTF-8
from flask import request, render_template
from flask import request, render_template, redirect, url_for
from organization.services.times_service import *

def to_home():
    return render_template('bourjois/home.html')

def to_home2():
    return render_template('bourjois/home2.html')


def to_send():
    return render_template('bourjois/test4.html')

def to_getCoupon():
    return render_template('bourjois/test5.html')

def to_share():
    return render_template('bourjois/share.html')

def get_total_times():
    t = get_times()
    return render_template('bourjois/total.html',
                           t=t)