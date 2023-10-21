
from datetime import datetime
import mysql.connector
#
mydb = mysql.connector.connect(host="localhost", user="root", password="Sql@007@", port=3306)
# # print(mydb)
my_curser = mydb.cursor()
# my_curser.execute("create database employee_management")
my_curser.execute("use employee_management")
#
#
# my_curser.execute("create table employee_details(Emp_id varchar(10) not null primary key,Pin int UNIQUE,First_name varchar(50),Last_name varchar(50),Address varchar(150),Mobile_no int,Designation varchar(100),Posting_location varchar(100),Salary int)")
#
class Hr:
    def add_employee(self):
        emp_id_ = input("ENTER THE EMPLOYEE_ID:")
        emp_id = emp_id_.upper()
        sql_query = "select * from employee_details where Emp_id=%s "
        values = (
        emp_id,)  # while using  my sql connector you use Python tuples to pass parameter values to SQL queries and receive query results.
        my_curser.execute(sql_query, values)
        result = my_curser.fetchone()
        if result is None:
            password = (input("ENTER THE PASSWORD{numbers}:"))
            if len(password) < 4:
                print("MIN PASSWORD LENGTH IS 4 DIGIT")
                return
            pin = int(password)
            sql_query = "select * from employee_details where Pin=%s "
            values = (pin,)
            my_curser.execute(sql_query, values)
            result = my_curser.fetchone()
            if result is None:
                first_name_ = input("ENTER THE FIRST NAME:")
                first_name = first_name_.upper()
                last_name_ = input("ENTER THE LAST NAME:")
                last_name = last_name_.upper()
                address_ = input("ENTER THE ADDRESS:")
                address = address_.upper()
                mob_no = input("ENTER THE MOBILE NO:")
                if len(mob_no) != 10:
                    print("ENTER A VALID MOB NO")
                    return
                mob_no_ = int(mob_no)
                designation_ = input("ENTER THE DESIGNATION OF EMPLOYEE:")
                designation = designation_.upper()
                posting_location_ = input("ENTER THE POSTING LOCATION:")
                posting_location = posting_location_.upper()
                salary = int(input("ENTER THE CTC OF EMPLOYEE:"))
                # nominee=input("ENTER THE NOMINEE DETAILS:").upper()
                # nominee_age=int(input("ENTER THE AGE OF NOMINEE:"))
                # nominee_relation=input("ENTER THE RELATION WITH INSURED:").upper()
                sql_query = "INSERT INTO employee_details (emp_id,Pin, First_name, Last_name, Address, Mobile_no, Designation, Posting_location, Salary) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (emp_id, pin, first_name, last_name, address, mob_no_, designation, posting_location, salary)
                my_curser.execute(sql_query, values)
                mydb.commit()
                print("EMPLOYEE ADDED SUCCESSFULLY")
            else:
                print("PASSWORD ALREADY ASSIGNED TO ANOTHER EMPLOYEE")
        else:
            print("EMPLOYEE ID ASSIGNED TO ANOTHER EMPLOYEE")

    def employee_del(self):
        emp_id_ = input("ENTER THE EMPLOYEE NO:")
        emp_id = emp_id_.upper()
        sql_query = "select * from employee_details where Emp_id=%s"
        values = (emp_id,)
        my_curser.execute(sql_query, values)
        result = my_curser.fetchone()
        if result is not None:
            sql_query_del = "delete from employee_details where Emp_id=%s "
            values_del = (emp_id,)
            my_curser.execute(sql_query_del, values_del)
            mydb.commit()
            print("DATA DELETED SUCCESSFULLY FROM DATA BASE")
        else:
            print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")


def salary_updation(self):
    emp_id_ = input("ENTER THE EMPLOYEE ID:")
    emp_id = emp_id_.upper()
    sq_val = "select * from employee_details where Emp_id=%s "
    value = (emp_id,)
    my_curser.execute(sq_val, value)
    result = my_curser.fetchone()
    if result is not None:
        up_sal = int(input("ENTER THE UPDATED SALARY :"))
        sql_up = "update employee_details set salary=%s where Emp_id=%s"
        val_up = (up_sal, emp_id)
        my_curser.execute(sql_up, val_up)
        mydb.commit()
        print("DATA UPDATED SUCCESSFULLY IN DATA BASE")
    else:
        print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")


def get_details(self):
    emp_id_ = input("ENTER THE EMPLOYEE ID:")
    emp_id = emp_id_.upper()
    sql_details = "select * from employee_details where Emp_id=%s"
    val_details = (emp_id,)
    my_curser.execute(sql_details, val_details)
    result = my_curser.fetchone()
    if result is not None:
        pin, emp_id, first_name, last_name, address, mob_no, designation, posting_location, salary, nominee, nominee_age, nomi_relation = result
        print(
            f"FIRST_NAME:{first_name},LAST_NAME:{last_name},ADDRESS :{address},MOB_NO:{mob_no},DESIGNATION:{designation},POSTING_LOCATION:{posting_location},SALARY:{salary},NOMINEE_NAME:{nominee},NOMINEE_AGE:{nominee_age},NOMINEE_RELATION:{nomi_relation}")
    else:
        print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")


