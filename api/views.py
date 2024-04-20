from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer


class LoginView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("Welcome!", status=status.HTTP_200_OK, content_type='text/plain')
        else:
            return Response("Invalid credentials.", status=status.HTTP_401_UNAUTHORIZED, content_type='text/plain')


class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response("Goodbye!", status=status.HTTP_200_OK, content_type='text/plain')
        except Exception as e:
            return Response(f"Logout failed: {str(e)}", status=status.HTTP_400_BAD_REQUEST, content_type='text/plain')

class StoryView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            serializer = StorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unauthenticated author.", status=status.HTTP_503_SERVICE_UNAVAILABLE, content_type='text/plain')

    def get(self, request):
        story_cat = request.GET.get('story_cat', '*')
        story_region = request.GET.get('story_region', '*')
        story_date = request.GET.get('story_date', '*')

        stories = Story.objects.all()

        if story_cat != '*':
            stories = stories.filter(category=story_cat)
        if story_region != '*':
            stories = stories.filter(region=story_region)
        if story_date != '*':
            stories = stories.filter(date__gte=story_date)

        serializer = StorySerializer(stories, many=True)
        if serializer.data:
            return Response({"stories": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response("No stories found.", status=status.HTTP_404_NOT_FOUND, content_type='text/plain')


class DeleteStoryView(APIView):
    def delete(self, request, key):
        if request.user.is_authenticated:
            try:
                story = Story.objects.get(id=key, author=request.user)
                story.delete()
                return Response(status=status.HTTP_200_OK)
            except Story.DoesNotExist:
                return Response("Story not found.", status=status.HTTP_503_SERVICE_UNAVAILABLE, content_type='text/plain')
        else:
            return Response("Unauthenticated author.", status=status.HTTP_503_SERVICE_UNAVAILABLE, content_type='text/plain')
