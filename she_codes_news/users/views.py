from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import get_object_or_404
from news.models import NewsStory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_slug_field(self):
        return 'username'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        person = User.objects.get(username=self.kwargs['slug'])
        posts = NewsStory.objects.filter(favourites=person.id)
        stories = NewsStory.objects.filter(author=person).order_by('-pub_date')
        context['person'] = person
        context['favourited'] = posts
        context['stories'] = stories
        return context

class UpdateAccountView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = User
    success_url = reverse_lazy('news:index')
    fields = ['first_name', 'last_name', 'pic','bio']
    template_name = 'users/updateAccount.html'

    def get_slug_field(self):
        return 'username'

    def test_func(self):
        if self.request.user.username == self.kwargs['slug']: #post.author:
            return True
        return False

