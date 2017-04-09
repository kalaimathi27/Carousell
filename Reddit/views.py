from django.http import HttpResponse
from django.template import loader
from Reddit.logic import get_initial_topics



def index(request):
	
	initial_topics = get_initial_topics()
	context = {"context" : initial_topics}
	template = loader.get_template('Reddit/index.html')
	return HttpResponse(template.render(context, request))