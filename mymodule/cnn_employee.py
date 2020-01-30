from mymodule.connutils import *


def get_employee(cif=None):
    employee = []
    if cif is None:
        query_sql = """SELECT cif, fullname, birthday, gender_name 
                       FROM hrms_employee a, hrms_gender b 
                       WHERE  a.gender_id = b.gender_id ORDER BY fullname;"""
        gdata = get_data(query_sql)
        for row in gdata:
            employee.append({"cif": row[0], "fullname": row[1], "birthday": row[2], "gender_name": row[3]})
    else:
        query_sql = " SELECT cif, fullname, gender_id, birthday FROM hrms_employee " \
                    " WHERE cif = '" + str(cif) + "';"
        gdata = get_data(query_sql)
        for row in gdata:
            employee.append({"cif": row[0], "fullname": row[1], "gender_id": row[2], "birthday": row[3]})
    return employee


def get_employee_working(start_day, end_day, company):
    employee = []
    query_sql = " SELECT a.cif, a.fullname,  "\
                " b.company_id, b.dept_name, "\
                " c.position_name,  "\
                " d.salary_scale_code, "\
                " e.salary_scale_name "\
                " FROM hrms_employee a, "\
                "      comp_department b, "\
                "      hrms_positions c, "\
                "      hrms_laborcontract d, "\
                "      hrms_salaryscale e "\
                " WHERE a.cif = c.cif "\
                " AND a.cif = d.cif "\
                " AND d.salary_scale_code = e.salary_scale_code "\
                " AND c.dept_id = b.dept_id "\
                " AND (\'" + start_day + "\' BETWEEN c.startday and c.endday " \
                " OR \'" + end_day + "\' BETWEEN c.startday and c.endday) "\
                " AND (\'" + start_day + "\' BETWEEN d.start_date and d.maturity_date " \
                " OR \'" + end_day + "\' BETWEEN d.start_date and d.maturity_date) "\
                " AND b.company_id = \'" + company + "\' "\
                " Group by c.position_name;"
    gdata = get_data(query_sql)
    for col in gdata:
        employee.append({
            "cif": col[0], 
            "fullname": col[1], 
            "company_id": col[2],
            "dept_name": col[3],
            "position_name": col[4],
        })
    return employee


def get_gender(gender_id=None):
    gender = []
    if gender_id is None:
        query_sql = "SELECT gender_id, gender_name FROM hrms_Gender ORDER BY gender_name;"
    else:
        query_sql = "SELECT gender_id, gender_name FROM hrms_Gender WHERE gender_id = '" \
                  + gender_id + "' ORDER BY gender_name;"
    gdata = get_data(query_sql)
    for row in gdata:
        gender.append({"gender_id": row[0], "gender_name": row[1]})
    # context = {'emp_gender':gender.fetchall()}
    return gender


def get_idname():
    id_name = []
    gdata = get_data("SELECT * FROM hrms_IdName ORDER BY name_of_identification DESC;")
    for row in gdata:
        id_name.append({"id_name_code": row[0], "name_of_identification": row[1]})
    return id_name


def get_place_of_identification():
    place_of_identification = []
    gdata = get_data("SELECT * FROM hrms_placeofidentification ORDER BY place_of_identification;")
    for row in gdata:
        place_of_identification.append({"code_place_of_id": row[0], "place_of_identification": row[1]})
    return place_of_identification


def get_people():
    people = []
    gdata = get_data("SELECT * FROM hrms_people ORDER BY people_name;")
    for row in gdata:
        people.append({"people_code": row[0], "people_name": row[1]})
    return people


def get_country():
    country = []
    gdata = get_data("SELECT nation_id, nation_name FROM hrms_nation ORDER BY nation_name;")
    for row in gdata:
        country.append({"nation_id": row[0], "nation_name": row[1]})
    return country


def get_subdepartment():
    subdepartment = []
    gdata = get_data("SELECT subdept_id, subdept_name FROM comp_subdepartment "
                     "WHERE is_active = 1 ORDER BY subdept_name;")
    for row in gdata:
        subdepartment.append({"subdept_id": row[0], "subdept_name": row[1]})
    return subdepartment


def get_department():
    department = []
    gdata = get_data("SELECT dept_id, dept_name FROM comp_department "
                     "WHERE is_active = 1 ORDER BY dept_name;")
    for row in gdata:
        department.append({"dept_id": row[0], "dept_name": row[1]})
    return department


def get_company():
    comp = []
    gdata = get_data("SELECT company_id, company_name FROM comp_company ORDER BY company_name;")
    for row in gdata:
        comp.append({"company_id": row[0], "company_name": row[1]})
    return comp


