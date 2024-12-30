import pandas as pd
data={
    "name":["alice","bob","charlie","david","eva"],
    "age":[25,30,45,56,22],
    "department":["HR","IT","marketing","HR","IT"],
    "salary":[50000,60000,70000,85000,55000],
    "joinig_date":['2019-05-01', '2018-06-15', '2017-07-20', '2015-04-11', '2020-09-10'],
    "city":['new york','california','san franscisco','chicago','los angeles']}
df=pd.DataFrame(data)
selected_columns=df[["name","age"]]
print("selected columns:\n ",selected_columns)


salary=df[df["salary"]>50000]
print("salary greater than 50000:\n",salary)

sorted_data=df.sort_values(by="age")
print('sorted data by age:\n',sorted_data)

drop_column=df.drop(columns=["city"])
print("dataframe after dropping column:\n",drop_column)