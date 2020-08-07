from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import get_object_or_404

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_slug_field(self):
        return 'username'

    # def get_queryset(self):
    #     user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
    #     return CustomUser.objects.filter(username=user)



# class UpdateAccountView(UpdateView):
#     model = CustomUser
#     success_url = reverse_lazy('home')
#     form_class = CustomUserChangeForm
#     template_name = 'users/updateAccount.html'


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
