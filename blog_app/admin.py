from django.contrib import admin
from .models import Post, Comment



@admin.action(description='Delete content from selected posts')
def del_content(modeladmin, request, queryset):
    queryset.update(content='')


@admin.action(description='Set title to uppercase for selected posts')
def set_title_uppercase(modeladmin, request, queryset):
    for post in queryset:
        post.title = post.title.upper()
        post.save()


@admin.action(description='Set title to capitalized for selected posts')
def set_title_capitalized(modeladmin, request, queryset):
    for post in queryset:
        post.title = post.title.capitalize()
        post.save()


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'len_content', 'created_at', 'author', 'is_popular')
    # list_editable = ('author', )
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    inlines = [CommentInline]
    actions = [del_content, set_title_uppercase, set_title_capitalized]

    def is_popular(self, obj):
        return obj.comments.count() > 5
    
    is_popular.boolean = True
    is_popular.short_description = 'Is Popular'

    def short_content(self, obj):
        if len(obj.content) > 40:
            return obj.content[:40] + '...'
        else:
            return obj.content
        
    short_content.short_description = 'Content'

    def len_content(self, obj):
        return len(obj.content)

    len_content.short_description = 'Length'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'post')
    list_filter = ('author', 'post', 'created_at')
    search_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)