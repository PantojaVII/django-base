from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django import forms

class AdminUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    is_staff = forms.BooleanField(required=False, initial=True, help_text="Permite acesso ao admin")
    is_superuser = forms.BooleanField(required=False, help_text="Concede todos os privilégios")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "is_staff", "is_superuser")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_staff = self.cleaned_data["is_staff"]
        user.is_superuser = self.cleaned_data["is_superuser"]
        if commit:
            user.save()
        return user

def admin_register_view(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Define como membro da equipe por padrão
            user.save()
            messages.success(request, f'Usuário {user.username} criado com sucesso!')
            return redirect('admin:index')
    else:
        form = AdminUserCreationForm(initial={'is_staff': True})
    
    return render(request, 'admin/register.html', {'form': form})

class AdminPasswordResetView(PasswordResetView):
    template_name = 'admin/password_reset.html'
    email_template_name = 'admin/password_reset_email.html'
    subject_template_name = 'admin/password_reset_subject.txt'
    success_url = reverse_lazy('admin_password_reset_done')
    
class AdminPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'admin/password_reset_confirm.html'
    success_url = reverse_lazy('admin_password_reset_complete')

def admin_password_reset_done(request):
    return render(request, 'admin/password_reset_done.html')

def admin_password_reset_complete(request):
    return render(request, 'admin/password_reset_complete.html')
