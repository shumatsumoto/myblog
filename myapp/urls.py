from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete


urlpatterns = [
  path('', BlogList.as_view(), name='blog_list'),
  path('detail/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
  path('create/', BlogCreate.as_view(), name='create'),
  path('update/<int:pk>', BlogUpdate.as_view(), name='blog_update'),
  path('delete/<int:pk>', BlogDelete.as_view(), name='blog_delete'),
]