def filter_sal(self):
    start_salr = int(input("ENTER THE STARTING SALARY RANGE:"))
    end_salr = int(input("ENTER THE ENDING SALARY RANGE: "))
    sql_query = "select Emp_id,First_name,Designation,Posting_location from employee_details where salary between %s and %s"
    sal_values = (start_salr, end_salr)
    my_curser.execute(sql_query, sal_values)
    result = my_curser.fetchall()
    data = list(result)
    if data:
        for i, account in enumerate(data):
            emp_id, first_name, designation, posting_location = account
            print(
                f"EMP_ID:{emp_id},FIRST_NAME:{first_name},DESIGNATION:{designation},POSTING_LOCATION:{posting_location}")
    else:
        print("0 RESULT FOUND")


def filter_location(self):
    loc_input_ = input("ENTER THE  POSTING_LOCATION DETAILS TO FILTER THE DATA:")
    loc_input = loc_input_.upper()
    sql_query = "select Emp_id,First_name,Designation,salary from employee_details where Posting_location=%s"
    values = (loc_input,)
    my_curser.execute(sql_query, values)
    result = my_curser.fetchall()
    data = list(result)
    if data:
        for i, account in enumerate(data):
            emp_id, first_name, designation, salary = account
            print(f"EMP_ID: {emp_id}, First_name: {first_name}, Designation: {designation}, Salary: {salary}")
    else:
        print("0 DETAILS FOUND")


def filter_designation(self):
    desig_input_ = input("ENTER THE DESIGNATION DETAILS :")
    desig_input = desig_input_.upper()
    sql_query = "select emp_id,first_name,mobile_no,Posting_location,salary from employee_details where Designation=%s"
    values = (desig_input,)
    my_curser.execute(sql_query, values)
    result = my_curser.fetchall()
    data = list(result)
    # print(data)
    if data:
        for i, account in enumerate(data):
            emp_id, first_name, mob_no, posting_location, salary = account
            print(
                f"EMP_ID:{emp_id},FIRST_NAME:{first_name},MOB_NO:{mob_no},POSTING_LOCATION:{posting_location},SALARY:{salary}")


    else:
     print("0 RESULTS FOUND ")


class Employee:
    def pin_change(self):
        emp_id_ = input("ENTER THE EMP ID:")
        emp_id = emp_id_.upper()
        pin = int(input("ENTER THE PASSWORD:"))
        query = "select * from employee_details where emp_id=%s and pin=%s"
        values = (emp_id, pin)
        my_curser.execute(query, values)
        result = my_curser.fetchone()
        if result is not None:
            new_pin_ = input("ENTER THE NEW PASSWORD:")
            if len(new_pin_) >= 4:
                new_pin = int(new_pin_)
                query_pin_val = "select * from employee_details where pin=%s"
                values_pin = (new_pin,)
                my_curser.execute(query_pin_val, values_pin)
                result_pin = my_curser.fetchone()
                # print(result_pin)
                if result_pin is None:
                    con_pin = int(input("CONFORM THE PIN NUMBER:"))
                    if new_pin == con_pin:
                        query = "update employee_details set pin=%s where emp_id=%s"
                        values = (new_pin, emp_id)
                        my_curser.execute(query, values)
                        mydb.commit()
                        print("PASSWORD UPDATED SUCCESSFULLY KINDLY LOG OUT AND LOG IN  ")
                    else:
                        print("NEW PASSWORD AND OLD PASSWORD MISSMATCH")
                else:
                    print("PIN ALREADY ASSIGNED TO ANOTHER EMPLOYEE")
            else:
                print("MIN LENGTH OF PASSWORD IS 4 ")
        else:
            print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE/INVALID EMPLOYEE ID OR PASSWORD ")

    def mob_change(self):
        emp_id = input("ENTER THE EMP_ID:").upper()
        pin = int(input("ENTER THE PASSWORD:"))
        query = "select * from employee_details where emp_id=%s and pin=%s"
        values = (emp_id, pin)
        my_curser.execute(query, values)
        result = my_curser.fetchone()
        if result is not None:
            mob_no_ = input("ENTER THE NEW MOB NO:")
            if len(mob_no_) != 10:
                print("ENTER A VALID MOB NO")
                return
            else:
                mob_no = int(mob_no_)
                query_mob = "select mobile_no from employee_details where emp_id=%s"
                values_mob = (emp_id,)
                my_curser.execute(query_mob, values_mob)
                result = my_curser.fetchone()
                for i in result:
                    mob_no_list = i
                    if mob_no_list == mob_no:
                        print("OLD AND NEW MOBILE NO CANNOT BE CAME ")
                        return
                else:
                    up_query = "update employee_details set mobile_no=%s where emp_id=%s"
                    up_val = (mob_no, emp_id)
                    my_curser.execute(up_query, up_val)
                    mydb.commit()
                    print("MOBILE NO UPDATED SUCCESSFULLY")
        else:
            print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE ")

    # def nominee_add(self):
    #     emp_id=input("ENTER THE EMPLOYEE_ID:").upper()
    #     pin=input("ENTER THE PIN:")
    #     query="select * from employee_details where emp_id=%s and pin=%s"
    #     values=(emp_id,pin)
    #     my_curser.execute(query,values)
    #     result=my_curser.fetchone()
    #     if result is not None:
    #         nominee_name=input("ENTER THE NOMINEE NAME:")
    #         nominee_age=int(input("ENTER THE AGE OF NOMINEE:"))
    #         rel_insured=input("ENTER THE RELATION :")
    #         up_query="update employee_details set nominee=%s ,nominee_age=%s ,nomi_relation=%s where emp_id=%s"
    #         up_values=(nominee_name,nominee_age,rel_insured,emp_id)
    #         my_curser.execute(up_query,up_values)
    #         mydb.commit()
    #         print("NOMINEE DETAILS UPDATED AGAINST",emp_id)
    #     else:
    #         print("EMPLOYEE DETAILS NOT FOUND IN DATA BASE")




