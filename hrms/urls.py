# from django.urls import path
from django.conf.urls import url
from django.urls import path
# import view from local directory
import comp.forms as comp_forms
from hrms import dropdowns
from . import views
from hrms.views import *

urlpatterns = [

    # do not use empty string in the url request path, it will intercept all request url with all request path value.
    # url(r'', views.home_page, name='home_page'),
    # if you want to intercept the django app root path request just use url path r'^$' to map it.
    # Then following url mapping will handle request http://127.0.0.1:8000/ with view function home_page.

    url(r'^$', views.hrms_page, name='hrms_page'),
    # Map to url http://127.0.0.1:8000/hrms/

    url(r'^hrms/$', views.hrms_page, name='hrms_page'),
    url(r'^employee_new/$', views.employee_new, name='employee_new'),
    url(r'^employee_success/$', views.employee_success, name='employee_success'),

    # Load dropdownlist
    path('ajax/load_depts/', comp_forms.load_depts, name='ajax_load_depts'),
    path('ajax/load_subdepts/', comp_forms.load_subdepts, name='ajax_load_subdepts'),
    path('ajax/load_companies/', comp_forms.load_companies, name='ajax_load_companies'),
    path('ajax/load_companies_cbb/', comp_forms.load_companies_cbb, name='ajax_load_companies_cbb'),

    path('ajax/load_employee/', dropdowns.load_employee, name='ajax_load_employee'),
    path('ajax/load_genders/', dropdowns.load_genders, name='ajax_load_genders'),
    path('ajax/load_idnames/', dropdowns.load_idnames, name='ajax_load_idnames'),
    path('ajax/load_places/', dropdowns.load_idplaces, name='ajax_load_idplaces'),
    path('ajax/load_people/', dropdowns.load_people, name='ajax_load_people'),
    path('ajax/load_countries/', dropdowns.load_countries, name='ajax_load_countries'),
    path('ajax/load_currency/', dropdowns.load_currency, name='ajax_load_currency'),
    path('ajax/load_workingtime/', dropdowns.load_workingtime, name='ajax_load_workingtime'),
    path('ajax/load_daysofweek/', dropdowns.load_daysofweek, name='ajax_load_daysofweek'),
    path('ajax/load_workinggroup/', dropdowns.load_workinggroup, name='ajax_load_workinggroup'),
    path('ajax/load_salaryscale/', dropdowns.load_salaryscale, name='ajax_load_salaryscale'),
    path('ajax/load_salarybasic/', dropdowns.load_salarybasic, name='ajax_load_salarybasic'),

    # Giới tính
    path('gender_list/', GenderListView.as_view(), name='gender_list'),
    path('gender_add/', GenderCreateView.as_view(), name='gender_add'),
    path('<str:pk>/gender_edit/', GenderUpdateView.as_view(), name='gender_edit'),
    path('<str:pk>/gender_delete/', GenderDeleteView.as_view(), name='gender_delete'),
    # Loại tiền
    path('currency_list/', CurrencyListView.as_view(), name='currency_list'),
    path('currency_add/', CurrencyCreateView.as_view(), name='currency_add'),
    path('<str:pk>/currency_edit/', CurrencyUpdateView.as_view(), name='currency_edit'),
    path('<str:pk>/currency_delete/', CurrencyDeleteView.as_view(), name='currency_delete'),

    # Nơi cấp CMND
    path('place_id_list/', PlaceOfIdentificationSearchListView.as_view(), name='place_id_list'),
    path('place_id_add/', PlaceOfIdentificationCreateView.as_view(), name='place_id_add'),
    path('<str:pk>/place_id_edit/', PlaceOfIdentificationUpdateView.as_view(), name='place_id_edit'),
    path('<str:pk>/place_id_delete/', PlaceOfIdentificationDeleteView.as_view(), name='place_id_delete'),
    # Loại giấy tờ tùy thân
    path('idname_list/', IdNameListView.as_view(), name='idname_list'),
    path('idname_add/', IdNameCreateView.as_view(), name='idname_add'),
    path('<str:pk>/idname_edit/', IdNameUpdateView.as_view(), name='idname_edit'),
    path('<str:pk>/idname_delete/', IdNameDeleteView.as_view(), name='idname_delete'),
    # Dân tộc
    path('people_list/', PeopleListView.as_view(), name='people_list'),
    path('people_add/', PeopleCreateView.as_view(), name='people_add'),
    path('<int:pk>/people_edit/', PeopleUpdateView.as_view(), name='people_edit'),
    path('<int:pk>/people_delete/', PeopleDeleteView.as_view(), name='people_delete'),
    # Quốc tịch
    path('nation_list/', NationListView.as_view(), name='nation_list'),
    path('nation_add/', NationCreateView.as_view(), name='nation_add'),
    path('<str:pk>/nation_edit/', NationUpdateView.as_view(), name='nation_edit'),
    path('<str:pk>/nation_delete/', NationDeleteView.as_view(), name='nation_delete'),
    # Tiền ăn trưa
    path('mealmoney_list/', MealMoneyListView.as_view(), name='mealmoney_list'),
    path('mealmoney_add/', MealMoneyCreateView.as_view(), name='mealmoney_add'),
    path('<int:pk>/mealmoney_edit/', MealMoneyUpdateView.as_view(), name='mealmoney_edit'),
    path('<int:pk>/mealmoney_delete/', MealMoneyDeleteView.as_view(), name='mealmoney_delete'),

    # Tiền lương cơ bản
    path('salarybasic_list/', SalaryBasicListView.as_view(), name='salarybasic_list'),
    path('salarybasic_add/', SalaryBasicCreateView.as_view(), name='salarybasic_add'),
    path('<int:pk>/salarybasic_edit/', SalaryBasicUpdateView.as_view(), name='salarybasic_edit'),
    path('<int:pk>/salarybasic_delete/', SalaryBasicDeleteView.as_view(), name='salarybasic_delete'),
    # Tỷ lệ Tiền lương cơ bản tăng thêm
    path('salarybasic_plus_list/', SalaryBasicPlusListView.as_view(), name='salarybasic_plus_list'),
    path('salarybasic_plus_add/', SalaryBasicPlusCreateView.as_view(), name='salarybasic_plus_add'),
    path('<int:pk>/salarybasic_plus_edit/', SalaryBasicPlusUpdateView.as_view(), name='salarybasic_plus_edit'),
    path('<int:pk>/salarybasic_plus_delete/', SalaryBasicPlusDeleteView.as_view(), name='salarybasic_plus_delete'),
    # Hệ số lương
    path('salaryscale_list/', SalaryScaleListView.as_view(), name='salaryscale_list'),
    path('salaryscale_add/', SalaryScaleCreateView.as_view(), name='salaryscale_add'),
    path('<int:pk>/salaryscale_edit/', SalaryScaleUpdateView.as_view(), name='salaryscale_edit'),
    path('<int:pk>/salaryscale_delete/', SalaryScaleDeleteView.as_view(), name='salaryscale_delete'),
    # Tỷ lệ đóng BHXH, BHYT, BHTN
    path('insurance_list/', InsuranceListView.as_view(), name='insurance_list'),
    path('insurance_add/', InsuranceCreateView.as_view(), name='insurance_add'),
    path('<int:pk>/insurance_edit/', InsuranceUpdateView.as_view(), name='insurance_edit'),
    path('<int:pk>/insurance_delete/', InsuranceDeleteView.as_view(), name='insurance_delete'),

    # Tỷ lệ đóng Công đoàn
    path('union_list/', UnionListView.as_view(), name='union_list'),
    path('union_add/', UnionCreateView.as_view(), name='union_add'),
    path('<int:pk>/union_edit/', UnionUpdateView.as_view(), name='union_edit'),
    path('<int:pk>/union_delete/', UnionDeleteView.as_view(), name='union_delete'),

    # Làm việc ngày thứ 7
    path('workingtime_list/', WorkingTimeListView.as_view(), name='workingtime_list'),
    path('workingtime_add/', WorkingTimeCreateView.as_view(), name='workingtime_add'),
    path('<int:pk>/workingtime_edit/', WorkingTimeUpdateView.as_view(), name='workingtime_edit'),
    path('<int:pk>/workingtime_delete/', WorkingTimeDeleteView.as_view(), name='workingtime_delete'),
    # Ngày trong tuần
    path('days_list/', DaysOfWeekListView.as_view(), name='days_list'),
    path('days_add/', DaysOfWeekCreateView.as_view(), name='days_add'),
    path('<str:pk>/days_edit/', DaysOfWeekUpdateView.as_view(), name='days_edit'),
    path('<str:pk>/days_delete/', DaysOfWeekDeleteView.as_view(), name='days_delete'),

    # Nhóm làm việc
    path('workinggroup_list/', WorkingGroupListView.as_view(), name='workinggroup_list'),
    path('workinggroup_add/', WorkingGroupCreateView.as_view(), name='workinggroup_add'),
    path('<int:pk>/workinggroup_edit/', WorkingGroupUpdateView.as_view(), name='workinggroup_edit'),
    path('<int:pk>/workinggroup_delete/', WorkingGroupDeleteView.as_view(), name='workinggroup_delete'),

    # Thời gian làm việc chi tiết
    path('workschedules_list/', WorkSchedulesListView.as_view(), name='workschedules_list'),
    path('workschedules_add/', WorkSchedulesCreateView.as_view(), name='workschedules_add'),
    path('<int:pk>/workschedules_edit/', WorkSchedulesUpdateView.as_view(), name='workschedules_edit'),
    path('<int:pk>/workschedules_delete/', WorkSchedulesDeleteView.as_view(), name='workschedules_delete'),
    # Hợp đồng lao động
    path('laborcontract_list/', LaborContractListView.as_view(), name='laborcontract_list'),
    path('laborcontract_add/', LaborContractCreateView.as_view(), name='laborcontract_add'),
    path('<int:pk>/laborcontract_edit/', LaborContractUpdateView.as_view(), name='laborcontract_edit'),
    path('<int:pk>/laborcontract_delete/', LaborContractDeleteView.as_view(), name='laborcontract_delete')
]
