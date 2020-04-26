from django.conf.urls import url
from . import views

app_name = 'profili'

urlpatterns = [

	url(r"^profile_view/$",views.profile_detail, name="detail"),
	url(r"^edit/$",views.profile_edit,name="edit")
]
