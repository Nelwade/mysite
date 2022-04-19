from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context ={
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You are the polls index.")
# Create your views here.

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context )
    # return HttpResponse(
    #     "You are looking at the question %s." % question_id
    # )

def results (request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(
        response % question_id
    )

def vote (request, question_id):
    return HttpResponse(
        "You are voting on question %s." % question_id
    )