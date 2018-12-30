from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import UserProfile

# Create your views here.

User = get_user_model()


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    # def get_object(self, queryset=None):
    #     return get_object_or_404(User, username__iexact=self.kwargs.get('username'))
    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(user=self.request.user, followed_by_user=self.get_object())
        context['following'] = following
        return context


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=self.kwargs.get("username"))
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect('profiles:user-detail', username=username)

