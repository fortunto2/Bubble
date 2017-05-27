#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bubble Copyright © 2017 Il'ya Semyonov
# License: https://www.gnu.org/licenses/gpl-3.0.en.html
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^redirect/$', views.initialization),
    url(r'^pending/$', views.pending),
    url(r'^success/$', views.success),
    url(r'^fail/$', views.fail),
    url(r'^$', views.index)
]
