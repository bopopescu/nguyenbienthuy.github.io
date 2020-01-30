from django.core.serializers import json
from django.views.generic.edit import ModelFormMixin
from search_views.search import SearchListView

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers.json import DjangoJSONEncoder
import json as simplejson

from hrms.forms import *
from hrms.models import *

from mymodule.cnn_employee import *
from mymodule.err_trap import *
# Rollback database
from django.db import IntegrityError, transaction

# FormView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def hrms_page(request):
    list_acc = [{'an_name': 'account_number1', 'an_id': 'account_number1', 'account_number': "",
                 'bn_name': 'bank_name1', 'bn_id': 'bank_name1', 'bank_name': "",
                 'ba_name': 'bank_address1', 'ba_id': 'bank_address1', 'bank_address': "", 'row': 1}]

    init_attribute = {
        'count_address': 1,
        'address': [{'name': 'address1', 'id': 'address1', 'address': "", 'row': 1}],
        'phone_number': [{'name': 'phone_number1', 'id': 'phone_number1', 'phone_number': "", 'row': 1}],
        'emp_email': [{'name': 'emp_email1', 'id': 'emp_email1', 'emp_email': "", 'row': 1}],
        "account_number": list_acc,
        'selected_idplace': "7600",
        'selected_country': "084",
        'selected_idname': "0001",
    }
    return render(request, 'hrms/employee/employee_new.html', init_attribute)


