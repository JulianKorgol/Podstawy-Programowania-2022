for i in range(0, numer[0]):  # Do poprawy, nie łapie wszytskich elementów z listy.
    doDodania = klasy.pop(i)
    # print(doDodania)
    szkola['klasa_{0}'.format(x - 1 if runned else x)].append(doDodania)
    print(szkola['klasa_{0}'.format(x - 1 if runned else x)])  # Do usunięcia