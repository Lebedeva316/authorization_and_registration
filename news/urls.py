from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
   path('news_list/', ArticleList.as_view()),
   path('<int:pk>', ArticleDetail.as_view()),
]
