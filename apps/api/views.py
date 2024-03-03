from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.views import (
    APIView,
    Request,
    Response
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from apps.api.models import User, Product, Category, Article
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ArticleSerializer

# Создайте ViewSet, который позволяет получить список всех пользователей из базы данных.
# Пользователи должны иметь возможность получить список всех пользователей в формате JSON,
# используя метод GET.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Создайте APIView, которое позволяет получить список всех товаров из базы данных.
# Пользователи должны иметь возможность получить список всех товаров в формате JSON, используя метод GET.


class ProductsApiView(APIView):

    def get(self, request: Request):
        products = Product.objects.filter(
            creator=request.user.id
        )

        if products:
            serializer = ProductSerializer(
                instance=products,
                many=True
            )

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request: Request):
        try:
            serializer = ProductSerializer(
                data=request.data
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        except ValidationError as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "error": str(error),
                    "detail": error.detail
                }
            )

# Создайте функцию с декоратором @api_view(['GET']), которая позволяет получить список всех категорий из базы данных.
# Пользователи должны иметь возможность получить список всех категорий в формате JSON, используя метод GET.


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()

    if categories:
        serializer = CategorySerializer(
            instance=categories,
            many=True
        )

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    return Response(
        status=status.HTTP_204_NO_CONTENT,
        data=[]
    )

# Создайте GenericAPIView с использованием RetrieveUpdateDestroyAPIView, которое позволяет просматривать информацию
# об отдельной статье по её уникальному идентификатору (ID). Пользователи должны иметь возможность получить информацию
# о статье в формате JSON, используя метод GET, обновить данные статьи, используя метод PUT или PATCH,
# и удалить статью, используя метод DELETE.


class ArticleGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


