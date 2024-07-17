from django.contrib import admin
from .models import User, Curses, Lessons, Likes, Comments

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email', 'phone_number']
    list_display_links = ['pk', 'username']

@admin.register(Curses)
class CurseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title_curs']
    list_editable = ['title_curs']
    list_display_links = ['pk']

@admin.register(Lessons)
class Lesson(admin.ModelAdmin):
    list_display = ['pk', 'course_lesson', 'title_lesson', 'description_for_lesson', 'created_at_lesson']
    list_editable = ['description_for_lesson']
    list_display_links = ['pk', 'title_lesson']

@admin.register(Comments)
class Comment(admin.ModelAdmin):
    list_display = ['pk', 'lesson_comment', 'author', 'content_comment']
    list_editable = ['content_comment']
    list_display_links = ['pk', 'lesson_comment']

@admin.register(Likes)
class Like(admin.ModelAdmin):
    list_display = ['pk', 'lesson_like', 'like_or_dislike', 'author', 'created_like']
    list_display_links = ['pk', 'author']
