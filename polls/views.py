from django.shortcuts import render
from django.http import HttpResponse
from models import Question, Choice

def index(request):
	questions = Question.objects.order_by('-pub_date')[:5]

	output = ' , '.join([p.question_text for p in questions])
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You are looking at Question %s" % question_id)

def results(request, question_id):
	return HttpResponse("Your lookign at the results of Question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("Your voting on question %s" % question_id)

