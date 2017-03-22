import requests
from bs4 import BeautifulSoup
import massFunctions


data = requests.get('https://bkpw.net/stats.php?idp=').text ## need to enter alliance id here
soup = BeautifulSoup(data)

total_cost = 0
local_cost = 0
temp = 0
ids = []
for td in soup.find_all('td'):
    try:
        temp = int(td.string)
    except ValueError:
        continue
    else:
        ids.append(int(td.string))


print(ids)

for id in ids:
    nation_link = 'https://politicsandwar.com/api/nation/id=' + str(id)
    data = requests.get(nation_link).json()
    nation_name = data['name']
    cities = data['cityids']
    print("========================================================================")
    print("NATION NAME: " + nation_name)
    print("NATION LINK: " + "https://politicsandwar.com/nation/id=" + str(id))
    print(" ")

    for city in cities:
        city_link = 'https://politicsandwar.com/api/city/id=' + str(city)
        city_data = requests.get(city_link).json()
        infrastructure = float(city_data['infrastructure'])
        name = city_data['name']
        print(name + ": " + str(infrastructure))
        if(infrastructure < 1500):
            repair_cost = float(massFunctions.infra_calculator(infrastructure, 1500, 0).replace(",", ""))
            print("Estimated repair cost for city: " + str(repair_cost))
            local_cost += repair_cost
    print("\nTotal cost for nation:" + str(local_cost))
    total_cost += local_cost
    local_cost = 0

print("Total cost for rebuilding aid(all nations): " + str(total_cost))
