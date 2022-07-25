from csv import reader

from models.fundraiser import Fundraiser
from models.level import Level

addies = []
with open("addresses.csv", "r") as f:
    rows = reader(f, delimiter='\n')
    for row in rows:
        addies.append(row[0])
host = addies.pop()

fundraiser = Fundraiser("Sandwich Fund", 20000000, [Level(0, 10000, "Friends"), Level(1, 100000, "Bigbois")], host)

print(fundraiser)
