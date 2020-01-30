from django.db import models
# from django.urls import reverse_lazy

from comp import models as comp_models
# Create your models here.


# Giới tính
class Gender(models.Model):
    gender_id = models.CharField(max_length=1, primary_key=True)
    gender_name = models.CharField(max_length=20)

    def __str__(self):
        return self.gender_name


class Employee(models.Model):
    cif = models.CharField(max_length=8, primary_key=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    fullname = models.TextField()
    birthday = models.DateTimeField()


# Loại tiền
class Currency(models.Model):
    currency_id = models.CharField(max_length=3, primary_key=True)
    currency_name = models.CharField(max_length=30)

    def __str__(self):
        return self.currency_name


# Tiền ăn
class MealMoney(models.Model):
    mealmoney_id = models.AutoField(primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()


# Tiền lương tối thiểu
class SalaryBasic(models.Model):
    salary_basic_id = models.AutoField(primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    amount = models.FloatField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()
    designation = models.TextField(null=True)

    def __str__(self):
        return self.name


# Tỷ lệ lương tối thiểu tăng thêm
class SalaryBasicPlus(models.Model):
    salary_basic_plus_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    ratio = models.FloatField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()

    def __str__(self):
        return self.name


# Hệ số lương
class SalaryScale(models.Model):
    scale_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    scale = models.FloatField(default=0)
    startday = models.DateTimeField()
    endday = models.DateTimeField()

    def __str__(self):
        return self.name


# Tỷ lệ đóng BHXH, BHYT, BHTN
class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    # BHXH Người sử dụng lao động
    social_company = models.FloatField()
    # BH tai nạn lao động Bệnh nghề nghiệp (Cty đóng)
    social_tnld_bnn = models.FloatField()
    # BHXH Người lao động
    social_employee = models.FloatField()
    # BHYT Người sử dụng lao động
    health_company = models.FloatField()
    # BHYT Người lao động
    health_employee = models.FloatField()
    # BHTN Người sử dụng lao động
    unemployment_company = models.FloatField()
    # BHTN Người lao động
    unemployment_employee = models.FloatField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()
    # Theo văn bản
    designation = models.TextField(null=True)


# Tỷ lệ đóng Công đoàn
class Union(models.Model):
    union_id = models.AutoField(primary_key=True)
    ratio_company = models.FloatField()
    ratio_employee = models.FloatField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()
    # Theo văn bản
    designation = models.TextField(null=True)


class EmployeeAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address = models.TextField()
    startday = models.DateTimeField()
    endday = models.DateTimeField()
    address_index = models.IntegerField()  # Vị trí của từng địa chỉ khi nhập liệu (Khi Xóa thì = 0)

    class Meta:
        unique_together = ('cif', 'address_id')


class EmployeePhone(models.Model):
    phone_number_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    phone_number_index = models.IntegerField()  # Vị trí của từng số điện thoại khi nhập liệu (Khi Xóa thì = 0)

    class Meta:
        unique_together = ('cif', 'phone_number_id')


class EmployeeBankAccount(models.Model):
    bank_account_id = models.AutoField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    bank_name = models.TextField()
    bank_address = models.TextField()
    account_number_index = models.IntegerField()  # Vị trí của từng số TK NH khi nhập liệu (Khi Xóa thì = 0)

    class Meta:
        unique_together = ('cif', 'bank_account_id')


class EmployeeEmail(models.Model):
    email_id = models.AutoField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    email_index = models.IntegerField()  # Vị trí của từng email khi nhập liệu (Khi Xóa thì = 0)

    class Meta:
        unique_together = ('cif', 'email_id')


class EmployeePosition(models.Model):
    emp_position_id = models.AutoField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(comp_models.Positions, on_delete=models.CASCADE)
    subdept = models.ForeignKey(comp_models.SubDepartment, on_delete=models.CASCADE, null=True)
    dept = models.ForeignKey(comp_models.Department, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(comp_models.Company, on_delete=models.CASCADE)
    position_index = models.IntegerField(null=True)
    startday = models.DateTimeField()
    endday = models.DateTimeField()


# Nơi cấp CMND
class PlaceOfIdentification(models.Model):
    place_id = models.CharField(primary_key=True, max_length=4)
    place_of_identification = models.CharField(max_length=250)


# Loại giấy tờ tùy thân
class IdName(models.Model):
    id_name_code = models.CharField(primary_key=True, max_length=4)
    name_of_identification = models.CharField(max_length=250)


# Dân tộc
class People(models.Model):
    people_id = models.AutoField(primary_key=True)
    people_name = models.CharField(max_length=250)


# Quốc tịch
class Nation(models.Model):
    nation_id = models.CharField(primary_key=True, max_length=3)
    nation_name = models.CharField(max_length=250)


class IdentityDocument(models.Model):
    id_code = models.IntegerField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    place = models.ForeignKey(PlaceOfIdentification, on_delete=models.CASCADE)
    id_name_code = models.ForeignKey(IdName, on_delete=models.CASCADE)
    id = models.CharField(max_length=20)    
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    startday = models.DateTimeField()
    endday = models.DateTimeField()


# Thời gian làm việc
class WorkingTime(models.Model):
    workingtime_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " (" + str(self.starttime) + " - " + str(self.endtime) + ")"


# Các ngày trong tuần
class DaysOfWeek(models.Model):
    daysofweek_id = models.CharField(primary_key=True, max_length=1)
    dayname = models.CharField(max_length=50)

    def __str__(self):
        return self.dayname


# Nhóm thời gian làm việc
class WorkingGroup(models.Model):
    workinggroup_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Nhóm thời gian làm việc
class WorkSchedules(models.Model):
    workschedules_id = models.AutoField(primary_key=True)
    workingtime = models.ForeignKey(WorkingTime, on_delete=models.CASCADE)
    daysofweek = models.ManyToManyField(DaysOfWeek)
    workinggroup = models.ForeignKey(WorkingGroup, on_delete=models.CASCADE)


# Hợp đồng lao động
class LaborContract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    # Số hợp đồng, quyết định... (XXX/YY/HDLD | XXX/YY/QD-GD,... )
    contract_number = models.CharField(max_length=30)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(comp_models.Company, on_delete=models.CASCADE)
    dept = models.ForeignKey(comp_models.Department, on_delete=models.CASCADE, null=True)
    subdept = models.ForeignKey(comp_models.SubDepartment, on_delete=models.CASCADE, null=True)
    salary_basic = models.ForeignKey(SalaryBasic, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    # Phụ cấp thường xuyên
    salary_benefit = models.FloatField()
    # Hệ số lương
    scale = models.ForeignKey(SalaryScale, on_delete=models.CASCADE)
    # Loại phụ cấp tiền ăn trưa
    mealmoney = models.ForeignKey(MealMoney, on_delete=models.CASCADE)
    # Ngày hợp đồng
    contract_day = models.DateTimeField()
    # Ngày hiệu lực
    startday = models.DateTimeField()
    # Ngày thay đổi hệ số lương, tiền ăn, phụ cấp ...
    endday = models.DateTimeField()
    # Ngày hết hạn hợp đồng
    maturity_date = models.DateTimeField()
    # Thời hạn hợp đồng
    term = models.CharField(max_length=50)
    # Thuộc nhóm làm việc
    workinggroup = models.ForeignKey(WorkingGroup, on_delete=models.CASCADE)


class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    cif = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contract = models.ForeignKey(LaborContract, on_delete=models.CASCADE)
    salary_date = models.DateTimeField()
    salary_other = models.FloatField()
    salary_advance = models.FloatField()
    days_working = models.FloatField()
    days_unpaid_leave = models.FloatField()
    days_paid_leave = models.FloatField()
    days_annual_leave = models.FloatField()
    bonus = models.FloatField()
    kpi_point = models.FloatField()
    overtime = models.FloatField()
    tax_abatement = models.FloatField(null=True)