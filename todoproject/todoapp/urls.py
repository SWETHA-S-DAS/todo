from django.conf.urls.static import static
from django.urls import path, include

from todoproject import settings
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('listview', views.TaskListView.as_view(),name='listview'),
    path('detailview/<int:pk>/', views.TaskDetailView.as_view(), name='detailview'),
    path('updateview/<int:pk>/',views.TaskUpdateView.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDeleteView.as_view(),name='deleteview')
]
