from django.db import models
from django.contrib.auth.admin import User

STATUS = (
    (0, "Brouillon"),
    (1, "Publier")
)


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="images/header/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return self.title


"""# Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Commenté par {self.name}, {self.body}"
"""


# Contact
class Contact(models.Model):
    name = models.CharField("Nom".upper(), max_length=100)
    email = models.EmailField("Mail".upper(), max_length=100)
    content = models.TextField("Message".upper())
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Subscribe
class Subscribe(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
