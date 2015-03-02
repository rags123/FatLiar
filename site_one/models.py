from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
# Create your models here.


class Blog(models.Model):
	title = models.CharField(max_length=120, unique=True)
	# slug = models.SlugField(max_length=100, unique=True)
	content = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	

	def __unicode__(self):
		return "%s" % self.title

	# @permalink
	# def get_absolute_url(self):
	# 	return ('view_blog_post', None, {'slug': self.slug})

# class BlogContent(models.Model):
# 	heading = models.ForeignKey(BlogPost)
# 	image = models.ImageField(upload_to='blog_images', blank=True)
# 	url = models.URLField(blank=True)
# 	date = models.DateField(auto_now_add=True)
	

# 	def __unicode__(self):
# 		return self.date


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='blog_images', blank=True)

	def __unicode__(self):
		return self.user.username