from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory, Category
from .forms import StoryForm, CategoryForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils import timezone
import pytz
from django.db.models import Q
#from django.core.paginator import Paginator

User = get_user_model()
    
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    model = NewsStory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        context['most_fav'] = sorted(list(NewsStory.objects.all()),  key=lambda m: m.fav_count,reverse=True)[:4]
        
        categories = Category.objects.all()
        context['categories'] = []
        for category in categories:
            context['categories'].append( {
                'name': category,
                'stories': NewsStory.objects.filter(category=category)[:4]
            })
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(NewsStory, id=self.kwargs['pk'])
        total_favs = post.fav_count

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

class AddStoryView(LoginRequiredMixin,generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        if '_publish' in self.request.POST:
            form.instance.pub_date = timezone.now()
            #form.save()        
        return super(AddStoryView, self).form_valid(form)
 
class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView): 
    model = NewsStory
    success_url = reverse_lazy('news:index')
    fields = ["title","content","category"]
    template_name = "news/updateStory.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        if '_publish' in self.request.POST:
            form.instance.pub_date = timezone.now()
            #form.save()        
        return super().form_valid(form)

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author: 
            return True
        return False

class DeleteStoryView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')
    template_name = 'news/deleteStory.html'
    success_message = "Story Deleted Successfully"

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteStoryView, self).delete(request, *args, **kwargs)

class UserStoriesView(generic.ListView):
    model = NewsStory
    template_name = 'news/userStories.html' 
    context_object_name = 'stories'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        stories = NewsStory.objects.filter(pub_date__isnull = False).filter(author=user).order_by('-pub_date')
        return stories

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = User.objects.get(username=self.kwargs.get('username'))
        return context
  
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

class AllCategoriesView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'news/allCategories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.filter(category=None)
        context['no_cat'] = stories
        return context

class CreateCategoryView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin, generic.CreateView):
    form_class = CategoryForm
    context_object_name = 'categoryForm'
    template_name = 'news/createCategory.html'
    success_url = reverse_lazy('news:index')
    success_message = "Category created successfully!"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff 

class SearchResultsView(generic.ListView):
    model = NewsStory
    template_name = 'news/search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            object_list = NewsStory.objects.filter(pub_date__isnull = False).filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query) 
            )

            #object_list = object_list.distinct()
        else:
            object_list = None
        return object_list

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['count'] = object_list.count()
    #     return context
