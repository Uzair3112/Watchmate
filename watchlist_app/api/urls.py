from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_detail
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, 
                                     ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS
                                     , UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'), 
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
]
