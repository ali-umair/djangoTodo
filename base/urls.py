from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>', views.DetailList.as_view(), name='detaillist'),
    path('create', views.TaskCreate.as_view(), name='create')
]