def main():
    hr = Hr()
    emp = Employee()
    print("WELCOME TO EMPLOYEE MANAGEMENT SYSTEM", datetime.today())
    while True:
        print("LOGIN OPTIONS")
        print("1-HR LOGIN")
        print("2-EMPLOYEE LOGIN")
        print("3-EXIT")
        choice = int(input("ENTER THE CHOICE: "))
        if choice == 1:
            print("WELCOME TO EMPLOYEE MANAGEMENT SYSTEM,YOU HAVE LOGGED IN AS HR,KINDLY CHOOSE THE OPTION FROM BELOW ")
            print("1-ADD EMPLOYEE")
            print("2-UPDATE SALARY OF EMPLOYEE")
            print("3-VIEW EMPLOYEE DETAILS ")
            print("4-FILTER OPTIONS")
            print("5-DELETE EMPLOYEE")
            print("6-EXIT")
            sel = int(input("ENTER THE CHOICE:"))
            if sel == 1:
                hr.add_employee()
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            elif sel == 2:
                hr.salary_updation()
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            elif sel == 3:
                hr.get_details()
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            elif sel == 4:
                print("1-FILTER BY SALARY RANGE")
                print("2-FILTER BY WORK LOCATION")
                print("3-FILTER BY DESIGNATION")
                c1 = int(input("SELECT THE FILTER OPTION:"))
                if c1 == 1:
                    hr.filter_sal()
                    print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
                elif c1 == 2:
                    hr.filter_location()
                    print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
                elif c1 == 3:
                    hr.filter_designation()
                    print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
                else:
                    print("INVALID CHOICE")
            elif sel == 5:
                hr.employee_del()
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            elif sel == 6:
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
                break
            else:
                print("INVALID CHOICE")
        elif choice == 2:
            print("WELCOME TO EMPLOYEE MANAGEMENT SYSTEM,YOU HAVE LOGGED AS EMPLOYEE CHOOSE THE OPTION FROM BELOW")
            print("1-PIN CHANGE")
            print("2-MOBILE NUMBER CHANGE")
            # print("3-NOMINEE DETAILS UPDATION ")
            # print("4-EMPLOYEE DETAILS")
            print("3-NEW FEATURES DETAILS")
            print("4-EXIT")
            c2 = int(input("ENTER THE OPTION:"))
            if c2 == 1:
                emp.pin_change()
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            elif c2 == 2:
                emp.mob_change()

                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            # elif c2==3:
            #     emp.nominee_add()
            #     print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            # elif c2==4:
            #     print("IMPLEMENTATION UNDER PROCESS PLEASE TRY AGAIN AFTER SOME DAYS THANK YOU ")
            elif c2 == 3:
                print(
                    "NOW THE EMPLOYEE CAN UPDATE THEIR NOMINEE DETAILS BY VISITING EMPLOYEE MANAGEMENT SYSTEM,LOGIN AS EMPLOYEE THEN SELECT NOMINEE UPDATION FROM THE CHOICE ")
            elif c2 == 4:
                print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
                break
            else:
                print("INVALID CHOICE1")
        elif choice == 3:
            print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ", datetime.today())
            break
        else:
            print("INVALID SELECTION")


main()