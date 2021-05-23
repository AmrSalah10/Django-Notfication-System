from django.urls import include, path
from django.urls import path, include
from django.conf.urls import url
import notifications.urls
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout_view, name='logout'),
    path('sendMsg', views.sendMsg, name='sendMsg'),
    path('sendMsgAll', views.sendMsgAll, name='sendMsgAll'),
    url('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

