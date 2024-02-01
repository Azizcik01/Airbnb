from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.models import Product, Category, Product_Images
from .helper import No_method
from .serializer import Category_Serializer, Product_Serializer, Images_Serializer

class CategoryView(GenericAPIView, No_method):
    permission_classes = AllowAny,
    serializer_class = Category_Serializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Category.objects.filter(pk=pk).first().format())
            except:
                return Response({"error":"Bunday Category mavjud emas"})
        ctgs = Category.objects.all().order_by('-id')
        return Response([x.format() for x in ctgs])
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        ctg = serializer.save()
        return Response(ctg.format())
    
    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Category.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "Bunday Category mavjud emas"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result.format())
    
    def delete(self, request, pk, ):
        try:
            Category.objects.get(pk=pk).delete()
            return Response({"result": "Muvaffaqqiyatli o'chirildi!"})
        except:
            return Response({"error": "Bunday post mavjud emas!"})


class ProductView(GenericAPIView, No_method):
    permission_classes = AllowAny,
    serializer_class = Product_Serializer

    def get(self, request, pk:None, *args, **kwargs):
        if pk:
            try:
                return Response(Product.objects.filter(pk=pk).first().format())
            except:
                return Response({"error":"Bunday Product mavjud emas"})
        ctgs = Product.objects.all().order_by('-pk')
        return Response([x.format() for x in ctgs])
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response(post.format())
    
    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Product.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "Bunday Product mavjud emas"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result.format())
    
    def delete(self, request, pk, ):
        try:
            Product.objects.get(pk=pk).delete()
            return Response({"result": "Muvaffaqqiyatli o'chirildi!"})
        except:
            return Response({"error": "Bunday post mavjud emas!"})


class Post_ImagesView(GenericAPIView, No_method):
    permission_classes = AllowAny,
    serializer_class = Images_Serializer

    def get(self, request, pk:None, *args, **kwargs):
        if pk:
            try:
                return Response(Product_Images.objects.filter(product_pk=pk).first().format())
            except:
                return Response({"error":"Rasm mavjud emas"})
        ctgs = Product_Images.objects.all().order_by('-pk')
        return Response([x.format() for x in ctgs])
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response(post.format())
    
    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Product_Images.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "Bunday rasm mavjud emas"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result.format())
    
    def delete(self, request, pk, ):
        try:
            Product_Images.objects.get(pk=pk).delete()
            return Response({"result": "Muvaffaqqiyatli o'chirildi!"})
        except:
            return Response({"error": "Bunday post mavjud emas!"})



