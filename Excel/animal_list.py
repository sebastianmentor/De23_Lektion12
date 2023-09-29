def animal_list(english = False) -> list[str]:
    '''If english is set to True, the list will contain english name for animals'''
    lista_med_djur = []

    with open('.\Excel\djur.txt','r',encoding='utf-8') as f:
        for rader_med_djur in f.readlines():
            sve, eng = rader_med_djur.strip().split()
            lista_med_djur.append(sve)

            if english: lista_med_djur.append(eng)
    return lista_med_djur

animal_list()