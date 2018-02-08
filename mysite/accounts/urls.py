from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.profile,  name="profile"),
    url(r'^edit', views.account_edit, name="edit"),
    url(r'^user/inbox', views.inbox, name="inbox"),
]
