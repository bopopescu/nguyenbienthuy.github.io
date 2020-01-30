from django.db import models

# Create your models here.


class Company(models.Model):
    company_id = models.CharField(primary_key=True, max_length=8)
    company_name = models.TextField()
    company_short_name = models.TextField(null=True)
    is_active = models.BooleanField()


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.dept_name


class SubDepartment(models.Model):
    subdept_id = models.AutoField(primary_key=True)
    subdept_name = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.subdept_name


class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=50)


class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    certificate_code = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_tax = models.CharField(max_length=20)
    cert_day = models.DateTimeField()
    cert_place = models.TextField()
    company_phone = models.CharField(max_length=20)
    company_fax = models.CharField(max_length=20)
    company_address = models.TextField()
    company_email = models.CharField(max_length=50)
    startday = models.DateTimeField()
    endday = models.DateTimeField()


class DeptOfCompany(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    startday = models.DateTimeField()
    endday = models.DateTimeField()


class SubdeptOfDept(models.Model):
    id = models.AutoField(primary_key=True)
    subdept = models.ForeignKey(SubDepartment, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    startday = models.DateTimeField()
    endday = models.DateTimeField()
