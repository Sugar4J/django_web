from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import current_datetime,display_mate
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/(\w{1,2})$',current_datetime),
    url(r'^display/$',display_mate),
)
