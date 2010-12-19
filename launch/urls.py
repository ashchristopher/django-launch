from django.conf.urls.defaults import *

urlpatterns = patterns('launch.views',
    url(r'^$', 'signup', name='launch_page'),
    url(r'^success/$', 'success', name='launch_page_success'),
)
