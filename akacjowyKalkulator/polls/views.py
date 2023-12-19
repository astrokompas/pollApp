from django.http import HttpResponse
from .models import question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    latestQuestionList = question.objects.order_by('-pubDate')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionList': latestQuestionList,
    }
    return HttpResponse(template.render(context, request))

def detail(request, questionId):
    q = get_object_or_404(question, pk = questionId)
    return render(request, "polls/detail.html", {"q": q})


def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)


def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