def get_mealmoney():
    mealmoney = []
    query_sql = "SELECT meal_money_code, meal_money_amount, currency_des, startday, endday " \
                "FROM hrms_mealmoney a, hrms_currency " \
                "WHERE a.currency_code = b.currency_code;"
    gdata = get_data(query_sql)
    for row in gdata:
        mealmoney.append({
           "meal_money_code": row[0],
           "meal_money_amount": row[1],
           "currency_des": row[2],
           "startday": row[3],
           "endday": row[4]
        })
    return mealmoney


def get_insurance(endday=None):
    insurance = []
    if endday is None:
        query_sql = """SELECT insurance_code, social_company, social_employee, health_company, health_employee,
                              unemployment_company, unemployment_employee, startday, endday, designation
                        FROM hrms_insurance;"""
    else:
        query_sql = " SELECT insurance_code, social_company, social_employee, health_company, health_employee," \
                    "        unemployment_company, unemployment_employee, startday, endday, designation " \
                    " FROM hrms_insurance " \
                    " WHERE endday = \'" + endday + "\';"
    gdata = get_data(query_sql)
    for col in gdata:
        insurance.append({
            "insurance_code": col[0],
            "social_company": col[1],
            "social_employee": col[2],
            "health_company": col[3],
            "health_employee": col[4],
            "unemployment_company": col[5],
            "unemployment_employee": col[6],
            "startday": col[7],
            "endday": col[8],
            "designation": col[9]
        })
    return insurance


def insert_insurance(social_company, social_employee, health_company, health_employee,
                     unemployment_company, unemployment_employee, startday, endday, designation):
    query_insert = " INSERT INTO hrms_insurance " \
                   " (social_company, social_employee, health_company, health_employee," \
                   " unemployment_company, unemployment_employee, startday, endday, designation) " \
                   " VALUES (\'" \
                   + social_company + "\', \'" \
                   + social_employee + "\', \'" \
                   + health_company + "\', \'" \
                   + health_employee + "\', \'" \
                   + unemployment_company + "\', \'" \
                   + unemployment_employee + "\', \'" \
                   + startday + "\', \'" \
                   + endday + "\', \'" \
                   + designation + "\');"
    return execute_sql(query_insert)


def update_insurance(insurance_code, social_company, social_employee, health_company, health_employee,
                     unemployment_company, unemployment_employee, startday, endday, designation):
    query_update = " UPDATE hrms_insurance " \
                   " SET social_company = \'" + social_company + "\', " \
                   " social_employee = \'" + social_employee + "\', " \
                   " health_company = \'" + health_company + "\', " \
                   " health_employee = \'" + health_employee + "\', " \
                   " unemployment_company = \'" + unemployment_company + "\', " \
                   " unemployment_employee = \'" + unemployment_employee + "\', " \
                   " startday = \'" + startday + "\'," \
                   " endday = \'" + endday + "\'," \
                   " designation = \'" + designation + "\'," \
                   " WHERE insurance_code = \'" + insurance_code + "\';"
    return execute_sql(query_update)


def get_salaryscale(endday=None):
    salaryscale = []
    if endday is None:
        query_sql = """SELECT salary_scale_code, salary_scale_name, salary_scale, startday, endday
                       FROM hrms_salaryscale;"""
    else:
        query_sql = " SELECT salary_scale_code, salary_scale_name, salary_scale, startday, endday "\
                    " FROM hrms_salaryscale "\
                    " WHERE endday = \'" + endday + "\';"
    gdata = get_data(query_sql)
    for col in gdata:
        salaryscale.append({
            "salary_scale_code": col[0],
            "salary_scale_name": col[1],
            "salary_scale": col[2],
            "startday": col[3],
            "endday": col[4]
        })
    return salaryscale


def insert_salaryscale(salary_scale_name, salary_scale, startday, endday):
    query_insert = " INSERT INTO hrms_salaryscale " \
                   " (salary_scale_name, salary_scale, startday, endday) "\
                   " VALUES (\'" \
                   + salary_scale_name + "\', \'" \
                   + salary_scale + "\', \'" \
                   + startday + "\', \'" \
                   + endday + "\');"
    return execute_sql(query_insert)


def get_currency():
    currency = []
    gdata = get_data("SELECT currency_code, currency_des FROM hrms_currency;")
    for col in gdata:
        currency.append({
            "currency_code": col[0],
            "currency_des": col[1],
        })
    return currency


