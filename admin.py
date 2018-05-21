from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display=['__str__','timestamp','updated','id']
	list_display_links=['updated','timestamp']
	list_filter=['updated']
	#list_editable=['title','content']
	search_fields=['title','content']
	class Meta:
		model=Post

admin.site.register(Post,PostModelAdmin)