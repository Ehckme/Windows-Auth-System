# gunicorn --worker-class=gevent --worker-connection=1000 --workers=1 'app:create_app()'
''' ####################  import flask #########################'''
from flask import Flask
''' ####################  import flask-migrate #########################'''
from flask_migrate import Migrate
''' ####################  import flask-login #########################'''
from flask_login import LoginManager, login_required, login_user, logout_user
''' ####################  import authentication Blueprints #########################'''
from authentication.login.login import login_bp
from authentication.sign_up.sign_up import sign_up_pb
from authentication.confirm.jwt_confirm import jwt_confirm_bp
from authentication.confirm.otp_confirm import otp_confirm_bp
from authentication.account_recovery.account_recovery import account_recovery_bp
from authentication.account_recovery.jwt_reset import jwt_reset_bp
from authentication.account_recovery.otp_reset import otp_reset_bp
from authentication.confirm.resend_token import resend_token_bp
from authentication.confirm.email_confirm import email_confirm_bp
from authentication.confirm.invalid_token import invalid_token_bp
from authentication.confirm.account_active import account_active_bp
from authentication.confirm.invalidReset_token import invalidReset_token_bp
from authentication.confirm.emailReset_confirm import emailReset_confirm_bp
from authentication.confirm.resendReset_token import resendReset_token_bp
from authentication.account_recovery.reset_password import reset_password_bp
from authentication.account_recovery.jwt_reset_password import jwt_reset_password_bp
from dashboard.dashboard import dashboard_bp
from authentication.database.extensions import db, OTP
from authentication.database.model import Users

from config import Config

def create_app(test_config=None):
    app = Flask(__name__)

    """ --------    Create a connection to the database using mysql and + pymysql   -----------"""
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.MARXZI_DATABASE_URI

    """-----------  config secrete key  ---------"""
    app.config['SECRET_KEY'] = Config.FLASK_SECRET_KEY

    """-----------  initialize flask-migrate  ---------"""
    migrate = Migrate(app, db)

    """-----------  initialize database app  ---------"""
    db.init_app(app)
    db.app = app
    app.app_context().push()

    """----------   register authentication blueprints -------"""
    app.register_blueprint(login_bp)
    app.register_blueprint(sign_up_pb)
    app.register_blueprint(jwt_confirm_bp)
    app.register_blueprint(otp_confirm_bp)
    app.register_blueprint(account_recovery_bp)
    app.register_blueprint(jwt_reset_bp)
    app.register_blueprint(otp_reset_bp)
    app.register_blueprint(resend_token_bp)
    app.register_blueprint(email_confirm_bp)
    app.register_blueprint(invalid_token_bp)
    app.register_blueprint(account_active_bp)
    app.register_blueprint(invalidReset_token_bp)
    app.register_blueprint(emailReset_confirm_bp)
    app.register_blueprint(reset_password_bp)
    app.register_blueprint(jwt_reset_password_bp)
    app.register_blueprint(dashboard_bp)
    """----------   register marxzi blueprints -------"""


    """--------------   create the application object   ----------------"""

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.login'

    ''' ##########  Load user from login_manager with their user id. ###########'''
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Users, int(user_id))

    with app.app_context():
        db.create_all()


    return app