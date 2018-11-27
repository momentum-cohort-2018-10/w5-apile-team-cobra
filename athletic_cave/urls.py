from django.contrib import admin
from django.urls import path, include
from posts import views
from django.contrib.auth.views import ( 
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView,)
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/password/reset/done/', PasswordResetView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
	path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
	path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name="password_reset_complete"),
]
