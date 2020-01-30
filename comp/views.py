from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.contrib import auth
from mymodule.cnn_company import *
from mymodule.fun_assistant import *
from comp.models import Company, Certificate, Department, SubDepartment, Positions
from comp.models import DeptOfCompany, SubdeptOfDept
from django.db import IntegrityError, transaction
from datetime import datetime
from django.db.models import Max
import json as simplejson
from django.core.serializers.json import DjangoJSONEncoder
# import io
# Create your views here.


def comp_actions(request):
    comp_attribute = {
        'data': simplejson.dumps(get_company(), ensure_ascii=True, cls=DjangoJSONEncoder),
    }
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        key_seach = request.POST.get('search', '')
        if len(key_seach) > 0:
            # Button 'edit_comp' được click
            if 'edit_comp' in request.POST:
                # View form to edit
                comp_attribute = view_comp(str(key_seach), readonly='')
            else:
                # Read only form
                comp_attribute = view_comp(str(key_seach), readonly='readonly')
            return render(request, 'company/company_edit.html', comp_attribute)
        else:
            return HttpResponseRedirect('/comp/comp')
    else:
        return render(request, 'company/comp_actions.html', comp_attribute)


def comp(request):
    comp_attribute = {
        'company_id': "",
        'checked': "checked",
        'company_name': "",
        'company_short_name': "",
        'certificate_code': "",
        'code_tax': "",
        'cert_day': "",
        'cert_place': "",
        'company_phone': "",
        'company_fax': "",
        'company_email': "",
        'company_address': "",
        'data': simplejson.dumps(get_company(), ensure_ascii=True, cls=DjangoJSONEncoder),
        'readonly': "",
    }
    # data1 = simplejson.dumps(get_company())
    # data1 = {"msg": "", "data": get_company()}
    # with open('static/multi-column/company.json', 'w', encoding='utf-8') as myfile:
    #    simplejson.dump(data1, myfile, ensure_ascii=False)
    return render(request, 'company/company_new.html', comp_attribute)


# Mã công ty đã có thì view readonly
def view_comp(company_id, readonly):
    # readonly = "": edit mẫu tin
    # readonly = 'readonly': view mẫu tin
    # form_status có 2 trạng thái 'UPDATE_RECORD', 'CHANGE_RECORD' hoặc 'NEW_RECORD'
    comp_attribute = {}
    for c in get_company(company_id=company_id):
        comp_attribute = {
            'company_id': c["company_id"],
            'checked': "checked",
            'company_name': c["company_name"],
            'company_short_name': c["company_short_name"],
            'certificate_id': c["certificate_id"],
            'certificate_code': c["certificate_code"],
            'code_tax': c["code_tax"],
            'cert_day': c["cert_day"],
            'cert_place': c["cert_place"],
            'company_phone': c["company_phone"],
            'company_fax': c["company_fax"],
            'company_email': c["company_email"],
            'company_address': c["company_address"],
            'data': simplejson.dumps(get_company(), ensure_ascii=True, cls=DjangoJSONEncoder),
            'readonly': readonly,
        }
    return comp_attribute


