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
    url(r'^$', views.comp_actions, name='comp_actions'),

    url(r'^comp/$', views.comp, name='company'),
    url(r'^add_company/$', views.add_company, name='add_company'),
    url(r'^edit_company/$', views.edit_company, name='edit_company'),
    url(r'^add_comp_success/$', views.add_comp_success, name='add_comp_success'),

    url(r'^dept/$', views.dept, name='dept'),
    url(r'^add_dept/$', views.add_dept, name='add_dept'),
    url(r'^add_dept_success/$', views.add_dept_success, name='add_dept_success'),

    url(r'^subdept/$', views.subdept, name='subdept'),
    url(r'^add_subdept/$', views.add_subdept, name='add_subdept'),
    url(r'^add_subdept_success/$', views.add_subdept_success, name='add_subdept_success'),
]
