from flask import Flask
from flask import flash
from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask_login import UserMixin, LoginManager, login_user
from authentication.database.extensions import session, OTP
from authentication.database.model import Users


from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from authentication.mail_message.email_message import MailMessage
from uconra.smtp_mail import SMTP_Mail
from uconra.register import Register
from authentication.j_wt.j_wt import JWT


from config import Config

"""-----------  import modules for regular expressions  -----------"""
import re


login_bp = Blueprint('login', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/login/static',
                     )

"""---------    Route for login Blueprint   ----------"""
@login_bp.route('/',)
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Get user email and password from the user input from the form
    mail = str(request.form.get('email'))
    password = str(request.form.get('password'))

    session['confirm_email'] = request.form.get('email', False)

    register = Register()
    # assign a token variable
    token = JWT()
    # Generate a user token
    user_token = token.generate_jwt_token(mail)

    if request.method == 'POST':

        # check email with regular expressions and display flash message
        if re.match(r"\S[^@]+\S+@[^@]+\S+[a-zA-Z]+\S+\.[^@]", mail):
            pass
        else:
            flash('invalid email')

        # Validate the database email with the user input email
        valid_user_email = Users.query.filter_by(email=mail).first()

        if valid_user_email:

            # instantiate PasswordHasher from argon2-cffi
            ph = PasswordHasher()
            hash = valid_user_email.password

            # Use the try block to catch the exception
            try:

                # Verify the hash in database with the user input password
                if ph.verify(hash, password):

                    if ph.check_needs_rehash(hash):
                        valid_user_email.password(valid_user_email, ph.hash(password))

                    # Check if user has confirmed email in database
                    is_confirmed = valid_user_email.confirmed

                    if is_confirmed == True:

                        # Login the user
                        login_user(valid_user_email)

                        # Display flash message
                        flash(f'You are logged in {valid_user_email.username}')
                        print(is_confirmed)
                        return redirect(url_for('dashboard.dashboard' )) # user_username=valid_user_email.username
                    else:
                        email = register.userEmail(mail)
                        """ -------- Create email message ---------- """
                        confirm_message = MailMessage()
                        sendMail = SMTP_Mail(
                            appKey=Config.APP_PASSWORD, userMail=email,
                            senderMail=Config.MARXZI_EMAIL, serverEhlo=Config.SERVER_EHLO,
                            smtpServer=Config.SMTP_EMAIL_SERVER,
                            subject='CONFIRM EMAIL', userName=valid_user_email.username,
                            message=confirm_message.confirm_message(token=user_token, otp=OTP),
                        )
                        """ -------- Send email ---------- """
                        sendMail.sendMail()

                        flash('To start using our services, please confirm your email account with us! ')
                        return redirect(url_for('confirm.otp_confirm'))
            except VerifyMismatchError:

                # Display a flash message
                print('please enter correct password')
                flash('please enter correct password')
                return redirect(url_for('login.login'))
        else:

            # Display a flash message
            print('please enter correct email')
            flash('please enter correct email')


        pass

    return render_template('login.html',)