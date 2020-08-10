from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = Post.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)

class Port_Project(models.Model):
	title = models.CharField(max_length=100)
	video = models.URLField()
	description = models.TextField()

	def __str__(self):
		return self.title

class Technologies(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Portfolio(models.Model):
	name = models.CharField(max_length=100)
	project = models.ManyToManyField(Port_Project, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.name)

			has_slug = Portfolio.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.name) + '-' + str(count) 
				has_slug = Portfolio.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)



class SkillCat(models.Model):
	title = models.CharField(max_length=100)
	skills = models.ManyToManyField(Technologies)

	def __str__(self):
		return self.title


class EmailList(models.Model):
    email = models.EmailField()

    def __str__(self):
    	return self.email