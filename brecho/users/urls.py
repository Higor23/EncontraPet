from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset'), name='password_reset' ),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]