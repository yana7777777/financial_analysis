from django.urls import path
from todo import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('ability/', views.ability, name='ability'),
    # Auth (регистрация и авторицзация) добавила 20.07.25
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

]