@transaction.atomic
def add_company(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        line = 1
        comp_attribute = {}
        err_string = ""

        # Add Comp_Company
        # Nếu auto_company_id checked thì tìm mã công ty lớn nhất trong database
        # Ngược lại thì kiểm tra mã nhập
        auto_company_id = request.POST.get('auto_company_id', '')
        if len(auto_company_id) > 0:
            # Mã công ty tiếp theo
            n = Company.objects.all().aggregate(Max('company_id'))
            if n['company_id__max'] is None:
                companycode = str(1000)
            else:
                companycode = str(int(n['company_id__max'])+1)
        else:
            companycode = request.POST.get('company_id', '')
        comp_attribute.update({'company_id': str(companycode)})  # đặt giá trị cho input khi render
        if len(companycode) != 4:
            err_string += "<a href=\"#company_id\" class=\"err_string\">" + str(line) \
                          + ". Mã công ty không hợp lệ!</a><br/>"
            line += 1
        else:
            company = Company.objects.filter(company_id=companycode).count()
            if company > 0:
                err_string += "<a href=\"#company_id\" class=\"err_string\">" + str(line) \
                              + ". Mã công ty đã có!</a><br/>"
                line += 1
      
        companyname = request.POST.get('company_name', '')
        comp_attribute.update({'company_name': str(companyname)})  # đặt giá trị cho input khi render
        if len(companyname) == 0:
            err_string += "<a href=\"#company_name\" class=\"err_string\">" + str(line) \
                          + ". Tên công ty không được bỏ trống!</a><br/>"
            line += 1
        
        comp_shortname = request.POST.get('company_short_name', '')
        comp_attribute.update({'company_short_name': str(comp_shortname)})  # đặt giá trị cho input khi render
        
        # Add Comp_Certificate
        cert_code = request.POST.get('certificate_code', '')
        comp_attribute.update({'certificate_code': str(cert_code)})  # đặt giá trị cho input khi render
        if len(cert_code) == 0:
            err_string += "<a href=\"#certificate_code\" class=\"err_string\">" + str(line) \
                          + ". Mã giấy ĐKKD không được bỏ trống!</a><br/>"
            line += 1
      
        codetax = request.POST.get('code_tax', '')
        comp_attribute.update({'code_tax': str(codetax)})  # đặt giá trị cho input khi render
        if len(codetax) == 0:
            err_string += "<a href=\"#code_tax\" class=\"err_string\">" + str(line) \
                          + ". Mã số thuế không được bỏ trống!</a><br/>"
            line += 1
        # Ngày cấp giấy đkkd
        cert_day = request.POST.get('cert_day', '')
        # comp_attribute.update({'cert_day': datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')})
        if len(cert_day) == 0:
            err_string += "<a href=\"#cert_day\" class=\"err_string\">" + str(line) \
                          + ". Ngày cấp ĐKKD không được bỏ trống!</a><br/>"
            line += 1
        else:
            # đặt giá trị cho input khi render (Tránh trường hợp ngày cấp = '')
            comp_attribute.update({'cert_day': datetime.strptime(str(cert_day), '%Y-%m-%d')})

        cert_place = request.POST.get('cert_place', '')
        comp_attribute.update({'cert_place': str(cert_place)})  # đặt giá trị cho input khi render
        if len(cert_place) == 0:
            err_string += "<a href=\"#cert_place\" class=\"err_string\">" + str(line) \
                          + ". Nơi cấp ĐKKD không được bỏ trống!</a><br/>"
            line += 1

        company_phone = request.POST.get('company_phone', '')
        comp_attribute.update({'company_phone': str(company_phone)})  # đặt giá trị cho input khi render
        
        company_fax = request.POST.get('company_fax', '')
        comp_attribute.update({'company_fax': str(company_fax)})  # đặt giá trị cho input khi render

        company_email = request.POST.get('company_email', '')
        comp_attribute.update({'company_email': str(company_email)})  # đặt giá trị cho input khi render

        company_address = request.POST.get('company_address', '')
        comp_attribute.update({'company_address': str(company_address)})  # đặt giá trị cho input khi render
        if len(company_address) == 0:
            err_string += "<a href=\"#company_address\" class=\"err_string\">" + str(line) \
                          + ". Địa chỉ công ty không được bỏ trống!</a><br/>"
            line += 1
      
        # Show error on webpage when has error of record

        if len(err_string) == 0:
            flag_test = str(request.POST.get('flag_test', ''))
            # Save mẫu tin
            if flag_test == "save":
                c = Company(company_id=companycode, company_name=companyname, company_short_name=comp_shortname, is_active=1)
                c.save()
                sid = transaction.savepoint()
                try:
                    cert = Certificate(
                        certificate_code=cert_code,
                        company_id=companycode,
                        code_tax=codetax,
                        cert_day=cert_day,
                        cert_place=cert_place,
                        company_phone=company_phone,
                        company_fax=company_fax,
                        company_address=company_address,
                        company_email=company_email,
                        startday=cert_day,
                        endday='9999-12-31')
                    cert.save()
                    transaction.savepoint_commit(sid)
                except IntegrityError:
                    transaction.savepoint_rollback(sid)
                # Thêm mới thành công
                response = HttpResponseRedirect('/comp/add_comp_success')
                return response
            # Save thử mẫu tin
            else:
                return render(request, 'company/company_new.html', comp_attribute)
        else:
            comp_attribute.update({'error_message': err_string})
            return render(request, 'company/company_new.html', comp_attribute)
    else:
        return render(request, 'company/company_new.html')


def edit_company(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        line = 1
        comp_attribute = {}
        err_string = ""
        companycode = request.POST.get('company_id', '')
        comp_attribute.update({'company_id': int(companycode)})

        companyname = request.POST.get('company_name', '')
        comp_attribute.update({'company_name': str(companyname)})  # đặt giá trị cho input khi render
        if len(companyname) == 0:
            err_string += "<a href=\"#company_name\" class=\"err_string\">" + str(line) \
                          + ". Tên công ty không được bỏ trống!</a><br/>"
            line += 1

        comp_shortname = request.POST.get('company_short_name', '')
        comp_attribute.update({'company_short_name': str(comp_shortname)})  # đặt giá trị cho input khi render

        # Add Comp_Certificate
        cert_code = request.POST.get('certificate_code', '')
        comp_attribute.update({'certificate_code': str(cert_code)})  # đặt giá trị cho input khi render
        if len(cert_code) == 0:
            err_string += "<a href=\"#certificate_code\" class=\"err_string\">" + str(line) \
                          + ". Mã giấy ĐKKD không được bỏ trống!</a><br/>"
            line += 1

        codetax = request.POST.get('code_tax', '')
        comp_attribute.update({'code_tax': str(codetax)})  # đặt giá trị cho input khi render
        if len(codetax) == 0:
            err_string += "<a href=\"#code_tax\" class=\"err_string\">" + str(line) \
                          + ". Mã số thuế không được bỏ trống!</a><br/>"
            line += 1
        # Ngày cấp giấy đkkd
        cert_day = request.POST.get('cert_day', '')
        # comp_attribute.update({'cert_day': datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')})
        if len(cert_day) == 0:
            err_string += "<a href=\"#cert_day\" class=\"err_string\">" + str(line) \
                          + ". Ngày cấp ĐKKD không được bỏ trống!</a><br/>"
            line += 1
        else:
            # đặt giá trị cho input khi render (Tránh trường hợp ngày cấp = '')
            comp_attribute.update({'cert_day': datetime.strptime(str(cert_day), '%Y-%m-%d')})

        cert_place = request.POST.get('cert_place', '')
        comp_attribute.update({'cert_place': str(cert_place)})  # đặt giá trị cho input khi render
        if len(cert_place) == 0:
            err_string += "<a href=\"#cert_place\" class=\"err_string\">" + str(line) \
                          + ". Nơi cấp ĐKKD không được bỏ trống!</a><br/>"
            line += 1

        company_phone = request.POST.get('company_phone', '')
        comp_attribute.update({'company_phone': str(company_phone)})  # đặt giá trị cho input khi render

        company_fax = request.POST.get('company_fax', '')
        comp_attribute.update({'company_fax': str(company_fax)})  # đặt giá trị cho input khi render

        company_email = request.POST.get('company_email', '')
        comp_attribute.update({'company_email': str(company_email)})  # đặt giá trị cho input khi render

        company_address = request.POST.get('company_address', '')
        comp_attribute.update({'company_address': str(company_address)})  # đặt giá trị cho input khi render

        cert_id = request.POST.get('certificate_id', '')
        comp_attribute.update({'certificate_id': str(cert_id)})  # đặt giá trị cho input khi render
        if len(company_address) == 0:
            err_string += "<a href=\"#company_address\" class=\"err_string\">" + str(line) \
                          + ". Địa chỉ công ty không được bỏ trống!</a><br/>"
            line += 1
        flag_test = str(request.POST.get('flag_test', ''))
        if len(err_string) == 0 and flag_test == "save":
            # Kiểm tra trường hợp Edit hay Change
            text_changed = request.POST.get('text_changed', '')
            check_changed = check_changed_certificate(certificate_id=cert_id,
                                                      certificate_code1=cert_code,
                                                      code_tax1=codetax,
                                                      cert_day1=cert_day,
                                                      cert_place1=cert_place,
                                                      company_phone1=company_phone,
                                                      company_fax1=company_fax,
                                                      company_address1=company_address,
                                                      company_email1=company_email,
                                                      startday1=cert_day)
            # COMPANY_CHANGE
            if text_changed == "COMPANY_CHANGE" and check_changed:
                # thêm 1 Giấy ĐKKD mới
                cert = Certificate(
                    certificate_code=cert_code,
                    company_id=companycode,
                    code_tax=codetax,
                    cert_day=cert_day,
                    cert_place=cert_place,
                    company_phone=company_phone,
                    company_fax=company_fax,
                    company_address=company_address,
                    company_email=company_email,
                    startday=cert_day,
                    endday='9999-12-31')
                cert.save()
                # Điều chỉnh hạn sử dụng đến ngày (cert_day-1)
                Certificate.objects.filter(certificate_id=cert_id).update(endday=last_of_date(cert_day))
            # COMPANY_EDIT
            else:
                # Update mẫu tin table Company
                c = Company.objects.filter(company_id=companycode)
                c.update(company_name=companyname, company_short_name=comp_shortname)

                # Update mẫu tin table Certificate
                ce = Certificate.objects.filter(certificate_id=cert_id)
                ce.update(
                    certificate_code=cert_code,
                    company_id=companycode,
                    code_tax=codetax,
                    cert_day=cert_day,
                    cert_place=cert_place,
                    company_phone=company_phone,
                    company_fax=company_fax,
                    company_address=company_address,
                    company_email=company_email,
                    startday=cert_day,
                    endday='9999-12-31')
                comp_attribute.update({'readonly': "readonly"})
                return render(request, 'company/company_edit.html', comp_attribute)
        # Save thử hoặc có lỗi
        else:
            comp_attribute.update({'error_message': err_string})
            return render(request, 'company/company_edit.html', comp_attribute)
    else:
        return render(request, 'company/company_edit.html')


def check_changed_certificate(certificate_id, certificate_code1, code_tax1, cert_day1, cert_place1,
                              company_phone1, company_fax1, company_address1, company_email1, startday1):
    # Lấy thông tin dkkd hiện tại
    ce = Certificate.objects.filter(certificate_id=certificate_id)
    # các biến có số 1 là thông tin nhập mới
    # Nếu có thay đổi function trả về giá trị True ngược lại False
    if ce['certificate_code'] != certificate_code1:
        return True
    elif ce['code_tax'] != code_tax1:
        return True
    elif ce['cert_day'] != cert_day1:
        return True
    elif ce['cert_place'] != cert_place1:
        return True
    elif ce['company_phone'] != company_phone1:
        return True
    elif ce['company_fax'] != company_fax1:
        return True
    elif ce['company_address'] != company_address1:
        return True
    elif ce['company_email'] != company_email1:
        return True
    elif ce['startday'] != startday1:
        return True
    else:
        return False


def add_comp_success(request):
    # f = ProductFilter(request.GET, queryset=Product.objects.all())
    get_com = get_company()
    """ author = Authors.objects.get(pk=1)
    books = Books.objects.filter(authorid=author.id)"""

    return render(request, 'company/company_list.html', {'comp': get_com})


def dept(request):
    list_dept_name = [{'dn_name': 'dept_name1', 'dn_id': 'dept_name1', 'dept_name': "",
                       'startday_name': 'startday1', 'startday_id': 'startday1', 'startday': "",
                       'endday_name': 'endday1', 'endday_id': 'endday1', 'endday': "9999-12-31",
                       'row': 1}]
    dept_attribute = {
        'comp': get_company(),
        'dept_name': list_dept_name,
    }
    return render(request, 'company/dept_new.html', dept_attribute)


@transaction.atomic
def add_dept(request):
    request_method = request.method
    print('request_method = ' + request_method)

    if request_method == 'POST':
        err_string = ""
        dept_attribute = {}

        company_id = request.POST.get('company', '')
        # Đặt giá trị cho input khi render
        dept_attribute.update({"company_choose": str(company_id)})

        line = 1
        if len(company_id) == 0:
            err_string += "<a href=\"#company\" class=\"err_string\">" + str(line) + ". Chưa chọn công ty!</a><br/>"
            line += 1

        j = 1
        count_dept_name = request.POST.get('count_dept_name', '')
        dept_attribute.update({"count_dept_name": str(count_dept_name)})  # đặt giá trị cho input khi render
        list_dept = []
        for i in range(j, int(count_dept_name)+1):
            dept_name = request.POST.get('dept_name' + str(i), '')
            if len(dept_name) == 0:
                err_string += "<a href=\"#dept_name\" class=\"err_string\"" + str(i) + "\">" \
                              + str(line) + ". Tên phòng ban " + str(i) + " không được để trống!</a><br/>"
            line += 1
            startday = request.POST.get('startday' + str(i), '')
            if len(startday) == 0:
                err_string += "<a href=\"#startday\" class=\"err_string\"" + str(i) + "\">" \
                              + str(line) + ". Ngày bắt đầu " + str(i) + " không được để trống!></a><br/>"
            line += 1
            # endday = request.POST.get('endday' + str(i), '')
            """
            query_insert += " INSERT INTO gpm_hrms_data.comp_department(company_id, dept_name, startday, endday) " \
                            " VALUES (\'" \
                            + company_id + "\', \'" \
                            + dept_name + "\', \'" \
                            + startday + "\', \'" \
                            + "9999-12-31\');"
            """
            list_dept.append({
                'dn_name': ('dept_name'+str(i)),
                'dn_id': ('dept_name'+str(i)),
                'dept_name': dept_name,
                'startday_name': ('startday'+str(i)),
                'startday_id': ('startday'+str(i)),
                'startday': startday,
                'endday_name': ('endday'+str(i)),
                'endday_id': ('endday'+str(i)),
                'endday': "9999-12-31",
                'row': i,
            })
        dept_attribute.update({"dept_name": list_dept})  # đặt giá trị cho input khi render

        flag_test = str(request.POST.get('flag_test', ''))
        if len(err_string) == 0 and flag_test == "0":
            # Nếu không có lỗi và bấm button Lưu (flag_test = "0") thì lưu vào database
            # execute_sql(query_insert)
            for d in list_dept:
                # a = d["dept_name"]
                dp = Department(dept_name=d["dept_name"], is_active=1)
                dp.save()
                deptid = dp.dept_id
                sid = transaction.savepoint()
                try:
                    dc = DeptOfCompany(company_id=company_id, dept_id=deptid, startday=d["startday"], endday=d["endday"])
                    dc.save()
                    transaction.savepoint_commit(sid)
                except IntegrityError:
                    # Nếu xảy ra ngoại lệ thì rollback data vừa ghi vào database
                    transaction.savepoint_rollback(sid)

            return HttpResponseRedirect('/comp/add_dept_success/')
        else:
            dept_attribute.update({'error_message': err_string})
            dept_attribute.update({'comp': get_company()})
         
            return render(request, 'company/dept_new.html', dept_attribute)
    else:
        return render(request, 'company/dept_new.html')


def add_dept_success(request):
    return render(request, 'company/dept_list.html', {'dept': get_dept()})


def subdept(request):
    list_subdept = [{
        'sdn_name': 'subdept_name1', 'sdn_id': 'subdept_name1', 'subdept_name': "",
        'startday_name': 'startday1', 'startday_id': 'startday1', 'startday': "",
        'endday_name': 'endday1', 'endday_id': 'endday1', 'endday': "9999-12-31",
        'row': 1
    }]
    subdept_attribute = {
        'dept': get_dept(),
        'comp': get_company(),
        'subdept': list_subdept,
    }
    return render(request, 'company/subdept_new.html', subdept_attribute)


@transaction.atomic
def add_subdept(request):
    request_method = request.method
    print('request_method = ' + request_method)

    if request_method == 'POST':
        # query_insert = ""
        line = 1
        subdept_attribute = {}
        err_string = ""

        company_id = request.POST.get('company', '')
        subdept_attribute.update({"company_choose": str(company_id)})  # đặt giá trị cho input khi render
        if len(company_id) == 0:
            err_string += "<a href=\"#company\" class=\"err_string\">" + str(line) + ". Chưa chọn công ty!</a><br/>"
            line += 1

        dept_id = request.POST.get('dept', '')
        subdept_attribute.update({"dept_choose": int(dept_id)})  # đặt giá trị cho input khi render
        if len(dept_id) == 0:
            err_string += "<a href=\"#dept\" class=\"err_string\">" + str(line) + ". Chưa chọn phòng ban</a><br/>"
            line += 1

        j = 1
        count_subdept_name = request.POST.get('count_subdept_name', '')
        # đặt giá trị cho input khi render
        subdept_attribute.update({"count_subdept_name": str(count_subdept_name)})
        list_subdept = []
        for i in range(j, int(count_subdept_name) + 1):
            subdept_name = request.POST.get('subdept_name' + str(i), '')
            if len(subdept_name) == 0:
                err_string += "<a href=\"#subdept_name\" class=\"err_string\"" + str(i) + "\">" \
                              + str(line) + ". Tên bộ phận " + str(i) + " không được để trống!</a><br/>"
            line += 1
            startday = request.POST.get('startday' + str(i), '')
            if len(startday) == 0:
                err_string += "<a href=\"#startday\" class=\"err_string\"" + str(i) + "\">" \
                              + str(line) + ". Ngày bắt đầu " + str(i) + " không được để trống!></a><br/>"
            line += 1

            """
            endday = request.POST.get('endday' + str(i), '')
            query_insert += " INSERT INTO gpm_hrms_data.comp_subdepartment" \
                            "(company_id, dept_id, subdept_name, startday, endday)" \
                            " VALUES (\'" \
                            + company_id + "\', \'" \
                            + dept_id + "\', \'" \
                            + subdept_name + "\', \'" \
                            + startday + "\', \'" \
                            + "9999-12-31\');"
            """
            list_subdept.append({
                'sdn_name': ('subdept_name' + str(i)), 'sdn_id': ('subdept_name' + str(i)), 'subdept_name': subdept_name,
                'startday_name': ('startday' + str(i)), 'startday_id': ('startday' + str(i)), 'startday': startday,
                'endday_name': ('endday' + str(i)), 'endday_id': ('endday' + str(i)), 'endday': "9999-12-31",
                'row': i
            })
        subdept_attribute.update({"subdept": list_subdept})  # đặt giá trị cho input khi render
        # Insert data
        flag_test = str(request.POST.get('flag_test', ''))
        if len(err_string) == 0 and flag_test == "0":
            # Nếu không có lỗi và bấm button Lưu (flag_test = "save") thì lưu vào database
            # execute_sql(query_insert)
            for d in list_subdept:
                # a = d["dept_name"]
                sdp = SubDepartment(subdept_name=d["subdept_name"], is_active=1)
                sdp.save()
                subdeptid = sdp.subdept_id
                sid = transaction.savepoint()
                try:
                    # insert Bộ phận thuộc Phòng/ban vào bảng SubdeptOfDept
                    dc = SubdeptOfDept(dept_id=dept_id, subdept_id=subdeptid, startday=d["startday"], endday=d["endday"])
                    dc.save()
                    transaction.savepoint_commit(sid)
                except IntegrityError:
                    # Có lỗi khi insert thì rollback từ vị trí [sid = transaction.savepoint()]
                    transaction.savepoint_rollback(sid)
            return HttpResponseRedirect('/comp/add_subdept_success/')
        else:
            subdept_attribute.update({'error_message': err_string})
            subdept_attribute.update({'comp': get_company()})
            subdept_attribute.update({'dept': get_dept()})

            return render(request, 'company/subdept_new.html', subdept_attribute)
    else:
        return render(request, 'company/subdept_list.html')


def add_subdept_success(request):
    return render(request, 'company/subdept_list.html', {'subdept': get_subdept()})


def home_page(request):
    return render(request, 'index.html')
