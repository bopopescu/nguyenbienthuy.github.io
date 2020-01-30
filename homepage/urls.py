# from django.urls import path
from django.conf.urls import url
# import view from local directory
from . import views


urlpatterns = [

    # do not use empty string in the url request path, it will intercept all request url with all request path value.
    # url(r'', views.home_page, name='home_page'),
    # if you want to intercept the django app root path request just use url path r'^$' to map it.
    # Then following url mapping will handle request http://127.0.0.1:8000/ with view function home_page.
    # Map to url http://127.0.0.1:8000/user/home/
    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage', views.homepage, name='homepage'),
]