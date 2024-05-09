from django.urls import path
from todo import views


urlpatterns = [
    path('', views.TodosAPIView.as_view()),
    path('<int:id>/', views.TodoAPIView.as_view()),
    path('done/', views.DoneTodosAPIView.as_view()),
    path('done/<int:id>/', views.DoneTodoAPIView.as_view()),
]