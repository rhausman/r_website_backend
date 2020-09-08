from django.db import models

# Create your models here.

class BlogPostPreview(models.Model):
    title = models.CharField(max_length=60)
    #id = models.CharField(max_length=60)
    md_file_path = models.CharField(max_length=1000) # Path to the .md file of the blog post
    preview_img_path = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    md_file = models.FileField(upload_to='blog_markdowns', max_length=1000)
    md_text = models.TextField()

    def __str__(self):
        return self.title