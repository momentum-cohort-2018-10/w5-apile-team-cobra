from django.contrib import admin
from django.urls import path, include
from posts import views
from django.contrib.auth.views import ( 
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView,)
from django.conf import settings


urlpatterns = [
    # registration url
    path('accounts/', include('registration.backends.simple.urls')),

    # password urls
    path('accounts/password/reset', 
        PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'),
        name="password_reset"),
    path('accounts/password/reset/done/',
        PasswordResetView.as_view(
            template_name='registration/password_reset_done.html'),
        name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'), 
        name="password_reset_confirm"),
	path('accounts/password/complete/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'),
        name="password_reset_complete"),

        # comment url
    path('comments/<int:id>/', views.comment_detail, name='comment_detail'),

    # index url
    path('', views.index, name='home'),

    # core url
    path('admin/', admin.site.urls),
]
