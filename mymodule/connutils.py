from django.db import connection, transaction


def get_data(query_sql):
    try:
        
        cursor = connection.cursor()
        # cursor.execute("SELECT cif, fullname, birthday, hrms_sexofemployee.description
        # FROM hrms_employee, hrms_sexofemployee
        # Where
        # hrms_employee.gender_code = hrms_sexofemployee.gender_code")
        cursor.execute(query_sql)
        return cursor.fetchall()
    except ImportError:
        return "Error"


def execute_sql(query_sql):
    try:
        # Insert nhiều dòng trong 1 lần thực thi hàm
        # query_sql = "INSERT INTO animals (grp,name) VALUES ('mammal','dog'),
        # ('mammal','cat'), 
        # ('bird','penguin'),
        # ('fish','lax'),
        # ('mammal','whale'), 
        # ('bird','ostrich');"
        # query_sql += "INSERT INTO animals (grp,name) VALUES ('mammal','bird');"
        
        cursor = connection.cursor()
        cursor.execute(query_sql)
        
        return "Dữ liệu đã được cập nhật!"  # cursor.fetchall()
    except ImportError:
        cn = connection
        return "Error"


def get_data_scalar(query_sql):
    # Lấy dữ liệu Thống kê hoặc tính toán từ database
    try:
        cursor = connection.cursor()        
        cursor.execute(query_sql)
        return cursor.fetchall()
    except ImportError:
        return "Error"
