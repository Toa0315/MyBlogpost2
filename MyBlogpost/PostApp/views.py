from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def homepage(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, "homepage.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent__isnull=True)  # Show only parent comments
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_id = request.POST.get("parent_id")
            comment = comment_form.save(commit=False)
            comment.post = post

            if parent_id:  # If it's a reply
                comment.parent = Comment.objects.get(id=parent_id)

            comment.save()
            return redirect(post.get_absolute_url())  # Refresh page after comment

        elif "like_submit" in request.POST:
            if request.user.is_authenticated:
                if post.likes.filter(id=request.user.id).exists():
                    post.likes.remove(request.user)  # Unlike if already liked
                else:
                    post.likes.add(request.user)  # Like the post
            return redirect(post.get_absolute_url())

    return render(request, "detail.html", {
        "post": post,
        "comments": comments,
        "commentform": comment_form,
        "total_likes": post.total_likes(),
        "liked": post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    })
