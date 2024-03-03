from rest_framework import serializers
from apps.product.models import Product, Rating, Comment
from apps.api.models import User, Article, Category


# Напишите ModelSerializer для всех трёх моделей.
# Далее, создайте отдельный Serializer для получения рейтинга товара с его комментариями.
# В этом Serializer реализуйте метод, который позволит пользователю ввести идентификатор товара,
# а затем вернет его рейтинг и список всех комментариев, связанных с этим товаром.


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductRatingCommentSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product does not exist.")
        return value

    def get_product_rating_and_comments(self, validated_data):
        product_id = validated_data['product_id']
        product = Product.objects.get(id=product_id)
        ratings = Rating.objects.filter(product=product)
        comments = Comment.objects.filter(product=product)
        rating_serializer = RatingSerializer(ratings, many=True)
        comment_serializer = CommentSerializer(comments, many=True)
        return {
            'product': ProductSerializer(product).data,
            'ratings': rating_serializer.data,
            'comments': comment_serializer.data
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']