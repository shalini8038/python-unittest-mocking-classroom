import pandas as pd
data = [['Kritika',20000], ['Harsh',25000], ['Ragini',10000],['Rohit',8000]]
ds= pd.DataFrame(data,columns=['Name','Salary'])

class DbHelper:
    def get_maximum_salary(self):
        return ds['Salary'].max()

    def get_minimum_salary(self):
        return ds['Salary'].min()
        
if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
