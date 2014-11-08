from django.template import Library, Node
from g43exercise.models import Article 

import random

register = Library()

@register.assignment_tag
def get_random_article():
	random_index = random.randint(0, Article.objects.count()-1)
	random_article = Article.objects.all()[random_index]
	return random_article

@register.assignment_tag
def get_random_article_list():
	r1 = random.randint(0, Article.objects.count()-1)
	r2 = random.randint(0, Article.objects.count()-1)
	r3 = random.randint(0, Article.objects.count()-1)
	r4 = random.randint(0, Article.objects.count()-1)
	r1a = Article.objects.all()[r1]
	r2a = Article.objects.all()[r2]
	r3a = Article.objects.all()[r3]
	r4a = Article.objects.all()[r4]
	return r1a,r2a,r3a,r4a	
