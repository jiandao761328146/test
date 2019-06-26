# -*- coding: utf-8 -*-

import flask
from Model.models import session, User
import traceback

home_api = flask.Blueprint('home_api', __name__)


@home_api.route('/home', methods=['get'])
def home():

    response = {
        "User": {},
        'msg': 'success'
    }
    try:
        user_id = flask.request.args['id']

        user = session.query(User).filter(User.id == user_id).one()
        response['User']['name']=user.name
        response['User']['age']=user.age
        response['User']['gender']=user.gender
    except Exception as e:
        response['msg'] = str(e)
    return flask.jsonify(response)


@home_api.route('/register_user', methods=['post'])
def register_user():
    response = {
        'msg': 'success'
    }
    try:
        name = flask.request.get_json()['name']
        gender = flask.request.get_json()['gender']
        age = flask.request.get_json()['age']

        user = User()
        user.name = name
        user.gender = gender
        user.age = age

        session.add(user)
        session.commit()
    except Exception as e:
        traceback.print_exc()
        session.rollback()
        response['msg'] = str(e)
    return flask.jsonify(response)
