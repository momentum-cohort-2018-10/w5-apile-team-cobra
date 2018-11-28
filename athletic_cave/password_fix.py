from django.contrib.auth.views import (
	PasswordResetView, PasswordResetDoneView,
	PasswordResetConfirmView, PasswordResetCompleteView,
)

urlpatterns = [
    ...
    # the new password reset URLs
   	path('accounts/password/reset/',
       PasswordResetView.as_view(
	    template_name='registration/password_reset_form.html'),
        name="password_reset"),
   	path('accounts/password/reset/done/', PasswordResetView.as_view(
	    template_name='registration/password_reset_done.html'), name="password_reset_done"),
   	path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
	    template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
   	path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
            name="password_reset_complete"),
   	path('accounts/', include('registration.backends.simple.urls')),
   	path('admin/', admin.site.urls), ]
