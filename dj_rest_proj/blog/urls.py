from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BlogNoteListView.as_view()),
    path('category/<int:pk>/', views.BLogNoteCategoryListView.as_view()),
    path('author/<int:pk>/', views.BLogNoteAuthorListView.as_view()),
    path('blog/<int:pk>/', views.BLogNoteRetrieveView.as_view()),
    path('generate/', views.RandomGenerationView.as_view())
]
