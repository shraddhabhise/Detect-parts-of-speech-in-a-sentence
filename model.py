import flask
from IModel import IModel
from google.cloud import datastore
	
"""
class inherited from abstract class Imodel
"""
class Model(IModel):
	def fetchall(self):
		"""
		Query to fetch all rows from datastore
		:return: list of dict containing of all records from the table
		"""
		client=datastore.Client()
		query=client.query(kind='SyntaxAnalysis')
		entities =query.fetch(None)
		return entities

	def AddRecord(self, data):
		"""
		Query to insert data into the table in datastore
		from the populated data in the form
		:return:syntax of the string
		"""
		client=datastore.Client()
		entity=datastore.Entity(key=client.key('SyntaxAnalysis'))
		entity['original']=data['original']
		entity['analysis']=data['analysis']
		client.put(entity)
