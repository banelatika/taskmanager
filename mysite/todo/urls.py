from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign_in, name='signup'),
    path('login/', views.login_form, name='login'),
    path('logied/', views.profile_userlog, name='logied'),
    path('profile/', views.profile_user, name='profile'),
    path('logout/', views.log_out, name='logout'),
    path('raccept/<my_user>', views.request_accepts, name='requestaccept'),
    path('tasks/', views.Task_User, name='tasks'),
    path('tasksboard/', views.task_board, name='tasksboard'),
    path('editask/<int:id>', views.task_edit, name='editask'),
    path('delete/<int:id>', views.delete_date, name="deletedata"),
    path('taskcompleted/<int:id>', views.task_completed, name="taskcompleted"),
]