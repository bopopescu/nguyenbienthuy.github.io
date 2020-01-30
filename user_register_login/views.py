from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your views here.


def home_page(request):
    return render(request, 'user_register_login/user_login.html')


def do_login(request):
    request_method = request.method
    print('request_method = ' + request_method)

    if request_method == 'POST':
        user_name = request.POST.get('username', '')
        user_password = request.POST.get('password', '')

        # Authenticate user account
        user = auth.authenticate(request, username=user_name, password=user_password)

        if user is not None:
            # Show login success info to client browser directly.

            auth.login(request, user)
            # redirect web page to login success page.
            response = HttpResponseRedirect('/admin')
            # set cookie to transfer username to login success page
            response.set_cookie('user_name', user_name, 3600)
            return response
        else:
            error_json = {'error_message': "Username hoặc password không đúng."}
            return render(request, 'user_register_login/user_login.html', error_json)
    else:
        return render(request, 'user_register_login/user_login.html')


def login_success(request):
    # get username from cookie.
    user_name = request.COOKIES.get('user_name', '')
    # pass user_name to display web page
    return render(request, 'user_register_login/user_login_success.html', {'user_name': user_name})


def user_register(request):
    # Clear session value before register.
    request.session['user_name'] = ''
    request.session['user_password'] = ''
    request.session['user_email'] = ''

    return render(request, 'user_register_login/user_register.html',
                  {'user_name': '', 'user_password': '', 'user_email': ''})


def do_register(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')
        user_email = request.POST.get('user_email', '')
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.
            user = auth.authenticate(request, username=user_name, password=user_password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=user_name, password=user_password,
                                                            email=user_email)
                # update user object staff field value and save to db.
                if user is not None:
                    user.is_staff = True
                    # save user properties in sqlite auth_user table.
                    user.save()
                # redirect web page to register success page.
                response = HttpResponseRedirect('/user/register_success/')
                # set user name, password and email value in session.
                request.session['user_name'] = user_name
                request.session['user_password'] = user_password
                request.session['user_email'] = user_email
                return response
            else:
                error_json = {'error_message': 'User account exist, please register another one.'}
                return render(request, 'user_register_login/user_register.html', error_json)
        else:
            error_json = {'error_message': 'User name, password and email can not be empty.'}
            return render(request, 'user_register_login/user_register.html', error_json)
    else:
        return render(request, 'user_register_login/user_register.html')


def register_success(request):
    # get user name, password, email value from session.
    user_name = request.session.get('user_name','')
    user_password = request.session.get('user_password', '')
    user_email = request.session.get('user_email', '')
    # pass user_name, user_password and user_email to display web page.
    return render(request, 'user_register_login/user_register_success.html',
                  {'user_name':user_name, 'user_password': user_password,'user_email': user_email})