def employee_new(request):
    request_method = request.method
    print('request_method = ' + request_method)

    if request_method == 'POST':
        err_string = ""
        line = 1
        emp_attribute = {}

        # add Employee
        # ===========================================================================================================
        # CIF
        emp_cif = request.POST.get('cif', '')
        # emp_cif='3979'
        emp_attribute.update({'cif': str(emp_cif)})  # đặt giá trị cho input khi render
        if len(emp_cif) == 0:
            err_string += get_err_msg_html(idname="#cif", line=line, msg="Mã cif không hợp lệ")
            line += 1

        # Họ tên
        emp_fullname = request.POST.get('fullname', '')
        emp_attribute.update({"fullname": str(emp_fullname)})  # đặt giá trị cho input khi render
        if len(emp_fullname) == 0:
            err_string += get_err_msg_html(idname="#fullname", line=line, msg="Họ tên không được để trống")
            line += 1
        # Giới tính
        emp_gender = request.POST.get('gender', '')
        emp_attribute.update({"selected_gender": str(emp_gender)})  # đặt giá trị cho input khi render
        if len(emp_gender) == 0:
            err_string += get_err_msg_html(idname="#gender", line=line, msg="Giới tính không được để trống")
            line += 1
        # Ngày sinh
        emp_birthday = request.POST.get('birthday', '')
        emp_attribute.update({"birthday": str(emp_birthday)})  # đặt giá trị cho input khi render
        if len(emp_birthday) == 0:
            err_string += get_err_msg_html(idname="#birthday", line=line, msg="Ngày sinh không được để trống")
            line += 1

        # add IdentityDocument
        # ===========================================================================================================
        # Loại giấy
        code_place_of_id = request.POST.get('idname', '')
        emp_attribute.update({"selected_idname": str(code_place_of_id)})  # đặt giá trị cho input khi render
        if len(code_place_of_id) == 0:
            err_string += get_err_msg_html(idname="#id_name", line=line, msg="Chưa chọn loại giấy tờ tùy thân")
            line += 1
        # Số CMND/CCCD (id)
        emp_id = request.POST.get('emp_id', '')
        emp_attribute.update({"emp_id": str(emp_id)})  # đặt giá trị cho input khi render
        if len(emp_id) == 0:
            err_string += get_err_msg_html(idname="#emp_id", line=line, msg="Số giấy tờ tùy thân không được để trống")
            line += 1
        # Mã nơi cấp CMND/CCCD
        place_of_identification = request.POST.get('place_of_identification', '')
        emp_attribute.update({"selected_idplace": str(place_of_identification)})  # đặt giá trị cho input khi render
        if len(place_of_identification) == 0:
            err_string += get_err_msg_html(idname="#place_of_identification", line=line, msg="Chưa chọn nơi cấp")
            line += 1
        # Ngày cấp CMND/CCCD/Hộ chiếu
        id_startday = request.POST.get('id_startday', '')
        emp_attribute.update({"id_startday": str(id_startday)})  # đặt giá trị cho input khi render
        if len(id_startday) == 0:
            err_string += get_err_msg_html(idname="#id_startday", line=line, msg="Chưa chọn ngày cấp")
            line += 1
        # Dân tộc
        people_code = request.POST.get('people', '')
        emp_attribute.update({"people_choose": str(people_code)})  # đặt giá trị cho input khi render
        if len(people_code) == 0:
            err_string += get_err_msg_html(idname="#people", line=line, msg="Chưa chọn dân tộc")
            line += 1
        # Quốc tịch
        nation_id = request.POST.get('nation', '')
        emp_attribute.update({"selected_country": str(nation_id)})  # đặt giá trị cho input khi render
        if len(nation_id) == 0:
            err_string += get_err_msg_html(idname="#nation", line=line, msg="Chưa chọn quốc tịch")
            line += 1

        # add EmployeeAddress
        # ===========================================================================================================
        j = 1
        countaddress = request.POST.get('count_address', '')
        emp_attribute.update({"count_address": str(countaddress)})  # đặt giá trị cho input khi render
        list_address = []
        for i in range(j, int(countaddress)+1):
            emp_address = request.POST.get('address'+str(i), '')
            list_address.append({'name': ('address'+str(i)),
                                 'id': ('address'+str(i)),
                                 'address': emp_address,
                                 'row': i})
            if len(emp_address) == 0:
                err_string += get_err_msg_html(idname="#address" + str(i), line=line,
                                               msg="Địa chỉ " + str(i) + " không được để trống")
                line += 1

        emp_attribute.update({"address": list_address})  # đặt giá trị cho input khi render

        # add EmployeePhone
        j = 1
        countphone = request.POST.get('count_phone', '')
        emp_attribute.update({"count_phone": str(countphone)})  # đặt giá trị cho input khi render
        list_phone = []
        for i in range(j, int(countphone)+1):
            emp_phone = request.POST.get('phone_number'+str(i), '')
            list_phone.append({'name': ('phone_number'+str(i)),
                               'id': ('phone_number'+str(i)),
                               'phone_number': emp_phone,
                               'row': i})
            if len(emp_phone) == 0:
                err_string += get_err_msg_html(idname="#phone_number" + str(i), line=line,
                                               msg="Số điện thoại " + str(i) + " không được để trống")
                line += 1
        emp_attribute.update({"phone_number": list_phone})  # đặt giá trị cho input khi render

        # add Email
        j = 1
        countemail = request.POST.get('count_email', '')
        emp_attribute.update({"count_email": str(countemail)})  # đặt giá trị cho input khi render
        list_email = []
        for i in range(j, int(countemail)+1):
            emp_email = request.POST.get('emp_email'+str(i), '')
            list_email.append({'name': ('emp_email'+str(i)),
                               'id': ('emp_email'+str(i)),
                               'emp_email': emp_email,
                               'row': i})
            if len(emp_email) == 0:
                err_string += get_err_msg_html(idname="#emp_email" + str(i), line=line,
                                               msg="Email " + str(i) + " không được để trống")
                line += 1
        emp_attribute.update({"emp_email": list_email})  # đặt giá trị cho input khi render

        # add EmployeeBankAccount
        j = 1
        count_account = request.POST.get('count_account_number', '')
        emp_attribute.update({"count_account_number": str(count_account)})  # đặt giá trị cho input khi render
        list_acc = []
        for i in range(j, int(count_account)+1):
            acc_number = request.POST.get('account_number'+str(i), '')
            if len(acc_number) == 0:
                err_string += get_err_msg_html(idname="#account_number" + str(i), line=line,
                                               msg="Số tài khoản " + str(i) + " không được để trống")
                line += 1
            bankname = request.POST.get('bank_name'+str(i), '')
            if len(bankname) == 0:
                err_string += get_err_msg_html(idname="#bank_name" + str(i), line=line,
                                               msg="Tên ngân hàng " + str(i) + " không được để trống")
                line += 1
            bankaddress = request.POST.get('bank_address'+str(i), '')      
            list_acc.append({
                'an_name': ('account_number'+str(i)), 'an_id': ('account_number'+str(i)), 'account_number': acc_number,
                'bn_name': ('bank_name'+str(i)), 'bn_id': ('bank_name'+str(i)), 'bank_name': bankname,
                'ba_name': ('bank_address'+str(i)), 'ba_id': ('bank_address'+str(i)), 'bank_address': bankaddress,
                'row': i})      
        emp_attribute.update({"account_number": list_acc})  # đặt giá trị cho input khi render
        
        # add Positions of Employee
        position_id = request.POST.get('position_id', '')
        emp_attribute.update({"position_id": str(position_id)})  # đặt giá trị cho input khi render
        if len(position_id) == 0:
            err_string += get_err_msg_html(idname="#position_id", line=line, msg="Chức danh không được để trống")
            line += 1
        startday = request.POST.get('startday', '')
        emp_attribute.update({"startday": str(startday)})  # đặt giá trị cho input khi render
        if len(startday) == 0:
            err_string += get_err_msg_html(idname="#startday", line=line, msg="Ngày bắt đầu chức danh chưa nhập")
            line += 1
        subdept = request.POST.get('subdept', '')  # Có thể nhận giá trị rỗng
        emp_attribute.update({"selected_subdept": int(subdept)})  # đặt giá trị cho input khi render
        selected_dept = request.POST.get('dept', '')

        emp_attribute.update({"selected_dept": int(selected_dept)})  # đặt giá trị cho input khi render

        company_id = request.POST.get('company', '')  # Có thể nhận giá trị rỗng
        emp_attribute.update({"selected_company": str(company_id)})  # đặt giá trị cho input khi render

        # add Dept_Of_Company
        if len(err_string) == 0:
            # check whether user account exist or not.
            aa = get_employee(cif=emp_cif)
            # if employee do not exist.
            if not aa:
                # create employee and return the user object.
                # insert Employee
                emp = Employee(cif=emp_cif, fullname=emp_fullname, birthday=emp_birthday, gender_id=emp_gender)
                emp.save()
                sid = transaction.savepoint()
                try:
                    # insert IdentityDocument
                    id_doc = IdentityDocument(cif_id=emp_cif, id=emp_id, startday=id_startday, endday='9999-12-31',
                                              people_id=people_code, nation_id=nation_id,
                                              id_name_code_id=code_place_of_id, place_id=place_of_identification)
                    id_doc.save()

                    # insert Address
                    for ea in list_address:
                        ea_add = EmployeeAddress(cif_id=emp_cif, address=ea['address'], address_index=ea['row'],
                                                 startday=startday, endday='9999-12-31')
                        ea_add.save()
                    # insert Address
                    for ep in list_phone:
                        ep_ph = EmployeePhone(cif_id=emp_cif, phone_number=ep['phone_number'],
                                              phone_number_index=ep['row'])
                        ep_ph.save()
                    # insert Email
                    for ee in list_email:
                        ee_em = EmployeeEmail(cif_id=emp_cif, email=ee['email'], email_index=ee['row'])
                        ee_em.save()
                    # insert EmployeeBankAccount
                    for eba in list_acc:
                        acc = EmployeeBankAccount(cif_id=emp_cif, account_number=eba['account_number'],
                                                  bank_name=eba['bank_name'], bank_address=eba['bank_address'],
                                                  account_number_index=eba['row'])
                        acc.save()
                    # insert EmployeePosition
                    emp_pos = EmployeePosition(cif_id=emp_cif, position_id=position_id,
                                               subdept_id=subdept, dept_id=selected_dept, company_id=company_id)
                    emp_pos.save()

                    transaction.savepoint_commit(sid)
                except IntegrityError:
                    transaction.savepoint_rollback(sid)

                response = HttpResponseRedirect('/hrms/employee_success/')
                # set cif value in session.
                request.session['emp_cif'] = emp_cif
                return response
            else:
                error_json = {'error_message': emp_cif + ' is exist'}
                return render(request, 'hrms/employee/employee_new.html', error_json)
        else:            
            emp_attribute.update({'error_message': err_string})
            return render(request, 'hrms/employee/employee_new.html', emp_attribute)
    else:
        return render(request, 'hrms/employee/employee_list.html')


