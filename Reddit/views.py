import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from Reddit.logic import get_initial_topics
from Reddit.utils import Utils



topics = get_initial_topics()

def index(request):
	utils_obj = Utils()
	topics_dict_list = []
	for topic in topics:
		topic_dict = utils_obj.get_topic_dict(topic)
		topics_dict_list.append(topic_dict)
	topics_dict_list = utils_obj.sort_topics(topics_dict_list)
	context = {"context": json.dumps(topics_dict_list)}
	template = loader.get_template('Reddit/index.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
def track_votes(request):
	utils_obj = Utils()
	request_obj = json.loads(request.body)
	title_id = request_obj["titleid"]
	vote_category = request_obj["votes"]
	for topic in topics:
		if topic.titleid == title_id:
			topic.track_votes(vote_category)
	return HttpResponse('')


@csrf_exempt
def add_user(request):
	import pdb;pdb.set_trace()
	request_obj = json.loads(request.body)
	username = request_obj["username"]
	email = request_obj["email"]
	
	pass
	
	