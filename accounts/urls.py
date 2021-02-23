from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

from .views import PasswordsChangeView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('', views.logout_view, name="logout"),

    path('password_change/', PasswordsChangeView.as_view(template_name='registrations/password_change.html',
                                                         success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),

    path('password_change_done/done/',
         views.password_change_done_view, name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registrations/password_reset_form.html',
                                                                 success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),

    # path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registrations/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
         name='password_reset_complete'),

    # path('password_reset/done/',
    # auth_views.PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),
    # name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # path('reset/done/',
    # auth_views.PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
    # name='password_reset_complete'),
]
