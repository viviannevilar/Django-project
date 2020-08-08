from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AddStoryView(LoginRequiredMixin,generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    model = NewsStory

    #the way below was what was originally in the file. 
    # I substituted them by the line model = NewsStory
    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView): #LoginRequiredMixin, UserPassesTestMixin, 
    model = NewsStory
    success_url = reverse_lazy('news:index')
    fields = ["title","content"]
    template_name = "news/updateStory.html"

    # def get_slug_field(self):
    #     return 'username'

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author: #post.author:
            return True
        return False


class UserStoriesView(generic.ListView):
    model = NewsStory
    template_name = 'news/userStories.html' 
    context_object_name = 'stories'
    #paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        return NewsStory.objects.filter(author=user).order_by('-pub_date')


# class MyStoriesView(LoginRequiredMixin, generic.ListView):
#     model = NewsStory
#     template_name = 'news/myStories.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = CustomUser.objects.filter(username=self.request.user).first()
#         context['my_stories'] =  user.post_set.all() 
#         return context
