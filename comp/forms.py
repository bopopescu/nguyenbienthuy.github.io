from django.http import JsonResponse
from django.shortcuts import render
from comp.models import *
# Load options of dropdown lists


def load_companies(request):
    # company_id = request.GET.get('company')
    selected_company = request.GET.get('selected_company')
    if len(selected_company) == 0:
        selected_company = '0'
    companies = Company.objects\
        .values('company_id', 'company_name')\
        .filter(is_active=True)\
        .order_by('company_name')
    return render(request, 'company/dropdown_list/company_dropdown_list_options.html',
                  {'companies': companies, 'selected_company': selected_company})


def load_companies_cbb(request):
    if request is None:
        companies = []
    else:
        companies = Company.objects\
            .values('company_id', 'company_name', 'company_short_name', 'certificate__company_address') \
            .filter(is_active=True) \
            .order_by('company_name')
    return JsonResponse({'data': list(companies)})


def load_depts(request):
    company_id = request.GET.get('company')
    selected_dept = request.GET.get('selected_dept')

    if selected_dept is None:
        selected_dept = '0'
    if len(selected_dept) == 0:
        selected_dept = '0'
    else:
        if len(company_id) == 0:
            company_id = str(DeptOfCompany.objects
                             .values('company_id')
                             .filter(dept_id=selected_dept)
                             .first()['company_id'])
    depts = Department.objects\
        .values('dept_id', 'dept_name', 'deptofcompany__company_id')\
        .filter(deptofcompany__company_id=company_id, is_active=True)\
        .order_by('dept_name')
    return render(request, 'company/dropdown_list/dept_dropdown_list_options.html',
                  {'depts': depts, 'selected_dept': str(selected_dept)})


def load_subdepts(request):
    # subdepts = {}
    # company_id = request.GET.get('company')
    dept_id = request.GET.get('dept')
    selected_subdept = request.GET.get('selected_subdept')
    if selected_subdept is None:
        selected_subdept = '0'
    if len(selected_subdept) == 0:
        selected_subdept = '0'
    else:
        if len(dept_id) == 0:
            # subdepts = SubDepartment.objects.filter(subdept_id=subdept_choose)
            dept_id = str(SubdeptOfDept.objects.values('dept_id').filter(subdept_id=selected_subdept).first()['dept_id'])

    subdepts = SubDepartment.objects.filter(subdeptofdept__dept_id=dept_id, is_active=True).order_by('subdept_name')

    return render(request, 'company/dropdown_list/subdept_dropdown_list_options.html',
                  {'subdepts': subdepts, 'selected_subdept': int(selected_subdept)})
