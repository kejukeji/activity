# coding: UTF-8

from organization.models.database import Base, engine
from organization.models.t_user import UserClass


if __name__ == '__main__':
    Base.metadata.create_all(engine)