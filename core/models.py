from io import BytesIO

from django.db import models
from django.core.files import File
from PIL import Image


class Allergen(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Item(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    allergen = models.ManyToManyField(Allergen, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    food_energy = models.IntegerField()
    description = models.CharField(max_length=255, null=False, blank=True, default='Tasty meal')

    def __str__(self):
        return str(self.name)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url

            else:
                return "https://https://placehold.co/240x240"

    def make_thumbnail(self, image, size=(240, 240)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_allergen_list(self):
        if self.allergen:

            allergen_list = Allergen.objects.filter(item__id=self.id)

            return allergen_list
        else: return None

    def get_price(self):
        return self.price / 100
