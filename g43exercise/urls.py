from django.conf.urls import patterns, url
from g43exercise import views
from django.conf.urls.static import static
from django.conf import settings

# Create your urls patterns here.
urlpatterns = patterns('',
	# ex: /article/
	url(r'^$', views.index, name='index'),
	#
	url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
	# 
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}, name='media'),
	#
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
	}),
)