#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=2 tabstop=2 expandtab textwidth=79:
'''@author: Difan Zhang <tifan@ifanr.com>
@license: New BSD License
@see: README.rst


A simple Flask based Event API handler.
'''
from flask import Flask, request
from flask.ext.restful import Api, Resource
import pprint


app = Flask(__name__)
api = Api(app)


class EventAPIDemo(Resource):

  def post(self):
    return message_handler(request.json), 200



def message_handler(msg):
  pprint.pprint(msg)
  return {'message_type': 'text',
          'payload': 'Yay, you said %s' % msg['message_content']}


api.add_resource(EventAPIDemo, '/demo')


if __name__ == "__main__":
  app.run()
