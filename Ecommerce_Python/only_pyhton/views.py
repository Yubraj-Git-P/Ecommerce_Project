from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')# whenever passe through route / goes to landing page 
def home_page():
    return "<h1>Landing page</h1>"