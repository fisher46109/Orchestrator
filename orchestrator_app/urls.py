from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.ProcessView, basename='view-all')


urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('new_process', views.new_process, name='new-process'),
    path('start_process/<int:process_id>/', views.start_process, name='start-process'),
    path('stop_process/<int:process_id>/', views.stop_process, name='stop-process'),
    path('kill_process/<int:process_id>/', views.kill_process, name='kill-process'),
    path('edit_process/<int:process_id>', views.edit_process, name='edit-process'),
    path('remove_process/<int:process_id>', views.remove_process, name='remove-process'),


    path('machines_view/', views.machines_view, name='machines-view'),
    path('new_machine', views.new_machine, name='new-machine'),
    path('remove_machine/<int:machine_id>', views.remove_machine, name='remove-machine'),
    path('edit_machine/<int:machine_id>', views.edit_machine, name='edit-machine'),

    path('users_view/', views.users_view, name='users-view'),
    path('new_user', views.new_user, name='new-user'),
    path('remove_user/<int:user_id>', views.remove_user, name='remove-user'),
    path('edit_user/<int:user_id>', views.edit_user, name='edit-user'),

    path('robots_view/', views.robots_view, name='robots-view'),
    path('new_robot', views.new_robot, name='new-robot'),
    path('remove_robot/<int:robot_id>', views.remove_robot, name='remove-robot'),
    path('edit_robot/<int:robot_id>', views.edit_robot, name='edit-robot'),

    path('scheduler_view/', views.scheduler_view, name='scheduler-view'),

    path('api/', include(router.urls)),

]

