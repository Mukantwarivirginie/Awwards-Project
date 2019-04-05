from django.contrib import admin
from .models import Profile,Project
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
admin.site.register(Profile)
admin.site.register(Project)
# admin.site.register(Follow)
# admin.site.register(Image)