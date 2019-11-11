from django.urls import path

from .views import PycListView, PycDetailView, PycResumeView

urlpatterns = [
	path('post/<int:pk>/', 
		PycDetailView.as_view(), 
		name='post_detail'),
	path('', PycListView.as_view(), name='home'),
	path('resume', PycResumeView.as_view(), name='resume'),
]

