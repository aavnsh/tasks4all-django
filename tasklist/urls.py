from django.conf.urls import url
from django.contrib import admin

from tasklist import views

urlpatterns = [
    url(r'^mine/$', views.view_list, {'filter_type': 'mine'}, name="list-mine"),
    url(r'^task/(?P<task_id>\d{1,6})$', views.view_task, name='task_detail'),
    url(r'^incomplete/$', views.view_list, {'filter_type': 'incomplete'}, name='incomplete_tasks'),
    url(r'^completed/$', views.view_list, {'view_completed': True}, name='completed_tasks'),
    url(r'^recent/added/$', views.view_list, {'filter_type': 'recent-add'}, name="recently_added"),
    url(r'^recent/completed/$', views.view_list, {'filter_type': 'recent-complete'}, name="recently_completed"),
    url(r'^admin/', admin.site.urls),
]