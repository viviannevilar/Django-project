from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory, Category
from .forms import StoryForm, CategoryForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        cat_funny = Category.objects.get(name='Funny')
        context['funny'] = NewsStory.objects.filter(category=cat_funny)
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(NewsStory, id=self.kwargs['pk'])
        total_favs = post.fav_count()

        favourited = False
        if post.favourites.filter(id=self.request.user.id).exists():
            favourited = True

        context['total_favs'] = total_favs
        context['story'] = post
        context['favourited'] = favourited 
        return context

def FavouriteView(request,pk):
    post = get_object_or_404(NewsStory, id=request.POST.get('post_fav'))
    favourited = False
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
        favourited = False
    else:
        post.favourites.add(request.user)
        favourited = True
    return HttpResponseRedirect(reverse('news:story', args=[str(pk),]))

class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView): 
    model = NewsStory
    success_url = reverse_lazy('news:index')
    fields = ["title","content"]
    template_name = "news/updateStory.html"

    # def get_slug_field(self):
    #     return 'username'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
        user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        return NewsStory.objects.filter(author=user).order_by('-pub_date')

class CategoryStoriesView(generic.DetailView):
    model = Category
    template_name = 'news/categoryStories.html' 
    context_object_name = 'category'
    
    def get_slug_field(self):
        return 'name'

class UncategorisedStoriesView(generic.TemplateView):
    model = Category
    template_name = 'news/categorynullStories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.filter(category=None)
        context['stories'] = stories
        return context

class CatStoriesView(generic.DetailView):
    model = Category
    template_name = 'news/catStories.html' 
    context_object_name = 'category'
    #paginate_by = 5

    def get_slug_field(self):
        return 'name'

class UncatStoriesView(generic.TemplateView):
    model = Category
    template_name = 'news/catnullStories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.filter(category=None)
        context['stories'] = stories
        return context

class CreateCategoryView(LoginRequiredMixin,UserPassesTestMixin, generic.CreateView):
    form_class = CategoryForm
    context_object_name = 'categoryForm'
    template_name = 'news/createCategory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff 


class AllCategoriesView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'news/allCategories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.filter(category=None)
        context['no_cat'] = stories
        return context

