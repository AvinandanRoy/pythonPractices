def list_to_dict(k,v):
    return dict(zip(k,v))



city = ['Dhaka','Jashore','Khulna','Chittagong','Narail']
year = [2021,2018,2021,2022,2002]

newDict = list_to_dict(city,year)
print(newDict)