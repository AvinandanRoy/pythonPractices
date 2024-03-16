
travellingList = ['India','Bhutan','Chaina','Nepal','Mayanmar']

removeItem = 'Mayanmar'

for country in travellingList:
    if country == removeItem:
        travellingList.remove(country)

print("New Travelling List :",travellingList)