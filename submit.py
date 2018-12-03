"""
reffered sites:
https://cloud.google.com/natural-language/docs/analyzing-syntax#language-syntax-string-python
http://universaldependencies.org/u/pos/all.html
http://universaldependencies.org/u/pos/

import google cloud language api for natural language processing (syntax analysis)
"""
import flask
from model import Model
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
"""
Define parts of speech to be detected from the user inputed text
where, UNKNOWN:Which cannot be detected ,ADJ: Adjectives, ADP: adposition,ADV: adverb, 
CONJ: conjunctions, DET: articles, Noun: all nouns, NUM: numerals, PRON: pronouns, 
PUNCT: punctuations, VERB: verbs, X:others, AFFIX: All prefixes, suffixes, infixes in sentence
"""
pos_tag = ('UNKNOWN',
           'ADJ',
           'ADP',
           'ADV',
           'CONJ',
           'DET', 
           'NOUN', 
           'NUM', 
           'PRON', 
           'PRT', 
           'PUNCT',
           'VERB',
           'X',
           'AFFIX')

"""
This class is responsile to handle all operations related to suubmitting of text 
inputted by user and doing sysntax analysis of it using google cloud api for 
natural language processing.
"""
class Submit(flask.views.MethodView):
	
	
	def get(self): 
		"""
         	This is a get method responsible to render submit.html form
         	param:
         	return: render form submit.html
         	"""
		return flask.render_template('submit.html')

	def post(self):
		"""
          	This is a post method responsible to retrieve text inputted by user from form
          	convert it into dictionary then sysntax analysis of the retrieved text and pass 
          	the analysed text to AddRecord method of model.py in order to store it into 
          	google cloud datastore.
          	param:
          	return: render form submit.html and pass the syntax analysed to it.
          	"""
		model=Model()
		if 'Submit' in flask.request.form:
			if flask.request.form:
				data=flask.request.form.to_dict(flat=True)
				syntax=syntax_analysis(data['syntax'])
				model=model.AddRecord(syntax)
				return flask.render_template('submit.html', analysis=syntax['analysis'])


def syntax_analysis(text):
	"""
	This method is responsible for the actual syntax analysis of text using google cloud natural language 
	client service and creating list using parts of speech from pos_tag declaration above and tokens 
	analyzed for text.
	param: text: user inputted text for syntax analys
	return: list of data consisting of parts of speech and tokens
	"""
	client=language.LanguageServiceClient()
	document=types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
	syntax=client.analyze_syntax(document=document)
	data=dict()
	data['original']=text
	data['analysis']=['{}:{}'.format(pos_tag[token.part_of_speech.tag],token.text.content) for token in syntax.tokens]
	return data

	
