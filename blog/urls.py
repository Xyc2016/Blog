from django.urls import path

from . import views

urlpatterns = [
    path('blog_backend', views.blog_backend, name='blog_backend'),
    path('write_article', views.write_article, name='write_article'),
    path('article_management', views.article_management, name='article_management'),
    path('article_delete/<int:article_id>', views.article_delete, name='article_delete'),
    path('add_friend_link', views.add_friend_link, name='add_friend_link'),
    path('friend_link_management', views.friend_link_management, name='friend_link_management'),
    path('friend_link_delete/<int:friend_link_id>', views.friend_link_delete, name='friend_link_delete'),
    path('message_delete/<int:message_id>', views.message_delete, name='message_delete'),
    path('message_management', views.message_management, name='message_management'),
    path('', views.index, name='index'),
    path('article_detail/<int:article_id>', views.article_detail, name='article_detail'),
    path('article', views.articles, name='article'),
    path('messages', views.messages, name='messages'),
    path('add_message', views.add_message, name='add_message'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('add_comment/<int:article_id>', views.add_comment, name='add_comment'),
    path('friend_links', views.friend_links, name='friend_links'),
    path('show_photos', views.show_photos, name='show_photos'),
    path('upload_photo', views.upload_photo, name='upload_photo'),
    path('photo_detail/<str:photo_name>', views.photo_detail, name='photo_detail'),
    path('add_photo_comment/<str:photo_name>', views.add_photo_comment, name='add_photo_comment'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('personal_info_management', views.personal_info_management, name='personal_info_management')

]
