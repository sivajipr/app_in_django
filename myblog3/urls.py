from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *
# register, register_success, home, logout_page, entry, write_blog

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^allblogs/$', showblogs),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^register/entry/$', entry),
    url(r'^home/$', write_blog),

    # Examples:
    # url(r'^$', 'myblog3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
