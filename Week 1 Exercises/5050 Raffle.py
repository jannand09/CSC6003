import random

entries = {
    "Louisa Jenness": 30,
    "Kaissa Oulhadj": 1,
    "Min Chen": 10,
    "Jenny Marcelin": 3,
    "Nora Lorion": 20,
    "Greg Sonek": 10,
    "Brett Wellman": 30,
    "Ruben Mosquera": 1,
    "Aisha Francis": 30,
    "Greg Lespinasse": 10,
    "Phoebe Lumley": 20,
    "Omar Merida": 1,
    "Kevin Hepner": 10,
    "Gabe Moore": 1,
    "Jeanie Hooper": 72,
    "William Gomes": 1,
    "Mackensy Beaucioquot": 1,
    "Emma Michalowski": 1,
    "David Kamin": 22,
    "Juan Gaivan": 2,
    "Marta Aguilar": 1,
    "Alan Blair": 10,
    "FULL DONATION": 3,
    "Serge Andre": 1
}

tickets = []

for x in entries:
    for j in range(entries[x]):
        tickets.append(x)

winNum = random.randrange(len(tickets))

print(tickets[winNum])
