from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'), #pulls primary key from class PostDetailView
    path('post/edit/<int:pk>/', PostEditView.as_view(), name = 'post_edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name = 'comment_delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)