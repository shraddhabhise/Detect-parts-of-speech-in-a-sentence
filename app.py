"""
all files and packages required 
"""
import flask, flask.views
from main import Main
from submit import Submit
from home import Home

app = flask.Flask(__name__)

"""Route for index page: to redirect to either Listing all analyzed syntaxes 
for texts or for user to do syntax analysis"""

app.add_url_rule('/', view_func=Main.as_view('index'),methods=["GET","POST"])

""" Route for a form to submit a text for syntax analysis
"""
app.add_url_rule('/submit', view_func=Submit.as_view('submit'),methods=["GET","POST"])

"""
Route to list all analyzed syntaxes for texts
"""
app.add_url_rule('/home', view_func=Home.as_view('home'),methods=["GET","POST"])

app.debug=True

"""
To define entrypoint 
"""
if __name__=='__main__':
	app.run(host='0.0.0.0', port=8000,debug=True)
 
