# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder
# import json as simplejson

# from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from hrms.models import *


# Load data for Droppdown Giới tính
# from mymodule.cnn_company import get_company


def load_genders(request):
    # company_id = request.GET.get('company')
    selected_gender = request.GET.get('selected_gender')
    if len(selected_gender) == 0:
        selected_gender = '0'
    genders = Gender.objects.values('gender_id', 'gender_name').all().order_by('gender_name')
    return render(request, 'hrms/employee/dropdown_list/gender_dropdown_list_options.html',
                  {'genders': genders, 'selected_gender': selected_gender})


# Load data for Droppdown Loại giấy tờ tùy thân
def load_idnames(request):
    selected_idname = request.GET.get('selected_idname')
    if len(selected_idname) == 0:
        selected_idname = '0'
    idnames = IdName.objects\
        .values('id_name_code', 'name_of_identification')\
        .all().order_by('name_of_identification')
    return render(request, 'hrms/employee/dropdown_list/idname_dropdown_list_options.html',
                  {'idnames': idnames, 'selected_idname': selected_idname})


# Load data for Droppdown Nơi cấp
def load_idplaces(request):
    selected_idplace = request.GET.get('selected_idplace')
    if len(selected_idplace) == 0:
        selected_idplace = '0'
    idplaces = PlaceOfIdentification.objects\
        .values('place_id', 'place_of_identification')\
        .all().order_by('place_of_identification')
    return render(request, 'hrms/employee/dropdown_list/idplace_dropdown_list_options.html',
                  {'idplaces': idplaces, 'selected_idplace': selected_idplace})


# Load data for Droppdown Dân tộc
def load_people(request):
    selected_people = request.GET.get('selected_people')
    if len(selected_people) == 0:
        selected_people = '0'
    people = People.objects\
        .values('people_id', 'people_name')\
        .all().order_by('people_name')
    return render(request, 'hrms/employee/dropdown_list/people_dropdown_list_options.html',
                  {'people': people, 'selected_idplace': selected_people})


# Load data for Droppdown Quốc tịch
def load_countries(request):
    selected_country = request.GET.get('selected_country')
    if len(selected_country) == 0:
        selected_country = '0'
    countries = Nation.objects\
        .values('nation_id', 'nation_name')\
        .all().order_by('nation_name')
    return render(request, 'hrms/employee/dropdown_list/country_dropdown_list_options.html',
                  {'countries': countries, 'selected_country': selected_country})


# Load data for Droppdown Loại tiền
def load_currency(request):
    """
    selected_currency = request.GET.get('selected_currency')
    if selected_currency is None:
        selected_currency = '0'
        if len(selected_currency) == 0:
            selected_currency = '0'
    """
    currency = Currency.objects.values('currency_id', 'currency_name').all().order_by('currency_name')
    return render(request, 'hrms/employee/dropdown_list/currency_dropdown_list_options.html',
                  {'currency': currency, })


def load_workingtime(request):
    if request is None:
        w = []
    else:
        w = WorkingTime.objects.values('workingtime_id', 'name', 'starttime', 'endtime', 'description').all()\
            .order_by('workingtime_id')
    return JsonResponse({'data': list(w)})


def load_daysofweek(request):
    if request is None:
        daysofweek = []
    else:
        daysofweek = DaysOfWeek.objects.values('daysofweek_id', 'dayname').all().order_by('daysofweek_id')
    return JsonResponse({'data': list(daysofweek)})


def load_workinggroup(request):
    if request is None:
        workinggroup = []
    else:
        workinggroup = WorkingGroup.objects.values('workinggroup_id', 'name').all().order_by('workinggroup_id')
    return JsonResponse({'data': list(workinggroup)})


def load_employee(request):
    if request is None:
        emp = []
    else:
        emp = Employee.objects.values('cif', 'fullname', 'birthday', 'gender__gender_name').all().order_by('cif')
    return JsonResponse({'data': list(emp)})


def load_salaryscale(request):
    if request is None:
        s = []
    else:
        s = SalaryScale.objects.values('scale_id', 'name', 'scale').all().order_by('name')
    return JsonResponse({'data': list(s)})


def load_salarybasic(request):
    if request is None:
        s = []
    else:
        s = SalaryBasic.objects.values('salary_basic_id', 'name', 'amount', 'currency__currency_name').all()
    return JsonResponse({'data': list(s)})
