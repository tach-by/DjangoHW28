from django.db import models


# Создайте модели Product, Rating и Comment,
# где Product будет иметь отношение "один-ко-многим" к Rating и Comment.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(
        Product,
        related_name='ratings',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return self.rating


class Comment(models.Model):
    name = models.CharField(max_length=400)
    product = models.ForeignKey(
        Product,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
