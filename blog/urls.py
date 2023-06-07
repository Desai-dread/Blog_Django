from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view(), name='home'),
               path('create', views.create, name='create'),
               path('<int:pk>/', views.SoloPage.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')]