import requests
from flask import Flask
from flask import flash
from flask import Blueprint
from flask import request, render_template, redirect, url_for


class MailMessage:
    def __init__(self,):
        pass
    def confirm_message(self, user=None, otp=None, content=None, url=None, token=None, *args):
        self.user = user
        self.content = content
        self.message = message = f""" <!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Website Layout</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div class="header">
  <h1>Confirm Email </h1>
</div>
 <p> Click the link to confirm email --> : http://127.0.0.1:5000/jwt-confirm/{token}  </p> </br> </br>
 
 <h3> or copy and type this otp code to confirm <h2> {otp} </h2> </h3> </br> 
 <h3> as an alternative </h3>
 
</body>
</html>

"""

        return self.message

    def reset_message(self, user=None, otp=None, content=None, url=None, token=None, *args):
        self.reset_message = reset_message = f""" <!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Website Layout</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div class="header">
  <h1> Reset Password </h1>
</div>
 
 
  <h3> copy and type this otp code to reset <h2> {otp} </h2> </h3> </br> 
 <h3> as an alternative </h3>
</body>
</html>

"""
        return self.reset_message


if __name__ == '__main__':
    message = MailMessage()
    print(message.create_message())







