from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from site_one.models import Blog, UserProfile
from site_one.forms import BlogForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
	context = RequestContext(request)
	posts = Blog.objects.order_by('-likes')

	context_dict = {}
	context_dict['posts'] = posts

	for sub in posts:
		sub.url = en_de(sub.title, True)

	if request.session.get('last_visit'):
		last_visit_time = request.session.get('last_visit')
		visits = request.session.get('visits', 0)

		if (datetime.now() - datetime.strptime(last_visit_time[:7], "%Y-%m-%d %H:%M:%S")).days > 0:
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())
		else:
			request.session['last_visit'] = str(datetime.now())
			request.session['visits'] = 1

	return render_to_response('rose/index.html', context_dict, context)
	# return HttpResponse("Rose says Hello World!")


def blog(request, blog_title_url):
	context = RequestContext(request)
	blog_title = en_de(blog_title_url, False)
	context_dict = {'blog_title': blog_title, 'blog_title_url': blog_title_url}
	try:
		blog_body = Blog.objects.get(title=blog_title)
		context_dict['blog_body'] = blog_body
	except Blog.DoesNotExists:

		pass

	return render_to_response('rose/blog_body.html', context_dict, context)


def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = BlogForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = BlogForm()
	return render_to_response('rose/add_post.html', {'form': form}, context)


def en_de(name, value):
    if value:
        new = name.replace(' ', '_')
    else:
        new = name.replace('_', ' ')
    return new


def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = User

			if picture in request.FILES:
				profile.picture = request.Files['picture']

			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
	return render_to_response('rose/register.html', context_dict, context)
	

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/rose/')
			else:
				return HttpResponse('Your account is disabled.')
		else:
			print "Invalid login details: {0},{1}".format(username, password)
			return HttpResponse("Invalid Username or Password.")
	else:
		return render_to_response('rose/login.html',{}, context)

# def profile(request):
# 	context = RequestContext(request)


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rose/')



def about(request):
	context = RequestContext(request)
	context_dict = {'about': """This is the about page."""}

	return render_to_response('rose/about.html', context_dict, context)