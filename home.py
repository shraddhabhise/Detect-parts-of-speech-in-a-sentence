import flask
from model import Model

"""
This class displays all analyzed syntaxes retreived from the datastore
:param: flask.view.MethodView: pass MethodView of flask
"""

class Home(flask.views.MethodView):
       def get(self):
        """
        This method displays all analyzed syntaxes retreived from the datastore
        :param:  
        :return:render form(home.html), data: data retrieved from 
        fetchall method of model.py
        """
        model=Model()
        data= model.fetchall()
        return flask.render_template('home.html', data=data) 

