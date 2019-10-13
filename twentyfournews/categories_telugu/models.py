from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.db.models.signals import pre_save


class Categories_telugu(models.Model):
    category = models.CharField(max_length=50)
    home_Page_Order_1_to_5 = models.IntegerField(null=True, blank=True)
    Enable = models.BooleanField(default=False)

    class Meta:
        db_table = "categories_telugu"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category + ' (' + str(self.home_Page_Order_1_to_5) + ')'


class News_telugu(models.Model):
    Categories = models.ForeignKey(Categories_telugu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    telugu_title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    video = models.CharField(null=True, max_length=500)
    description = RichTextField()
    Popular_News = models.BooleanField(default=False)
    Banner_News = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "news_telugu"
        verbose_name = "news"
        verbose_name_plural = "news"

    def __str__(self):
        return self.Categories.category + ' > ' + self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        from twentyfournews.util import unique_slug_generator
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=News_telugu)


class Images_telugu(models.Model):
    Categories = models.ForeignKey(Categories_telugu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "images_telugu"
        verbose_name = "images"
        verbose_name_plural = "images"

    def __str__(self):
        return self.title


class Videos_telugu(models.Model):
    Categories = models.ForeignKey(Categories_telugu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=200)

    class Meta:
        db_table = "videos_telugu"
        verbose_name = "videos"
        verbose_name_plural = "videos"

    def __str__(self):
        return self.title


class Reviews_telugu(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    RATING = [
        ('1', '1'),
        ('1.25', '1.25'),
        ('1.5', '1.5'),
        ('1.75', '1.75'),
        ('2', '2'),
        ('2.25', '2.25'),
        ('2.5', '2.5'),
        ('2.75', '2.75'),
        ('3', '3'),
        ('3.25', '3.25'),
        ('3.5', '3.5'),
        ('3.75', '3.75'),
        ('4', '4'),
        ('4.25', '4.25'),
        ('4.5', '4.5'),
        ('4.75', '4.75'),
        ('5', '5'),
    ]
    rating = models.CharField(
        max_length=5,
        choices=RATING,
        default='',
    )

    class Meta:
        db_table = "reviews_telugu"
        verbose_name = "reviews"
        verbose_name_plural = "reviews"

    def __str__(self):
        return self.name


class Cms_telugu(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()

    class Meta:
        db_table = "cms_telugu"
        verbose_name = "cms"
        verbose_name_plural = "cms"

    def __str__(self):
        return self.title


class Contacted_telugu(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = RichTextField()

    class Meta:
        db_table = "contacted_telugu"
        verbose_name = "contacted"
        verbose_name_plural = "contacted"

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Email: ' + str(self.email) + ', Message: ' + str(self.message)
