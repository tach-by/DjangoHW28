from rest_framework import serializers
from apps.product.models import Product, Rating, Comment


# Напишите ModelSerializer для всех трёх моделей.
# Далее, создайте отдельный Serializer для получения рейтинга товара с его комментариями.
# В этом Serializer реализуйте метод, который позволит пользователю ввести идентификатор товара,
# а затем вернет его рейтинг и список всех комментариев, связанных с этим товаром.