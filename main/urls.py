from django.urls import path
from main.v1_views.auth import Sign_in, Sign_up
from main.v1_views.core import ProductView, CategoryView, Post_ImagesView



urlpatterns = [
    ###         Authenticate        ###
    path("sign-in/", Sign_in.as_view()),
    path("sign-up/", Sign_up.as_view()),

    ###          Category           ###
    path("ctg/", CategoryView.as_view()),
    path("ctg/<int:pk>/", CategoryView.as_view()),

    ###         Product_post        ###
    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductView.as_view()),

    ###           Imaga_post        ###
    path("img/", Post_ImagesView.as_view()),
    path("img/<int:pk>/", Post_ImagesView.as_view()),

]
