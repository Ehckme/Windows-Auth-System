"""
The following below code is for connecting  to an existing
database and creating new table using SQLAlchemy 2.22 version
It inherits from sqlalchemy.orm DeclarativeBase

Please check for latest version updates and update when necessary!

"""

# import SQLAlchemy
from __future__ import annotations
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from typing import List
from sqlalchemy import ForeignKey, String, Integer, CHAR, Boolean, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import Session

# create an inheritance class from declarativeBase
class Base(DeclarativeBase):
    pass


# Create an association tabele for both tables to merge
# note for a Core table, we use the sqlalchemy.column construct
# not sqlalchemy.orm.mapped_column




# Create User a Table class
class Uconra(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
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
               f'email={self.email}, password={self.password}, ' \
               f'confirmed={self.confirmed}, otp={self.otp}, ' \
               f'signup_at={self.signup_at}, lastlogin_at={self.lastLogin_at},' \
               f'lastLogout_at={self.lastLout_at}'
    ''' ############# Student Table #################  '''





connection_string = 'mysql+pymysql://root:root@localhost/Uconra'
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    motchello  = Uconra(
        username='motchello',
        email='motchello@gmail.com',
        password='1234',
        confirmed=True,


    )
    lerato = Uconra(
        username='Lerato',
        email='lerato@yahoo.com',
        password='FuckMe#!',
        confirmed=True,

    )


    # Add
    session.add_all([motchello, lerato])
    session.commit()