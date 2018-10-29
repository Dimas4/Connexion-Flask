from uuid import uuid4

from app.db.db import User, init_db


db_session = init_db("postgresql://adminq:passwordq@localhost/dbnameq")


def get_all_users():
    users = db_session.query(User)
    return [user.dump() for user in users]


def get_user_by_id(uuid):
    user = db_session.query(User).filter(User.uuid == uuid).one_or_none()
    return user.dump() or {'error': 'user does not exist'}


def create_user(user):
    if 'name' not in user or len(user) != 1:
        return {'error': 'bad request'}

    uuid = str(uuid4())
    user = User(uuid=uuid, name=user['name'])
    return_user = user.dump()
    db_session.add(user)
    db_session.commit()
    return return_user
