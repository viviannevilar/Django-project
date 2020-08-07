from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import get_object_or_404
from news.models import NewsStory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'person'

    def get_slug_field(self):
        return 'username'

    # def get_context_data(self, **kwargs):
    #     context = super(UserView, self).get_context_data(**kwargs)
    #     context['stories'] = NewsStory.objects.filter(author=self.kwargs.get('username')).order_by('-pub_date')
    #     return context


class UpdateAccountView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = CustomUser
    success_url = reverse_lazy('news:index')
    fields = ["pic"]
    template_name = 'users/updateAccount.html'

    def get_slug_field(self):
        return 'username'

    def test_func(self):
        #user = self.get_object()
        if self.request.user.username == self.kwargs['slug']: #post.author:
            return True
        return False


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, 
#                                    request.FILES, 
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"Your account has been updated.")
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'users/profile.html', context)
