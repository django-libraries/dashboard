from django.urls import path
from dashboards import views as dashboards_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboards_views.DashboardView.as_view(), name='index'),
    path('billing/', dashboards_views.billing, name='billing'),
    path('tables/', dashboards_views.tables, name='tables'),
    path('vr/', dashboards_views.vr, name='vr'),
    path('rtl/', dashboards_views.rtl, name='rtl'),
    path('profile/', dashboards_views.profile, name='profile'),

    # Authentication
    path('accounts/login/', dashboards_views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', dashboards_views.logout_view, name='logout'),
    path('accounts/register/', dashboards_views.register, name='register'),
    path('accounts/password-change/', dashboards_views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', dashboards_views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',
         dashboards_views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
