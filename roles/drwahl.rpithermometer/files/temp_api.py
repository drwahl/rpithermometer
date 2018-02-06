#!/usr/bin/env python
import os
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Temperature(Resource):
    @app.route("/")
    def get(self):
        
        sensors = {}
        for root, dirnames, filenames in os.walk('/sys/bus/w1/devices'):
            for dirname in dirnames:
                slave_file = root + '/' + dirname + '/' + 'w1_slave'
                if os.path.isfile(slave_file):
                    celsius = self._get_value_from_file(slave_file)*.001
                    fahrenheit = (celsius * (9.0/5.0)) + 32.0
                    sensors[dirname] = { 'celsius': round(celsius, 2),
                                         'fahrenheit': round(fahrenheit, 2) }
        return sensors


    def _get_value_from_file(self, target):
        """Extract and return the temperature value from the file the driver creates"""

        target_file = open(target, 'r')
        lines = target_file.readlines()
        target_file.close()
        return int(lines[-1].strip().split('=')[1] or 0)


api.add_resource(Temperature, '/temperature')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5001)
