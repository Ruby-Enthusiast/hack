from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm

def comments_list_and_add(request, code):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.code = code
            comment.save()
            return redirect('comments_list_and_add', code=code)
    else:
        form = CommentForm()

    comments = Comment.objects.filter(code=code)
    return render(request, 'comments_list.html', {'code': code, 'comments': comments, 'form': form})

def delete_comment(request, code, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == comment.password:
            comment.delete()
            return redirect('comments_list_and_add', code=code)

    return render(request, 'delete_comment.html', {'comment': comment, 'code': code})

