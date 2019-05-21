from django.shortcuts import render, get_object_or_404
from .models import Article, FriendLink, Message, ArticleComment, PhotoComment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import os
from .forms import UploadFileForm


# Create your views here.
@login_required
def blog_backend(request):
    return render(request, 'blog_backend.html')


@login_required
def write_article(request):
    if request.method == 'GET':
        return render(request, 'write_article.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
    return HttpResponseRedirect(reverse('blog_backend', args=()))


@login_required
def article_management(request):
    article_list = Article.objects.all()
    return render(request, 'article_management.html', {
        'article_list': article_list
    })


@login_required
def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse('article_management', args=()))


@login_required
def friend_link_management(request):
    friend_link_list = FriendLink.objects.all()
    return render(request, 'friend_link_management.html', {
        'friend_link_list': friend_link_list
    })


@login_required
def friend_link_delete(request, friend_link_id):
    friend_link = FriendLink.objects.get(pk=friend_link_id)
    friend_link.delete()
    return HttpResponseRedirect(reverse('friend_link_management', args=()))


@login_required
def add_friend_link(request):
    friend_link = request.POST['friend_link']
    friend_link = FriendLink(link=friend_link)
    friend_link.save()
    return HttpResponseRedirect(reverse('friend_link_management', args=()))


@login_required
def message_management(request):
    return render(request, 'message_management.html', {
        'message_list': Message.objects.all()
    })


@login_required
def message_delete(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    return HttpResponseRedirect(reverse('message_management', args=()))


def index(request):
    return render(request, 'blog_index.html', {})


def articles(request):
    return render(request, 'article.html', {
        'article_list': Article.objects.all()
    })


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article_detail.html', {
        'article': article
    })


def messages(request):
    return render(request, 'messages.html', {
        'message_list': Message.objects.all()
    })


@login_required
def add_message(request):
    content = request.POST['content']
    author = request.POST['author']
    message = Message(content=content, author=author)
    message.save()
    return HttpResponseRedirect(reverse('messages', args=()))


def log_in(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('blog_backend', args=()))
        return HttpResponseRedirect(reverse('log_in', args=()))
    return render(request, 'log_in.html', {})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index', args=()))


def add_comment(request, article_id):
    content = request.POST['content']
    author = request.POST['author']
    article_comment = ArticleComment(content=content, author=author)
    article1 = Article.objects.get(pk=article_id)
    article_comment.article = article1
    article_comment.save()
    return HttpResponseRedirect(reverse('article_detail', args=(article_id,)))


def friend_links(request):
    friend_link_list = FriendLink.objects.all()
    return render(request, 'friend_links.html', {
        'friend_link_list': friend_link_list
    })


def show_photos(request):
    # os.chdir('static/photos')
    # for name in os.listdir():
    #     print(name)
    return render(request, 'photos.html', {
        'photo_name_list': os.listdir('static/photos')
    })

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            with open('static/photos/' + request.POST['title'], 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    print(1)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'upload_photo.html', {
        'form': form
    })


def photo_detail(request, photo_name):
    photo_comment_list = PhotoComment.objects.filter(photo_name=photo_name).all()
    print(photo_comment_list)
    return render(request, 'photo_detail.html', {
        'photo_name': photo_name,
        'photo_comment_list': photo_comment_list,
    })


def add_photo_comment(request, photo_name):
    photo_comment = PhotoComment()
    photo_comment.photo_name = photo_name

    photo_comment.content = request.POST['content']
    photo_comment.author = request.POST['author']
    photo_comment.save()
    return HttpResponseRedirect(reverse('show_photos', args=()))


personal_information = {
    'name': '徐玉才',
    'age': '22',
    'gender': '男',
    'school': '烟台大学',
}


def personal_info(request):
    return render(request, 'personal_info.html', personal_information)

@login_required
def personal_info_management(request):
    if request.method == 'GET':
        return render(request, 'personal_info_management.html', personal_information)
    else:
        personal_information['name'] = request.POST['name']
        personal_information['age'] = request.POST['age']
        personal_information['gender'] = request.POST['gender']
        personal_information['school'] = request.POST['school']
        return HttpResponseRedirect(reverse('personal_info_management', args=()))
