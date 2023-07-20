from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from .forms import CommentsForm


def forum_index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'forum_index.html', context)


def forum_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return redirect('forum_detail', pk=post.pk)
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'forum_detail.html', context)


def forum_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'forum_category.html', context)


def search_results(request):
    query = request.GET.get('query')
    results = Post.objects.filter(title__contains=query)
    context = {'results': results}
    return render(request, 'search_results.html', context)

