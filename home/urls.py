from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('add_friend_page',views.add_friend_page,name='add_friend_page'),
    path('view_friends',views.view_friends,name='view_friends'),
    path('edit_friend/<int:pk>/edit',views.edit_friend,name='edit_friend'),
    path('delete_friend/<int:pk>/delete',views.delete_friend,name='delete_friend'),
    path('friend_cell',views.friend_cell,name='friend_cell'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('login',views.login,name='login'),
    path('add_gallery',views.add_gallery,name='add_gallery'),
    path('view_gallery',views.view_gallery,name='view_gallery'),
    path('gallery',views.gallery,name='gallery'),
    path('delete_image/<int:pk>/',views.delete_image,name='delete_image'),
]
