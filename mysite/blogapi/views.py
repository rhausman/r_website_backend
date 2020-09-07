from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BlogPostPreviewSerializer
from .models import BlogPostPreview


class BlogPostPreviewViewSet(viewsets.ModelViewSet):
    queryset = BlogPostPreview.objects.all().order_by('title')
    serializer_class = BlogPostPreviewSerializer