def get_salarybasic(endday=None):
    salaryscale = []
    if endday is None:
        query_sql = """SELECT salary_basic_code, salary_basic_name, salary_basic_amount, currency_code, startday, endday
                       FROM hrms_salarybasic;"""
    else:
        query_sql = " SELECT salary_basic_code, salary_basic_name, " \
                    "        salary_basic_amount, currency_code, startday, endday "\
                    " FROM hrms_salarybasic "\
                    " WHERE \'" + endday + "\' BETWEEN startday and endday;"
    gdata = get_data(query_sql)
    for col in gdata:
        salaryscale.append({
            "salary_basic_code": col[0],
            "salary_basic_name": col[1],
            "salary_basic_amount": col[2],
            "currency_code": col[3],
            "startday": col[4],
            "endday": col[5]
        })
    return salaryscale


def insert_salarybasic(salary_basic_name, salary_basic_amount, currency_code, startday, endday):
    query_insert = " INSERT INTO hrms_salarybasic " \
                   " (salary_basic_name, salary_basic_amount, currency_code, startday, endday) "\
                   " VALUES (\'" \
                   + salary_basic_name + "\', \'" \
                   + salary_basic_amount + "\', \'" \
                   + currency_code + "\', \'" \
                   + startday + "\', \'" \
                   + endday + "\');"
    return execute_sql(query_insert)


def get_salarybasic_plus(endday=None):
    salaryscale_plus = []
    if endday is None:
        query_sql = """SELECT salary_basic_plus_code, salary_basic_plus_ratio, startday, endday
                       FROM hrms_SalaryBasicPlus;"""
    else:
        query_sql = " SELECT salary_basic_plus_code, salary_basic_plus_ratio, startday, endday "\
                    " FROM hrms_SalaryBasicPlus "\
                    " WHERE endday = \'" + endday + "\';"
    gdata = get_data(query_sql)
    for col in gdata:
        salaryscale_plus.append({
            "salary_basic_plus_code": col[0],
            "salary_basic_plus_ratio": col[1],
            "startday": col[2],
            "endday": col[3]
        })
    return salaryscale_plus


def insert_salarybasic_plus(salary_basic_plus_ratio, startday, endday):
    query_insert = " INSERT INTO hrms_SalaryBasicPlus " \
                   " (salary_basic_plus_ratio, startday, endday) " \
                   " VALUES (\'" \
                   + salary_basic_plus_ratio + "\', \'" \
                   + startday + "\', \'" \
                   + endday + "\');"
    return execute_sql(query_insert)


def get_union(endday=None):
    union = []
    if endday is None:
        query_sql = """SELECT union_code, union_company, union_employee, startday, endday, designation
                       FROM hrms_Union;"""
    else:
        query_sql = " SELECT union_code, union_company, union_employee, startday, endday, designation "\
                    " FROM hrms_Union "\
                    " WHERE endday = \'" + endday + "\';"
    gdata = get_data(query_sql)
    for col in gdata:
        union.append({
            "union_code": col[0],
            "union_company": col[1],
            "union_employee": col[2],
            "startday": col[3],
            "endday": col[4],
            'designation': col[5]
        })
    return union


def insert_union(union_company, union_employee, startday, endday, designation):
    query_insert = " INSERT INTO hrms_Union " \
                   " (union_company, union_employee, startday, endday, designation) " \
                   " VALUES (\'" \
                   + union_company + "\', \'" \
                   + union_employee + "\', \'" \
                   + startday + "\', \'" \
                   + endday + "\', \'" \
                   + designation + "\');"
    return execute_sql(query_insert)


def get_place_of_id(endday=None):
    place_of_id = []
    query_sql = "SELECT code_place_of_id, place_of_identification FROM hrms_PlaceOfIdentification;"
    gdata = get_data(query_sql)
    for col in gdata:
        place_of_id.append({
            "code_place_of_id": col[0],
            "place_of_identification": col[1],
        })
    return place_of_id


def get_salary(salary_month, salary_year,):
    union = []
    query_sql = " SELECT salary_code, cif, salary_month, salary_year, "\
                " union_code, insurance_code, meal_money_code, salary_scale_code, "\
                " salary_basic_plus_code, salary_basic_code, "\
                " salary_benefit, salary_other, salary_advance, "\
                " days_working, days_unpaid_leave, days_paid_leave, days_annual_leave, "\
                " bonus, kpi_point, overtime, tax_abatement "\
                " FROM hrms_salary " \
                " WHERE salary_month = \'" + salary_month + "\' "\
                " AND salary_year = \'" + salary_year + "\'; "
    
    gdata = get_data(query_sql)
    for col in gdata:
        union.append({
            "union_code": col[0],
            "union_company": col[1],
            "union_employee": col[2],
            "startday": col[3],
            "endday": col[4],
            'designation': col[5]
        })
    return union
