"""restframework_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url,include, patterns
from django.contrib import admin
from but_moim.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', 'django.contrib.auth.views.login', {
        'authentication_form': LoginForm
    }, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/login/',
    }, name='logout'),

    url(r'^moim_list/',
        'but_moim.views.moim_list',
        name='moim_list'),

    url(r'^moim_detail/(?P<moim_name>[\w.@+-]+)/$',
        'but_moim.views.moim_detail',
        name='moim_detail'),

    url(r'^moim_detail_post/',
        'but_moim.views.moim_detail_post',
        name='moim_detail_post'),

    url(r'^moim_join/',
        'but_moim.views.moim_join',
        name='moim_join'),

    url(r'^moim_search/',
        'but_moim.views.moim_search',
        name='moim_search'),

    url(r'^moim_search_join/(?P<moim_name>[\w.@+-]+)/$',
        'but_moim.views.moim_search_join',
        name='moim_search_join'),

    url(r'^user_deposit/',
        'but_moim.views.user_deposit',
        name='user_deposit'),

    url(r'^signup/',
        'but_moim.views.signup',
        name='signup'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
