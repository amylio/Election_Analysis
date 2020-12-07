voting_data = [{"county":"Arapahoe","registered voters":422829},
{"county":"Denver","registered voters":463353},
{"county":"Jefferson","registered voters":432438}]

for counties_dict in voting_data:
    print(counties_dict)

len(voting_data)

for county in voting_data:
    print(county)

for i in range(len(voting_data)):
    print(voting_data[i])

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes/total_votes)*100
print("I received " +str(percentage_votes)+"% of total votes.")

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes*100}% of the total votes")

