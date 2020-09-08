# serializers.py
from rest_framework import serializers

from .models import BlogPostPreview

class BlogPostPreviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPostPreview
        fields = ('id','title', 'md_file_path', 'preview_img_path', 'description', 'md_file', 'md_text')