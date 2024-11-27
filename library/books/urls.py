from rest_framework import routers
from .api import BookViewSet, LoanViewSet, UserViewSet, GroupViewSet
from django.urls import include, path
from rest_framework.documentation import include_docs_urls



router = routers.DefaultRouter()

router.register('api/books', BookViewSet)
router.register('api/loans', LoanViewSet)
router.register('api/users', UserViewSet)
router.register('api/groups', GroupViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title="Libray API"))
]