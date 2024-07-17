from django.conf import settings
from django.core.mail import send_mail

from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User, Curses, Lessons, Comments, Likes
from .permissions import Permissions
from .serializers import UserSerializer, CursesSerializer, LessonsSerializer, CommentsSerializer, LikesSerializer, EmailSerializer

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CursesViewSet(viewsets.ModelViewSet):
    queryset = Curses.objects.all()
    serializer_class = CursesSerializer
    permission_classes = [Permissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title_curs", "description_curs"]


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [Permissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["course_lesson__title_curs", "title_lesson", "description_for_lesson", "lesson_video"]


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [Permissions]

class LikesView(APIView):
    def get(self, request, pk):
        like = len(Likes.objects.filter(like_or_dislike=True, video_id=pk))
        dislike = len(Likes.objects.filter(like_or_dislike=False, video_id=pk))
        return Response({"like":like, "dislike":dislike})


class CreateLikesView(APIView):
    def post(self, request):
        try:
            like_dislike = Likes.objects.filter(author_id=request.data.get("author"))
            for like in like_dislike:
                like.delete()
        except:
            pass
        serializer = Likes(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(Likes(like_or_dislike).data)


class SendMassageMailView(APIView):
    def post(self,request: Request):

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_user = []
        for user in users:
            if user.email != '':
                email_user.append(user.email)

    
        subject = serializer.validated_data.get('subject')
        message = serializer.validated_data.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_user
        fail_silently = False
        send_mail( subject, message, email_from, recipient_list, fail_silently )
        return Response({'massage':'success'})
    