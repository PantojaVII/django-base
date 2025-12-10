from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    admin_register_view, 
    AdminPasswordResetView, 
    AdminPasswordResetConfirmView,
    admin_password_reset_done,
    admin_password_reset_complete
)


urlpatterns = [
    path('', include('configs_project.urls')),  # Site raiz
    path('admin/', admin.site.urls),
    path('account/register/', admin_register_view, name='admin_register'),
    path('account/password_reset/', AdminPasswordResetView.as_view(), name='admin_password_reset'),
    path('account/password_reset/done/', admin_password_reset_done, name='admin_password_reset_done'),
    path('account/reset/<uidb64>/<token>/', AdminPasswordResetConfirmView.as_view(), name='admin_password_reset_confirm'),
    path('account/reset/done/', admin_password_reset_complete, name='admin_password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
