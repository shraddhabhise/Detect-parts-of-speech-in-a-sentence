from abc import ABCMeta, abstractmethod

class IModel:
	"""
	Abstract class to represent model
	"""
	__metaclass__ = ABCMeta
	@abstractmethod
	def fetchall(self,data):
		"""
		Abstract method to fetchall records from datastore
		"""
		pass

	@abstractmethod
	def AddRecord(self,data):
		"""
	 	Add analysed syntax to datastore
	 	"""
		pass


