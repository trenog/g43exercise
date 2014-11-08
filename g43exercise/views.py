from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext, loader

from g43exercise.models import Article

# Create your views here.

#class IndexView(generic.ListView):
#	template_name = 'g43exercise/index.html'
#	context_object_name = 'news_articles'
all_articles = Article.objects.filter(
				pub_date__lte=timezone.now()
				).order_by('-pub_date')[:5]

def index(request):
	# List Page that enumerates all articles contained on the site
	context = {'all_articles':all_articles}
	return render(request, 'g43exercise/index.html', context)
def detail(request, article_id):
	# Detail page that displays all the contents of a particular article
	article = get_object_or_404(Article, pk=article_id)
	context = {'all_articles': all_articles, 'article': article}
	return render(request, 'g43exercise/article.html', context)	
	
