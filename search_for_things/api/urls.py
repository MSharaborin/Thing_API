from django.urls import path
from .views import (StolenAPI,
                    DetailStolenAPI,
                    PictureStolenAPI,
                    PersonAPI,
                    PicturePersonAPI,
                    DetailPersonAPI,
                    UserAPI,
                    SearchAPI,
                    )


urlpatterns = [
    # API StolenItem
    path('stolen/', StolenAPI.as_view(),),
    path('stolen/<int:pk>/', DetailStolenAPI.as_view()),
    # API Picture Stolen
    path('stolen/pic/', PictureStolenAPI.as_view(),),

    # API Person
    path('person/', PersonAPI.as_view(),),
    path('person/<int:pk>/', DetailPersonAPI.as_view(),),
    # API Picture Person
    path('person/pic/', PicturePersonAPI.as_view(),),

    # API User
    path('user/<str:user>/', UserAPI.as_view()),

    # API Search
    path('stolen/search/<str:search>/', SearchAPI.as_view())
]