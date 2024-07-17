from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)

class Curses(models.Model):
    title_curs = models.CharField(max_length=200)
    description_curs = models.TextField()
    created_by_curs = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_curs

class Lessons(models.Model):
    course_lesson = models.ForeignKey(Curses, related_name='lessons', on_delete=models.CASCADE)
    title_lesson = models.CharField(max_length=200)
    lesson_video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])
    ],null=True, blank=True)
    description_for_lesson = models.TextField()
    created_at_lesson = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_lesson

class Comments(models.Model):
    lesson_comment = models.ForeignKey(Lessons, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_comment = models.TextField()
    created_at_comment = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bu odam {self.author} bu mavzuga {self.lesson_comment.title_lesson} comment yozdi"

class Likes(models.Model):
    lesson_like = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_like = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bu odam {self.author} bu mavzuga {self.lesson_like} qoydi"