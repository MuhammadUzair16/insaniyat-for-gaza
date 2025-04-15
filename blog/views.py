from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, Comment
from .forms import CommentForm


def blog_list(request):
    posts_list = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 6)  # 6 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blogs/blog_list.html', {'page_obj': page_obj})


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, 'blogs/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })