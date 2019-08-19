from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.views.static import serve

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1/', include(('encuestas.users.urls', 'users'), namespace='users')),
    path('api/v1/', include(('encuestas.api.urls', 'api'), namespace='api')),
    re_path(r'^(?:.*)/?', include(('encuestas.encuesta.urls', 'encuesta'), namespace='encuesta')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
