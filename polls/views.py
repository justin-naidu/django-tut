from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
	questions = Question.objects.order_by('-pub_date')[:5]
	context = {'questions': questions}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
	return HttpResponse("Your lookign at the results of Question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("Your voting on question %s" % question_id)

