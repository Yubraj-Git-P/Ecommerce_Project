from flask import flask

def create_lugakin_aapp():
    app=Flask(__name__)
    app.config['SECRET_KEY']='dkjjdsjgek'
    
    from .views import views #import the blue print from the views 
    from .auth import auth # import the blueprint file from the auth

    app.register_blueprint(views,url_prefix='/')# how url are fetch or used by url_prefix
    app.register_blurprint(auth,url_prefix='/')# all url related to auth ie authentication

    return app