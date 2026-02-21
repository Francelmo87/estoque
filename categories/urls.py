from django.urls import path

from . import views 
from . import views 

urlpatterns = [
    path('list/', views.CategoryListView.as_view(), name='category_list'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    path('api/v1/', views.CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('<int:pk>/api/v1/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail-api-view'),
]
