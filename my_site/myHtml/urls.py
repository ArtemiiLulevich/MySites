from django.urls import path

from . import views

app_name = 'myHtml'

urlpatterns = [

    # path('', views.post_list, name='post_list'),
    path('', views.start, name='post_list'),

]
