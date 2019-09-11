from django.urls import path, include
from . import views

app_name = 'todos'
# handler404 = 'todos.views.page_not_found_view'
# handler505 = 'todos.views.page_not_found_view'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    # path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]

