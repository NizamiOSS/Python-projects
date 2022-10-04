from django.shortcuts import render, redirect

from .models import Title, Post
from .forms import TitleForm, PostForm

# Create your views here.
def index(request):
	return render(request, 'blogs/index.html')

def titles(request):
	titles = Title.objects.order_by('date_added')
	context = {'titles':titles}
	return render(request, 'blogs/titles.html', context)

def title(request, title_id):
	"""Show a single title and  its post."""
	title = Title.objects.get(id=title_id)
	posts = title.post_set.order_by('-date_added')
	context = {'title':title, 'posts':posts}
	return render(request, 'blogs/title.html', context)

def new_title(request):
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TitleForm
	else:
		# POST data submitted; process data.
		form = TitleForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:titles')

	#Display a blank or invalid form.
	context = {'form':form}
	return render(request, 'blogs/new_title.html', context)

def new_post(request, title_id):
	"""Add a new entry for a particular title."""
	title = Title.objects.get(id=title_id)

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = PostForm()
	else:
		# POST data submitted; process data.
		form = PostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.title = title
			new_post.save()
			return redirect('blogs:title', title_id=title_id)

	# Display a blank or invalid form.
	context = {'title':title, 'form':form}
	return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
	"""Edit an existing post."""
	post = Post.objects.get(id=post_id)
	title = post.title

	if request.method != 'POST':
		#Initial request; pre-fill form with the current post.
		form = PostForm(instance=post)
	else:
		# POST data submitted; process data.
		form = PostForm(instance=post,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:title', title_id=title.id)

	context = {'post': post, 'title': title, 'form': form}
	return render(request, 'blogs/edit_post.html', context)
