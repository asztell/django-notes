from urllib import quote_plus
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .models import Post
from .forms import PostForm


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'New post successfully created!')
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, 'Something went wrong... New post NOT created.')
    context = {
        'form':form,
        'title':'Create',
    }
    return render(request, 'post_form.html', context)


def posts_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    print instance.draft
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        'title':instance.title,
        'instance':instance,
        'share_string':share_string,
    }
    return render(request, 'post_detail.html', context)


def posts_list(request):
    queryset_list = Post.objects.active().order_by('-timestamp')
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list':queryset,
        'title':'List',
    }
    return render(request, 'post_list.html', context)


def posts_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post successfully updated!')
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, 'Something went wrong... Post NOT updated.')
    context = {
        'instance':instance,
        'form':form,
        'title': 'Update',
    }
    return render(request, 'post_form.html', context)


def posts_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    context = {
        'title':'Delete',
    }
    messages.success(request, 'Post successfully deleted!')
    return redirect('posts:list')
