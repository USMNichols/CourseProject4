#Brandon Nichols
#jay Gaines CIS261
#CourseProject4

from binascii import Incomplete
from datetime import datetime


def CreateUsers():
    print("Create users, passwords and roles:")
    UserFile = open("Users.txt", "a+")
    while True:
        username + GetUserName()
        if (username.upper() == "End"):
            break
        userpwd = GetUserPassword()
        userrole =GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter  user name or'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd



def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "User")
            return userrole
        else:
            userrole + input("Enter role (Admin or User): ")
 
            
def printuserinfo():
    UserFile = open("User.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User name: ", username, " Password: ", userpassword, "Role: ", userrole)
        


def Login():
    UserFile = open("User.txt", "r")
    UserList = []
    UserName = input("Enter user name: ")
    UserRole = "None"
    while True:
        UserDetail = userFile.readline()
        if not UserDetail:
            return UserRole, UserName
        UserDetail = userDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0]
            UserRole = UserList[2]
            return UserRole, UserName
    return UserRole, UserName


def GetEmpName():
    empname = input("Enter employee name: ")
    return empname


def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter the End date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours

def GetHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

    
def CalcTaxAndNetPay(hours, hourlyRate, taxrate):
    grosspay = hours * hourlyRate
    incometax + grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt, "r")
    while True:
        rundate = input("Enter start date for the report (mm/dd/yyyy) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%y")
            break
        except ValueError:
            print("Invalid date format. Try Again.")
            print()
            continue
    while True:
        EmpDetail = EmpFile.redline()
        if not EmdDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if str(rundate).upper() !+ "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%y)
            if (checkdate < rundate):
                continue
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay =CalcTaxAndNetPay(hours, hourlyRate, taxrate)
        print(fromdate, todate,empname, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True
    if (DetailsPrinted):
        PrintTotals(EmpTotals)
    else:
        print("No detail information to print")

def PrintTotals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total hours worked: {EmpTotals['TotHrs']:,.2f}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total income tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total net pay: {EmpTotals['TotNetPay']:,.2f}")
    
if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, username = Login()
    DetailsPrinted = False
    EmpTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, "is invalid")
else:
    if (UserRole.upper() == "ADMIN"):
        EmpFile = open("Employees.txt", "a+")
        while True:
            empname = GetEmpName()
            if (empname.upper() == "END"):
                break
            fromdate, todate = GetDatesWorked()
            hours = GetHoursWorked()
            hourlyRate = GetHourlyRate()
            taxrate = GetTaxRate()
            EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyRate) + "|" + str(taxrate) + "\n"
            EmpFile.write(EmpDetail)
        
        EmpFile.close()
    printinfo(DetailsPrinted)
     
    
        

                
