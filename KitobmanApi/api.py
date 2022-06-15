from book.views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
# router.register(r'news', BookApiView, basename='news')

urlpatterns = router.urls

urlpatterns += [
    path('books/', BookApiView.as_view(), name='books'),
    path('books/<int:pk>/', RetrieveBookApiView.as_view(), name='retrieve-books'),
]