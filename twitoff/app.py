from flask import Flask
from .db_model import DB, User
from .db_model import DB, Tweet


def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/marianvinas/DSPT7-Twitoff/twitoff.sqlite"  # for absolute path- mac
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)  # Connect Flask app to SQLAlchemy DB

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    @app.route('/<tweet>/<user_id>')
    def tweet(tweet, user_id, username):
        tweet = Tweet(tweet=tweet, user_id=user_id, username=username)
        #DB.session.add(tweet)
        #DB.session.commit()

        return f'{username} post a tweet!'

    return app