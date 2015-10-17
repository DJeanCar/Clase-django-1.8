from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Movie(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField()
	synopsis = models.TextField()
	image = models.ImageField(upload_to = 'movies')

	def __unicode__(self): # python 3.x: __str__
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Movie, self).save(*args, **kwargs)