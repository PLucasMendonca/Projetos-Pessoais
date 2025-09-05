

mesa_1 = {'comanda1': ['bebida', 24, 'comida', 74, 'doces', 21]}
mesa_2 = {'comanda1': ['bebida', 24, 'comida', 74, 'doces', 21], 'comanda2': ['bebida', 41, 'comida', 2, 'doces', 13]}
mesa_3 = {'comanda1': ['bebida', 24, 'comida', 74, 'doces', 21], 'comanda2': ['bebida', 41, 'comida', 2, 'doces', 13], 'comanda3': ['bebida', 41, 'comida', 2, 'doces', 13]}

def base():
    for i in mesa_1:
        print(i)
    print(mesa_1)
    print(mesa_2)
    print(mesa_3)

def main():
    base()


if __name__ == '__main__':
    main()