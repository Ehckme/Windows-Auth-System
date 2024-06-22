"""------------ import modules for sqlalchemy and flask-sqlaclhemy  ------------"""
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import String, Integer, CHAR, Column, ForeignKey
from sqlalchemy import create_engine, Table
from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from .extensions import db
from .extensions import Base


""" --------------  Create a User Model, which is a table for Users with flask-sqlalchemy   ----------- 
"""


class Users(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30) )
    password: Mapped[str] = mapped_column(CHAR(200))

    confirmed: Mapped[bool] = mapped_column(nullable=False, default=False)
    otp: Mapped[int] = mapped_column(nullable=True)
    confirmed_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )
    signup_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())
    lastLogin_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )
    lastLout_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )

    def __repr__(self) -> str:
        return f'Users(id={self.id!r}, username={self.username!r}, ' \
               f'email={self.email!r}, password={self.password!r}, ' \
               f'confirmed={self.confirmed!r}, otp={self.otp!r}'