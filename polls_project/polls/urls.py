from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('create/', views.create_question, name='create_question'),
    path('<int:question_id>/update/', views.update_question, name='update_question'),
    path('<int:question_id>/delete/', views.delete_question, name='delete_question'),
]
