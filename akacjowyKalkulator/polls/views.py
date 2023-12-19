from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import question, choice


class indexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'
    
    def get_queryset(self):
        return question.objects.order_by('-pubDate')[:5]

class detailView(generic.DetailView):
    model = question
    template_name = "polls/detail.html"


class resultsView(generic.DetailView):
    model = question
    template_name = "polls/results.html"


def vote(request, questionId):
    q = get_object_or_404(question, pk = questionId)
    try:
        selectedChoice = q.choice_set.get(pk = request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': q,
                'errorMessage': 'wybieraj kurwo a nie odpierdalasz',
            },
        )
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (questionId,)))
