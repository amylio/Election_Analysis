voting_data = [{"county":"Arapahoe","registered voters":422829},
{"county":"Denver","registered voters":463353},
{"county":"Jefferson","registered voters":432438}]

for counties_dict in voting_data:
    for county in counties_dict.values():
        print(county,"has registered voters")