from django.urls import path
from . import views


urlpatterns = [
    path('', views.current_todos, name="todos"),
    # path('<int:todo_id>/', views.todo_detail, name="tododetail"),


    # Todos (постановка задач)
    path('current/', views.current_todos, name='currenttodos'),
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='createtodo'),
    path('todo/<int:todo_pk>', views.view_todo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='completetodo'),
    path('todo/completed', views.completed_todos, name='completedtodos'),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name='deletetodo'),
    path('trash/', views.trash_bin, name='trashbin' ),
    path('todo/<int:todo_pk>/softdelete', views.soft_delete_todo, name='softdeletetodo'),
    path('todo/<int:todo_pk>/restore', views.restore_todo, name='restoretodo'),

]

