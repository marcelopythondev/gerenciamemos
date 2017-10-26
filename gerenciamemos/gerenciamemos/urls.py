from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('memos.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
]