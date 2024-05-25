from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Comment by {self.author_name} on {self.post.title}'