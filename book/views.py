from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializer import *

class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    http_method_names = ['get','post','put','delete']
    permission_classes = (IsAuthenticated,)

    # def list(self, request, *args, **kwargs):
    #     pass

    def create(self, request, *args, **kwargs):
        # print(request.data)
        # name = request.data['name']
        # Category.objects.create(name=name)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':"Error"},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        cat = Category.objects.get(id=int(kwargs['pk']))
        return Response({'id':cat.id,'name':cat.name})

    def destroy(self, request, *args, **kwargs):
        Category.objects.get(id=int(kwargs['pk'])).delete()
        return Response({'message': "ok"})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data = request.data)
        serializer.is_valid(raise_exception=True)
        if instance.name != request.data['name']:
            cat = Category.objects.get(id=int(kwargs['pk']))
            cat.name = request.data['name']
            cat.save()
            return Response({'message':"ok"})
        return Response(status=status.HTTP_400_BAD_REQUEST)

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def list(self, request, *args, **kwargs):
        data = self.get_queryset().all().order_by('-id')
        context = []
        for i in data:
            a = {
                'id':i.id,
                "name": i.name,
                "image": i.imageURL,
                "description": i.description,
                'published':i.published,
                "author": i.author.fullname,
                "janr": [j.name for j in i.janr.all()]
            }
            context.append(a)
        return Response(context)

class RetrieveBookApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class AuthorApiView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class ReadersApiView(viewsets.ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializers

