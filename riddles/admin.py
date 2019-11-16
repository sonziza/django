from django.contrib import admin
from .models import Option, Riddle
# Register your models here.

#admin.site.register(Riddle)
#admin.site.register(Option)

@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    list_display = ('riddle_text', 'pub_date')
    date_hierarchy = 'pub_date'




@admin.register(Option)
class PostOption(admin.ModelAdmin):
    list_display = ('riddle', 'text', 'correct')
    # подбор автора по списку
    raw_id_fields = ('riddle',)
    # автоподбор поля slug по полю title
    #prepopulated_fields = {'riddle': ('riddle_text',)}