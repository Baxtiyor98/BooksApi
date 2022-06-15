from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializer import *

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class RetrieveBookApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