def employee_success(request):
    # get user name, password, email value from session.
    # emp_cif = request.session.get('emp_cif','')
    # emp_fullname = request.session.get('emp_fullname', '')
    # pass user_name, user_password and user_email to display web page.
    emp = get_employee()
    # emp = Employee.objects.raw("SELECT * FROM hrms_employee WHERE cif=\'11111112\'")
    return render(request, 'hrms/employee/employee_list.html', {'emp': emp})


def edit_success(request):
    # code here
    emp = get_employee()
    return render(request, 'hrms/employee/employee_list.html', {'emp': emp})


#################################################################################################
# Giới tính
class GenderListView(ListView):
    model = Gender
    template_name = 'hrms/Gender/gender_view.html'
    context_object_name = 'gender'


class GenderCreateView(CreateView):
    model = Gender
    form_class = GenderForm
    template_name = 'hrms/Gender/gender_new.html'
    success_url = reverse_lazy('gender_list')


class GenderUpdateView(UpdateView):
    model = Gender
    form_class = GenderUpdateForm
    template_name = 'hrms/Gender/gender_update.html'
    success_url = reverse_lazy('gender_list')


class GenderDeleteView(SuccessMessageMixin, DeleteView):
    model = Gender
    success_url = reverse_lazy('gender_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View CurrencyForm
class CurrencyListView(SearchListView):
    model = Currency
    paginate_by = 10
    template_name = 'hrms/Currency/currency_view.html'
    form_class = CurrencySearchForm
    filter_class = CurrencyFilter
    context_object_name = 'currency'


class CurrencyCreateView(CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'hrms/Currency/currency_new.html'
    success_url = reverse_lazy('currency_list')


class CurrencyUpdateView(UpdateView):
    model = Currency
    form_class = CurrencyUpdateForm
    template_name = 'hrms/Currency/currency_update.html'
    success_url = reverse_lazy('currency_list')


class CurrencyDeleteView(SuccessMessageMixin, DeleteView):
    model = Currency
    success_url = reverse_lazy('currency_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View CurrencyForm
class PlaceOfIdentificationSearchListView(SearchListView):
    model = PlaceOfIdentification
    paginate_by = 10
    template_name = 'hrms/PlaceOfId/place_id_view.html'
    form_class = PlaceOfIdentificationSearchForm
    filter_class = PlaceOfIdentificationFilter
    context_object_name = 'place_ids'


class PlaceOfIdentificationCreateView(CreateView):
    model = PlaceOfIdentification
    form_class = PlaceOfIdentificationForm
    template_name = 'hrms/PlaceOfId/place_id_new.html'
    success_url = reverse_lazy('place_id_list')


class PlaceOfIdentificationUpdateView(UpdateView):
    model = PlaceOfIdentification
    form_class = PlaceOfIdentificationUpdateForm
    template_name = 'hrms/PlaceOfId/place_id_update.html'
    success_url = reverse_lazy('place_id_list')


class PlaceOfIdentificationDeleteView(SuccessMessageMixin, DeleteView):
    model = PlaceOfIdentification
    success_url = reverse_lazy('place_id_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View CurrencyForm
class IdNameListView(SearchListView):
    model = IdName
    paginate_by = 10
    template_name = 'hrms/IdName/id_name_view.html'
    form_class = IdNameSearchForm
    filter_class = IdNameFilter
    context_object_name = 'idnames'


class IdNameCreateView(CreateView):
    model = IdName
    form_class = IdNameForm
    template_name = 'hrms/IdName/id_name_new.html'
    success_url = reverse_lazy('idname_list')


class IdNameUpdateView(UpdateView):
    model = IdName
    form_class = IdNameUpdateForm

    template_name = 'hrms/IdName/id_name_update.html'
    success_url = reverse_lazy('idname_list')


class IdNameDeleteView(SuccessMessageMixin, DeleteView):
    model = IdName
    success_url = reverse_lazy('idname_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View PeopleForm
class PeopleListView(SearchListView):
    model = People
    paginate_by = 10
    template_name = 'hrms/People/view.html'
    form_class = PeopleSearchForm
    filter_class = PeopleFilter
    context_object_name = 'people'


class PeopleCreateView(CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'hrms/People/new.html'
    success_url = reverse_lazy('people_list')


class PeopleUpdateView(UpdateView):
    model = People
    form_class = PeopleForm
    template_name = 'hrms/People/update.html'
    success_url = reverse_lazy('people_list')


class PeopleDeleteView(SuccessMessageMixin, DeleteView):
    model = People
    success_url = reverse_lazy('people_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View NationForm
class NationListView(SearchListView):
    model = Nation
    paginate_by = 2
    template_name = 'hrms/Nation/view.html'
    context_object_name = 'nation'
    form_class = NationSearchForm
    filter_class = NationFilter


class NationCreateView(CreateView):
    model = Nation
    form_class = NationForm
    template_name = 'hrms/Nation/new.html'
    success_url = reverse_lazy('nation_list')


class NationUpdateView(UpdateView):
    model = Nation
    form_class = NationUpdateForm
    template_name = 'hrms/Nation/update.html'
    success_url = reverse_lazy('nation_list')


class NationDeleteView(SuccessMessageMixin, DeleteView):
    model = Nation
    success_url = reverse_lazy('nation_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View MealMoney
class MealMoneyListView(SearchListView):
    model = MealMoney
    paginate_by = 10
    template_name = 'hrms/MealMoney/view.html'
    context_object_name = 'mealmoney'
    form_class = MealMoneySearchForm
    filter_class = MealMoneyFilter


class MealMoneyCreateView(CreateView):
    model = MealMoney
    form_class = MealMoneyForm
    template_name = 'hrms/MealMoney/new.html'
    success_url = reverse_lazy('mealmoney_list')


class MealMoneyUpdateView(UpdateView):
    model = MealMoney
    form_class = MealMoneyUpdateForm
    template_name = 'hrms/MealMoney/update.html'
    success_url = reverse_lazy('mealmoney_list')


class MealMoneyDeleteView(SuccessMessageMixin, DeleteView):
    model = MealMoney
    success_url = reverse_lazy('mealmoney_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View SalaryBasic
class SalaryBasicListView(SearchListView):
    model = SalaryBasic
    paginate_by = 10
    template_name = 'hrms/SalaryBasic/view.html'
    context_object_name = 'salarybasic'
    form_class = SalaryBasicSearchForm
    filter_class = SalaryBasicFilter


class SalaryBasicCreateView(CreateView):
    model = SalaryBasic
    form_class = SalaryBasicForm
    template_name = 'hrms/SalaryBasic/new.html'
    success_url = reverse_lazy('salarybasic_list')


class SalaryBasicUpdateView(UpdateView):
    model = SalaryBasic
    form_class = SalaryBasicUpdateForm
    template_name = 'hrms/SalaryBasic/update.html'
    success_url = reverse_lazy('salarybasic_list')


class SalaryBasicDeleteView(SuccessMessageMixin, DeleteView):
    model = SalaryBasic
    success_url = reverse_lazy('salarybasic_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View SalaryBasicPlus
class SalaryBasicPlusListView(SearchListView):
    model = SalaryBasicPlus
    paginate_by = 10
    template_name = 'hrms/SalaryBasicPlus/view.html'
    context_object_name = 'salarybasic_plus'
    form_class = SalaryBasicPlusSearchForm
    filter_class = SalaryBasicPlusFilter


class SalaryBasicPlusCreateView(CreateView):
    model = SalaryBasicPlus
    form_class = SalaryBasicPlusForm
    template_name = 'hrms/SalaryBasicPlus/new.html'
    success_url = reverse_lazy('salarybasic_plus_list')


class SalaryBasicPlusUpdateView(UpdateView):
    model = SalaryBasicPlus
    form_class = SalaryBasicPlusUpdateForm
    template_name = 'hrms/SalaryBasicPlus/update.html'
    success_url = reverse_lazy('salarybasic_plus_list')


class SalaryBasicPlusDeleteView(SuccessMessageMixin, DeleteView):
    model = SalaryBasicPlus
    success_url = reverse_lazy('salarybasic_plus_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View SalaryScale
class SalaryScaleListView(SearchListView):
    model = SalaryScale
    paginate_by = 10
    template_name = 'hrms/SalaryScale/view.html'
    context_object_name = 'salaryscale'
    form_class = SalaryScaleSearchForm
    filter_class = SalaryScaleFilter


class SalaryScaleCreateView(CreateView):
    model = SalaryScale
    form_class = SalaryScaleForm
    template_name = 'hrms/SalaryScale/new.html'
    success_url = reverse_lazy('salaryscale_list')


class SalaryScaleUpdateView(UpdateView):
    model = SalaryScale
    form_class = SalaryScaleUpdateForm
    template_name = 'hrms/SalaryScale/update.html'
    success_url = reverse_lazy('salaryscale_list')


class SalaryScaleDeleteView(SuccessMessageMixin, DeleteView):
    model = SalaryScale
    success_url = reverse_lazy('salaryscale_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View Insurance
class InsuranceListView(SearchListView):
    model = Insurance
    paginate_by = 10
    template_name = 'hrms/Insurance/view.html'
    context_object_name = 'insurance'
    form_class = InsuranceSearchForm
    filter_class = InsuranceFilter


class InsuranceCreateView(CreateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'hrms/Insurance/new.html'
    success_url = reverse_lazy('insurance_list')


class InsuranceUpdateView(UpdateView):
    model = Insurance
    form_class = InsuranceUpdateForm
    template_name = 'hrms/Insurance/update.html'
    success_url = reverse_lazy('insurance_list')


class InsuranceDeleteView(SuccessMessageMixin, DeleteView):
    model = Insurance
    success_url = reverse_lazy('insurance_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View Union
class UnionListView(SearchListView):
    model = Union
    paginate_by = 10
    template_name = 'hrms/Union/view.html'
    context_object_name = 'union'
    form_class = UnionSearchForm
    filter_class = UnionFilter


class UnionCreateView(CreateView):
    model = Union
    form_class = UnionForm
    template_name = 'hrms/Union/new.html'
    success_url = reverse_lazy('union_list')


class UnionUpdateView(UpdateView):
    model = Union
    form_class = UnionUpdateForm
    template_name = 'hrms/Union/update.html'
    success_url = reverse_lazy('union_list')


class UnionDeleteView(SuccessMessageMixin, DeleteView):
    model = Union
    success_url = reverse_lazy('union_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View WorkingTime
class WorkingTimeListView(SearchListView):
    model = WorkingTime
    paginate_by = 10
    template_name = 'hrms/WorkingTime/view.html'
    context_object_name = 'workingtime'
    form_class = WorkingTimeSearchForm
    filter_class = WorkingTimeFilter


class WorkingTimeCreateView(CreateView):
    model = WorkingTime
    form_class = WorkingTimeForm
    template_name = 'hrms/WorkingTime/new.html'
    success_url = reverse_lazy('workingtime_list')


class WorkingTimeUpdateView(UpdateView):
    model = WorkingTime
    form_class = WorkingTimeUpdateForm
    template_name = 'hrms/WorkingTime/update.html'
    success_url = reverse_lazy('workingtime_list')


class WorkingTimeDeleteView(SuccessMessageMixin, DeleteView):
    model = WorkingTime
    success_url = reverse_lazy('workingtime_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View DaysOfWeek
class DaysOfWeekListView(SearchListView):
    model = DaysOfWeek
    paginate_by = 10
    template_name = 'hrms/DaysOfWeek/view.html'
    context_object_name = 'days'
    form_class = DaysOfWeekSearchForm
    filter_class = DaysOfWeekFilter


class DaysOfWeekCreateView(CreateView):
    model = DaysOfWeek
    form_class = DaysOfWeekForm
    template_name = 'hrms/DaysOfWeek/new.html'
    success_url = reverse_lazy('days_list')


class DaysOfWeekUpdateView(UpdateView):
    model = DaysOfWeek
    form_class = DaysOfWeekUpdateForm
    template_name = 'hrms/DaysOfWeek/update.html'
    success_url = reverse_lazy('days_list')


class DaysOfWeekDeleteView(SuccessMessageMixin, DeleteView):
    model = DaysOfWeek
    success_url = reverse_lazy('days_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View WorkingGroup
class WorkingGroupListView(SearchListView):
    model = WorkingGroup
    paginate_by = 10
    template_name = 'hrms/WorkingGroup/view.html'
    context_object_name = 'workinggroup'
    form_class = WorkingGroupSearchForm
    filter_class = WorkingGroupFilter


class WorkingGroupCreateView(CreateView):
    model = WorkingGroup
    form_class = WorkingGroupForm
    template_name = 'hrms/WorkingGroup/new.html'
    success_url = reverse_lazy('workinggroup_list')


class WorkingGroupUpdateView(UpdateView):
    model = WorkingGroup
    form_class = WorkingGroupUpdateForm
    template_name = 'hrms/WorkingGroup/update.html'
    success_url = reverse_lazy('workinggroup_list')


class WorkingGroupDeleteView(SuccessMessageMixin, DeleteView):
    model = WorkingGroup
    success_url = reverse_lazy('workinggroup_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View WorkingGroup
class WorkSchedulesListView(SearchListView):
    model = WorkSchedules
    paginate_by = 10
    template_name = 'hrms/WorkSchedules/view.html'
    context_object_name = 'workschedules'
    form_class = WorkSchedulesSearchForm
    filter_class = WorkSchedulesFilter


class WorkSchedulesCreateView(CreateView):
    model = WorkSchedules
    form_class = WorkSchedulesForm
    template_name = 'hrms/WorkSchedules/new.html'
    success_url = reverse_lazy('workschedules_list')


class WorkSchedulesUpdateView(UpdateView):
    model = WorkSchedules
    form_class = WorkSchedulesUpdateForm
    template_name = 'hrms/WorkSchedules/update.html'
    success_url = reverse_lazy('workschedules_list')


class WorkSchedulesDeleteView(SuccessMessageMixin, DeleteView):
    model = WorkSchedules
    success_url = reverse_lazy('workschedules_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################################################################################################
# View LaborContract
class LaborContractListView(SearchListView):
    model = LaborContract
    paginate_by = 10
    template_name = 'hrms/LaborContract/view.html'
    context_object_name = 'laborcontracts'
    form_class = LaborContractSearchForm
    filter_class = LaborContractFilter


class LaborContractCreateView(CreateView):
    model = LaborContract
    form_class = LaborContractForm
    template_name = 'hrms/LaborContract/new.html'
    success_url = reverse_lazy('laborcontract_list')


class LaborContractUpdateView(UpdateView):
    model = LaborContract
    form_class = LaborContractUpdateForm
    template_name = 'hrms/LaborContract/update.html'
    success_url = reverse_lazy('laborcontract_list')


class LaborContractDeleteView(SuccessMessageMixin, DeleteView):
    model = LaborContract
    success_url = reverse_lazy('laborcontract_list')

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
