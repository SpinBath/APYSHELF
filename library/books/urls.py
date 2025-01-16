from rest_framework import routers
from books.api import BookViewSet, LoanViewSet, UserViewSet
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from . import views



router = routers.DefaultRouter()

router.register('api/books', BookViewSet)
router.register('api/loans', LoanViewSet)
router.register('api/users', UserViewSet)




urlpatterns = [

    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="Libray API")),

    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),

]