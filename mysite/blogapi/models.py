from django.db import models

# Create your models here.

class BlogPostPreview(models.Model):
    title = models.CharField(max_length=60)
    #id = models.CharField(max_length=60)
    md_file_path = models.CharField(max_length=60) # Path to the .md file of the blog post
    preview_img_path = models.CharField(max_length=60)

    def __str__(self):
        return self.title