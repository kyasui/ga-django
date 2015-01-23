import random
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):

	posts = Post.objects.all().filter(published_date__isnull=False)

	return render(request, 'blog/post_list.html', {
		'posts': posts
	})