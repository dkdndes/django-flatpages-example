from django.conf.urls import patterns, include, url

# Setting for STATIC_URL i developement environment
from django.conf import settings
from django.conf.urls.static import static

# Django Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Tinymce requires access to static files
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# djangoproject.com documentation, works with /pages ...
# (r'^pages/', include('django.contrib.flatpages.urls')),
urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)
