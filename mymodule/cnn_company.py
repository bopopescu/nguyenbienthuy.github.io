from mymodule.connutils import *
# from mymodule.fun_assistant import *
from comp.models import Department, SubDepartment, SubdeptOfDept
from django.shortcuts import render


def get_company(company_id=None):
    comp = []
    if company_id is None:
        query_sql = """SELECT a.company_id, company_name, company_short_name, certificate_id,
                              certificate_code, code_tax, cert_day, cert_place, company_phone, 
                              company_fax, company_address, company_email, startday, endday 
                       FROM comp_company a, comp_certificate b
                       WHERE a.company_id = b.company_id;"""
    else:
        query_sql = " SELECT a.company_id, company_name, company_short_name, certificate_id, " \
                    " certificate_code, code_tax, cert_day, cert_place, company_phone, " \
                    " company_fax, company_address, company_email, startday, endday " \
                    " FROM comp_company a, comp_certificate b " \
                    " WHERE (a.company_id = b.company_id) " \
                    " AND (a.company_id = \'" + str(company_id) + "\');"
    gdata = get_data(query_sql)
    for col in gdata:
        comp.append({"company_id": col[0],
                     "company_name": col[1],
                     "company_short_name": col[2],
                     "certificate_id": col[3],
                     "certificate_code": col[4],
                     "code_tax": col[5],
                     "cert_day": col[6],
                     "cert_place": col[7],
                     "company_phone": col[8],
                     "company_fax": col[9],
                     "company_address": col[10],
                     "company_email": col[11],
                     "startday": col[12],
                     "endday": col[13],
                     })
    return comp


def insert_company(company_id, company_name, company_short_name, certificate_code, code_tax, cert_day, cert_place,
                   company_phone, company_fax, company_address, company_email, startday, endday):
    # Thêm công ty mới
    query_sql = " INSERT INTO Comp_Company(company_id, company_name, company_short_name) " \
                " VALUES(\'" + company_id + "\', \'" + company_name + "\', \'" + company_short_name + "\');" + \
                " INSERT INTO Comp_Certificate(certificate_code, company_id, code_tax, cert_day, " \
                " cert_place, company_phone, company_fax, company_address, company_email, startday, endday) " \
                " VALUES(\'" + certificate_code + "\', \'" \
                + company_id + "\', \'" \
                + code_tax + "\', \'" \
                + cert_day + "\', \'" \
                + cert_place + "\', \'" \
                + company_phone + "\', \'" \
                + company_fax + "\', \'" \
                + company_address + "\', \'" \
                + company_email + "\', \'" \
                + startday + "\', \'" \
                + endday + "\');"
    return execute_sql(query_sql)


def get_dept(dept_id=None, company_id=None):
    dept = []
    if dept_id is None:
        query_sql = """SELECT a.company_id, company_name, b.dept_id, dept_name, startday, endday 
                       FROM comp_company a, comp_department b, comp_deptofcompany c
                       WHERE a.company_id = c.company_id
                       AND b.dept_id = c.dept_id;"""
    else:
        query_sql = " SELECT a.company_id, company_name, dept_id, dept_name, startday, endday" \
                    " FROM comp_company a, comp_department b " \
                    " WHERE (a.company_id = b.company_id) " \
                    " AND (a.company_id = \'" + str(company_id) + "\') " \
                    " AND (b.dept_id = \'" + str(dept_id) + "\');"
    gdata = get_data(query_sql)
    for col in gdata:
        dept.append({
            "company_id": col[0],
            "company_name": col[1],
            "dept_id": col[2],
            "dept_name": col[3],
            "startday": col[4],
            "endday": col[5],
        })
    return dept


def insert_dept(company_id, dept_name, startday, endday):
    # Thêm 1 phòng ban mới
    query_sql = " INSERT INTO comp_department(company_id, dept_name, startday, endday) " \
                " VALUES (\'" + company_id + "\', \'" \
                + dept_name + "\', \'" \
                + startday + "\', \'" \
                + endday + "\');"

    return execute_sql(query_sql)


def get_subdept(subdept_id=None, dept_id=None, company_id=None):
    subdept = []
    if subdept_id is None and dept_id is None and company_id is None:
        query_sql = """SELECT 
                            a.company_id,
                            a.company_name, 
                            b.dept_id, 
                            b.dept_name, 
                            d.subdept_id, 
                            d.subdept_name ,
                            e.startday, 
                            e.endday, 
                            d.is_active
                       FROM 
                            comp_company a,
                            comp_department b, 
                            comp_deptofcompany c,
                            comp_subdepartment d,
                            comp_subdeptofdept e
                       WHERE    a.company_id = c.company_id
                       AND      b.dept_id = c.dept_id
                       AND      b.dept_id = e.dept_id
                       AND      d.subdept_id = e.subdept_id;"""
        gdata = get_data(query_sql)
        for col in gdata:
            subdept.append({
                "company_id": col[0],
                "company_name": col[1],
                "dept_id": col[2],
                "dept_name": col[3],
                "subdept_id": col[4],
                "subdept_name": col[5],
                "startday": col[6],
                "endday": col[7],
                "is_active": col[8]
            })
    else:
        query_sql = " SELECT a.company_id, `company_name`, `dept_id`, `dept_name`, `startday`, `endday`" \
                    " FROM `gpm_hrms_data`.`comp_company` a, `gpm_hrms_data`.`comp_department` b " \
                    " WHERE (a.`company_id` = b.`company_id`) " \
                    " AND (a.`company_id` = \'" + str(company_id) + "\') " \
                    " AND (b.`dept_id` = \'" + str(dept_id) + "\');"
        gdata = get_data(query_sql)
        for col in gdata:
            subdept.append({
                "company_id": col[0],
                "company_name": col[1],
                "dept_id": col[2],
                "dept_name": col[3],
                "startday": col[4],
                "endday": col[5]
            })
    return subdept
