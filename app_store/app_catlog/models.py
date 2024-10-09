# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator 
# from django.urls import reverse
# from django.utils.text import slugify

# class App(models.Model):
#     name = models.CharField(max_length=500)
#     rating = models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(5)]
#     )
#     developer = models.CharField(null=True, max_length=100)
#     is_bestselling = models.BooleanField(default=False)
#     slug = models.SlugField(default="", null=False, unique=True)


#     def get_absolute_url(self):
#         return reverse("app_detail", args=[self.id])
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
    

#     # Indent the __str__ method to be part of the class
#     def __str__(self):
#         return f"{self.name} ({self.rating})"


from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class App(models.Model):
    name = models.CharField(max_length=500)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    developer = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, unique=True,editable=False, blank=True)  # Removed default=""

    def get_absolute_url(self):
        return reverse("app_detail", args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if App.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{self.id}"  # Ensure unique slug if there's a duplicate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.rating})"

