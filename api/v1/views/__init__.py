#!/usr/bin/python3
"""creating a variable app_views an instance of Blueprint"""
from flask import Blueprint
from . import *
#from api.v1.views.index import *
#from api.v1.views.states import *

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
