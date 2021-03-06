from django.urls import path
from ..api import monitor as MonitorAPI
urlpatterns=[
    # Resource host api
    path(r'v1/host/<uuid:pk>/cpu/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailCPUAPI.as_view()),
    path(r'v1/host/<uuid:pk>/memory/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailMemoryAPI.as_view()),
    path(r'v1/host/<uuid:pk>/disk/read/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailIReadIOPS.as_view()),
    path(r'v1/host/<uuid:pk>/internet/in/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailInternetInRate.as_view()),
]