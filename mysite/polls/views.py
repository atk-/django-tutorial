from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, qid):
    question = get_object_or_404(Question, pk=qid)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, qid):
    return HttpResponse(f"You're looking at the results of question {qid}.")

def vote(request, qid):
    question = get_object_or_404(Question, pk=qid)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected.votes += 1
        selected.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

