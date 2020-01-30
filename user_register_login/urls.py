from django.urls import path
from django.conf.urls import url
# import view from local directory
from . import views

urlpatterns =[

    # do not use empty string in the url request path, it will intercept all request url with all request path value.
    # url(r'', views.home_page, name='home_page'),
    # if you want to intercept the django app root path request just use url path r'^$' to map it.
    # Then following url mapping will handle request http://127.0.0.1:8000/ with view function home_page.
    url(r'^$', views.home_page, name='home_page'),
    # Map to url http://127.0.0.1:8000/user/home/
    url(r'^home/$', views.home_page, name='home_page'),
    # When user browse http://localhost:8000/user/do_login, it will invoke the do_login function defined in views.py.
    url(r'^do_login/$', views.do_login, name='do_login'),
    # Map to url http://127.0.0.1:8000/user/login_success/, this url will be invoked after login success.
    url(r'^login_success/$', views.login_success, name='login_success'),
    # Map to url http://127.0.0.1:8000/user/register/
    url(r'^register/$', views.user_register, name='user_register'),
    # When user browse http://localhost:8000/user/do_register, it will invoke the do_register function
    # defined in views.py.
    url(r'^do_register/$', views.do_register, name='do_register'),
    # Map to url http://127.0.0.1:8000/user/register_success/, this url will be invoked after register success.
    url(r'^register_success/$', views.register_success, name='register_success'),
]
