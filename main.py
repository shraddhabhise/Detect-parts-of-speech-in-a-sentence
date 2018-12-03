import flask
"""
Class for retrieving index page
"""
class Main(flask.views.MethodView):
	def get(self):
		"""
		Method to render index page
		"""
		return flask.render_template('index.html')

