from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_notes, name='home'),
    path('blog/<int:id>/', views.blog_note, name='note'),
    path('category/<int:cat_id>/', views.category_notes, name='category'),
    path('user_notes/<int:user_id>/', views.user_notes, name='user_notes'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('my_blogs/', views.current_user_notes, name='my_blogs'),
]
