from django.http import HttpResponse
from django.template import loader
from Reddit.logic import get_initial_topics
import json

initial_topics = get_initial_topics()

def index(request):
	topics = sorted(initial_topics, key=lambda k: k['upvotes'])
	context = {"context": json.dumps(topics)}
	template = loader.get_template('Reddit/index.html')
	return HttpResponse(template.render(context, request))