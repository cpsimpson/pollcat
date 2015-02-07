from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from ballots.models import Poll, Ballot, Vote, Category, CategoryItem
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class PollIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('-id')[:5]



class PollDetailView(LoginRequiredMixin, generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class PollResultsView(LoginRequiredMixin, generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


@login_required
def vote(request, slug):

    poll = get_object_or_404(Poll, slug=slug)

    ballot = Ballot(person=request.user)
    ballot.save()

    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            try:
                category = poll.category_set.get(slug=key)
                item = CategoryItem.objects.get(id=value)

                category_vote = Vote(ballot=ballot,
                                     category=category,
                                     item=item)
                category_vote.save()
            except (KeyError, Category.DoesNotExist,
                    CategoryItem.DoesNotExist):
                return render(request, 'polls/detail.html', {
                              'poll': poll,
                              'error_message': "You didn't select a choice.",
                              })

    return HttpResponseRedirect(reverse('polls:results', args=(poll.slug,)))

