from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # #output = ','.join([q.question_text for q in latest_question_list])
    # #template = loader.get_template('polls/index.html')
    # context ={
    #     'latest_question_list': latest_question_list
    # }
    # return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You are the polls index.")
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions."""
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # question = get_object_or_404(Question, pk=question_id)
    # context = {'question': question}
    # return render(request, 'polls/detail.html', context )
    # return HttpResponse(
    #     "You are looking at the question %s." % question_id
    # )
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# def results (request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context )
    # response = "You are looking at the results of question %s."
    # return HttpResponse(
    #     response % question_id
    # )

def vote (request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    
    
    # return HttpResponse(
    #     "You are voting on question %s." % question_id
    # )