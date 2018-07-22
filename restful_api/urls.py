from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, UserDetail

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),  # e.g. users/1/
]

#  Allows for /users/<pk>.json to return raw json
urlpatterns = format_suffix_patterns(urlpatterns)
