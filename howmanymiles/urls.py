from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^howmanymiles/', include('howmanymiles.foo.urls')),

    url(r'^$', 'howmanymiles.views.home', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
