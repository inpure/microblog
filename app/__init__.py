# _*_ encoding: utf-8 _*_
# @Author    : fly
# @Time      : 2022/10/30 0:44
# @Email     :
# @File      : __init__.py
# @License   : Do What The F*ck You Want To Public License
from flask import Flask

app = Flask(__name__)
from app import views
