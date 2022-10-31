from django.shortcuts import render
#from django.views.generic import ListView

from . models import Post
from . models import Category

'''
# pro navigaci a na vyzkoušení použijem třídy
class NavbarView(ListView):
	model = Category
	template_name = 'navigace.html'
'''





def home(request):
	parents = Category.objects.filter(parent=None)

	context = {
		'parents': parents,
	}
	return render(request, 'home.html', context)



def navbar(request):
	parents = Category.objects.filter(parent=None)

	context = {
		'article_list': Post.objects.all(),
		'parents': parents,
	}

	return render(request, 'navigace.html', context)


def index(request, pagename):
	pagename = pagename
	pg = Post.objects.get(slug=pagename)
	parents = Category.objects.filter(parent=None)

	context = {
		'title': pg.title,
		'content': pg.body,
		'slug': pg.slug,
		'article_list': Post.objects.all(),
		'parents': parents,
	}


	#assert False
	return render(request, 'article.html', context)

