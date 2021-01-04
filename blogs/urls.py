from django.urls import path

from .views import HomePageView, CategoryDetail, TestPageView

app_name = "blogs"

urlpatterns = [
    path("", HomePageView.as_view(), name='index'),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("test/", TestPageView.as_view(), name="test")
]
