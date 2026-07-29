from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home_page'),
   path('image_detection/', views.image_detection, name='image_detection'),
   path(
        "live_detection/",
        views.live_detection,
        name="live_detection"
    ),

    path(
        "predict-frame/",
        views.predict_frame,
        name="predict_frame"
    ),

#     path('video_detection', views.video_detection, name='video_detection'),
#     path("delete_video/", views.delete_video, name="delete_video"),
]