# from django.shortcuts import render


from rest_framework import viewsets, status
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.decorators import api_view
# Create your views here.
from functools import wraps


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['PUT', "GET"])
def vote(request, id):
    # print(request)

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        # print(id)
        # print(request.data)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404_NOT_FOUND)


def check_GET_Request(func):
    @wraps(func)
    def wrapper(request):

        return (func(request)) if request.method == "GET" else Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return wrapper


@api_view(['GET'])
@check_GET_Request
def boasts(request):

    posts = Post.objects.filter(message_type="B")
    serializer = PostSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@check_GET_Request
def roasts(request):

    posts = Post.objects.filter(message_type="R")
    serializer = PostSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@check_GET_Request
def top_posts(request):

    post = [p for p in Post.objects.all()]

    post = sorted(post, key=lambda x: x.vote_total(), reverse=True)

    serializer = PostSerializer(post, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_message(request):
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            message = serializer.validated_data.get("message")
            message_type = serializer.validated_data.get("message_type")
            Post.objects.create(message=message, message_type=message_type)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
