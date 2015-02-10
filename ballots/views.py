from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from ballots.models import Poll, Ballot, Vote, Category, CategoryItem
from django.contrib.auth.decorators import login_required
from registration.users import UserModel
from registration import signals
from django.contrib.auth import authenticate
from django.contrib.auth import login


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


class PollDetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class PollResultsView(LoginRequiredMixin, generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def create_user_from_poll(request):
    username = request.POST['username']
    email = request.POST['email']
    password = UserModel().objects.make_random_password()
    UserModel().objects.create_user(username, email, password)

    new_user = authenticate(username=username, password=password)
    login(request, new_user)
    signals.user_registered.send(sender=None,
                                 user=new_user,
                                 request=request)

    return new_user


def vote(request, slug):

    poll = get_object_or_404(Poll, slug=slug)

    user = request.user
    if request.user.is_anonymous():
        user = create_user_from_poll(request)

    ballot = Ballot(person=user)
    ballot.save()

    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken' \
                and key != 'username' \
                and key != 'email':

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

