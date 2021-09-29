from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>', views.DetailList.as_view(), name='detaillist'),
]
