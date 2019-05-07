def validar_campos(obj, campos_obrigatorios, tipos,campos_n_obrj = []):
    bkp_campos =campos_obrigatorios.copy()
    bkp_tipos = tipos.copy()
    if len(campos_n_obrj) == 0:
        pass
    else:
        for x in campos_n_obrj:
            bkp_campos.append(x)
            bkp_tipos[x] = int
    print('oijuhkjdfnkjlsdnsjdkvnsjfskdvnfskj')
    print(campos_obrigatorios)
    print(tipos)
    print(obj)
    print("-"*23)
    if type(obj) != dict:
        return False
    for k in obj:
        if k not in bkp_campos:
            print('q')
            print(k)
            return False
    for k in bkp_campos:
        if k not in obj:
            print('qq')
            return False
    for item in obj:
        if type(obj[item]) != bkp_tipos[item]:
            print('qqq')
            return False
    bkp_campos.clear()
    bkp_tipos = {}
    return True

