from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.db.models import Q
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import LoginForm, SignUpForm, PasswordChangingForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in user next time
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # log in user next time
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('homepage')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('password_change_done')


# class PasswordChangeDoneViews(PasswordChangeDoneView):
# form_control = PasswordChangingDoneView()
def password_change_done_view(request):
    auth.logout(request)
    return render(request, 'registrations/password_changed_done.html')


# def password_reset(request):
# return render(request, 'registrations/password_reset_form.html')
"""def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registrations/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect('homepage')
            messages.error(request, 'An invalid email has been entered.')
        password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registrations/password_reset_form.html",
                  context={"password_reset_form": password_reset_form})"""
