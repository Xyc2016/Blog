from django.urls import path

from . import views

urlpatterns = [
    path('blog_backend', views.blog_backend, name='blog_backend'),
    path('write_article', views.write_article, name='write_article'),
    path('article_management', views.article_management, name='article_management'),
    path('article_delete/<int:id>', views.article_delete, name='article_delete'),
    path('add_friend_link', views.add_friend_link, name='add_friend_link'),
    path('friend_link_management', views.friend_link_management, name='friend_link_management'),
    path('friend_link_delete/<int:id>', views.friend_link_delete, name='friend_link_delete'),
    path('message_delete/<int:id>', views.message_delete, name='message_delete'),
    path('message_management', views.message_management, name='message_management'),
    path('', views.index, name='index'),
    path('article_detail/<int:id>', views.article_detail, name='article_detail'),
    path('article', views.article, name='article'),
    path('messages', views.messages, name='messages'),
    path('add_message', views.add_message, name='add_message'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('add_comment/<int:article_id>', views.add_comment, name='add_comment'),
    path('friend_links', views.friend_links, name='friend_links'),
    path('show_photos',views.show_photos,name='show_photos'),
    path('upload_photo',views.upload_photo,name='upload_photo'),
]
