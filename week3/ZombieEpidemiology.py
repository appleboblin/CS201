year = 2001
n_humans = 535753
n_zombies = 10
while year <= 2029:
    print(year, n_zombies, n_humans, sep=",")
    n_bitten = (n_humans - n_zombies)*0.1
    n_humans = n_humans - n_bitten
    n_zombies = n_zombies + n_bitten
    year += 1

