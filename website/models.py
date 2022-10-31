from django.db import models
#from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

#from tinymce import models as tinymce_models
from tinymce.models import HTMLField
#from ckeditor.fields import RichTextField


class Post(models.Model):
	title = models.CharField(max_length=255)
	category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
	#body = models.TextField('Page Content', blank=True)
	body = HTMLField('Page Content', blank=True)
	update_date = models.DateField('Last Update')
	publish = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)


	def __str__(self):
		return self.title

class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
	slug = models.SlugField()

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		unique_together = (('parent', 'slug',))
		verbose_name_plural = 'categories'

	def get_slug_list(self):
		try:
			ancestors = self.get_ancestors(include_self=True)
		except:
			ancestors = []
		else:
			ancestors = [ i.slug for i in ancestors]
			slugs = []
		for i in range(len(ancestors)):
			slugs.append('/'.join(ancestors[:i+1]))
		return slugs

	def __str__(self):
		return self.name
