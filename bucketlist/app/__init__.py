#! /usr/bin/python
# coding: utf8

from flask import request, jsonify, abort

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
	from app.models import Bucketlist
	from app.models import Personne

	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	@app.route('/personnes/', methods=['GET','POST'])
	def personnes():
		result = []
		if request.method == 'GET':
			personnes = Personne.query.all()
			for personne in personnes:
				obj = {
				'id': personne.id,
				'name': personne.name,
				'lastname': personne.lastname,
				'age': personne.age
				}
				result.append(obj)
			response = jsonify(result)
			response.status_code = 200
			return response
		if request.method == 'POST':
			name = request.data.get('name')
			lastname = request.data.get('lastname')
			age = request.data.get('age')
			personne = Personne(name, lastname, age)
			personne.save()
			response = jsonify({
				'id': personne.id,
				'name':personne.name,
				'lastname': personne.lastname,
				'age': personne.age
				})
			response.text ="Personne {} registered !".format(personne.name)
			response.status_code = 200
			return response



	@app.route('/bucketlists/', methods= ['GET', 'POST'])
	def bucketlists():
		if request.method == 'POST':
			# curl -H "Content-Type: application/json" -X POST -d '{"name":"Hello world API"}' http://localhost:5000/bucketlists/
			name = str(request.data.get('name', ''))
			if name:
				bucketlist = Bucketlist(name=name)
				bucketlist.save()
				response = jsonify({
					'id':bucketlist.id,
					'name':bucketlist.name,
					'date_created':bucketlist.date_created,
					'date_modified':bucketlist.date_modified
					})
				response.status_code = 201
				return response
		else:
			#  curl -H "Content-Type: application/json" -X GET http://localhost:5000/bucketlists/
			bucketlists = Bucketlist.get_all()
			results = []
			for bucketlist in bucketlists:
				obj = {
				'id': bucketlist.id,
				'name': bucketlist.name,
				'date_created': bucketlist.date_created,
				'date_modified': bucketlist.date_modified
				}
				results.append(obj)
			response = jsonify(results)
			response.status_code = 200
		return response

	@app.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
	def bucketlist_manip(id, **kwargs):
		bucketlist = Bucketlist.query.filter_by(id=id).first()
		if not bucketlist:
			abort(403)
		if request.method == 'DELETE':
			#curl -H "Content-Type: application/json" -X DELETE -d '{"id":1}' http://localhost:5000/bucketlists/
			bucketlist.delete()
			return {
			'message': 'Bucketlist {} deleted successfully !'.format(bucketlist.id)
			}, 200

		elif request.method == 'PUT':
			name = str(request.data.get('name',''))
			bucketlist.name = name
			bucketlist.save()
			response = jsonify({
				'id':bucketlist.id,
				'name': bucketlist.name,
				'date_created':bucketlist.date_created,
				'date_modified':bucketlist.date_modified
				})
			response.status_code = 200
			return response
		else:
			# curl -H "Content-Type: application/json" -X GET -d '{"name":"Hello world API"}' http://localhost:5000/bucketlists/
			response = jsonify({
				'id': bucketlist.id,
				'name':bucketlist.name,
				'date_created':bucketlist.date_created,
				'date_modified':bucketlist.date_modified
				})
			response.status_code = 200
			return response

	return app
