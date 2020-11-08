from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate

urlpatterns = [
  path('', BlogList.as_view(), name='blog_list'),
  path('detail/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
  path('create/', BlogCreate.as_view(), name='create'),
]
