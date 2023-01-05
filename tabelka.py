def get_part(sentence, tokens, token1, token2):
    # Initialize the starting and ending positions of the part of the sentence
    start_pos = 0
    end_pos = len(sentence)
    # Find the starting position of the part of the sentence
    for i, token in enumerate(tokens):
        if token == token1:
            start_pos = sentence.index(token, start_pos)
            break
    else:
        start_pos += len(token) + 1

    # Find the ending position of the part of the sentence
    for i, token in enumerate(tokens):
        if token == token2:
            end_pos = sentence.index(token, start_pos) + len(token)
            break
        else:
            end_pos += len(token) + 1

    # Get the part of the sentence between the two tokens
    part_of_sentence = sentence[start_pos:end_pos]

    return part_of_sentence
    



def pod(slowo, zdanie):
    lista = []
    for i in range(len(zdanie)):
        lista.append(0)
        if slowo[0] == zdanie[i][0]:
            lista[i] = 1
    for i in range(len(zdanie)):
        if zdanie[i][6] == slowo[0]:
            lista[i] = 1
            lista2 = pod(zdanie[i], zdanie)
            for j in range(len(lista2)):
                if lista2[j] == 1:
                    lista[j] = 1
    return lista


def zlacz(zdanie, lista):
    newlista = []
    for i in range(len(zdanie)):
        if lista[i] == 1:
            newlista.append(zdanie[i][1])
    # listanew = []
    # i = 0
    # for s in range(len(newlista)):
    #     if newlista[s] not in [",", ".", ";", "!", "?", ")", "}", "]", ">"]:
    #         listanew.append(newlista[s])
    #         if newlista[s-1] not in ["(", "<", "[", "{"]:
    #             i += 1
    #     else:
    #         if not listanew:
    #             listanew.append(newlista[s])
    #         else:
    #             listanew[i-1] += newlista[s]
    return " ".join(newlista)


def zmien(zdanie, lista):
    newlista = []
    for i in range(len(zdanie)):
        if lista[i] == 1:
            newlista.append(zdanie[i][1])
    return newlista


def zmien2(zdanie, lista):
    newlista = []
    for i in range(len(zdanie)):
        if lista[i] == 1 and (zdanie[i][3] != "interp" or zdanie[i][7] != "punct"):
            newlista.append(zdanie[i][1])
    return newlista


def zlicz(lista):
    slowa = 0
    znaki = 0
    for i in lista:
        for _ in i:
            znaki += 1
        slowa += 1
    return [slowa, znaki]


def main():
    with open("/Users/kvmilos/Desktop/PDB/treebank/PDB_test.conll", 'r') as plik:
        with open("/Users/kvmilos/Desktop/PDB/treebank/PDB_dev.conll", 'r') as plik2:
            with open("/Users/kvmilos/Desktop/PDB/treebank/PDB_train.conll", 'r') as plik3:
                lib = []
                for i in plik:
                    lib += [i.split()]
                for i in plik2:
                    lib += [i.split()]
                for i in plik3:
                    lib += [i.split()]

    with open("/Users/kvmilos/Desktop/PDB/sentences/PDB_test.txt", 'r') as plik:
        with open("/Users/kvmilos/Desktop/PDB/sentences/PDB_dev.txt", 'r') as plik2:
            with open("/Users/kvmilos/Desktop/PDB/sentences/PDB_train.txt", 'r') as plik3:
                phr = []
                for i in plik:
                    phr += [i.strip()]
                for i in plik2:
                    phr += [i.strip()]
                for i in plik3:
                    phr += [i.strip()]

    with open("/Users/kvmilos/Desktop/PDB/meta/PDB_test.json", 'r') as plik:
        meta = []
        line = 0
        for i in plik:
            if line%5 == 4:
                meta.append(i.split()[1][1:-1])
            line += 1
    with open("/Users/kvmilos/Desktop/PDB/meta/PDB_dev.json", 'r') as plik:
        line = 0
        for i in plik:
            if line%5 == 4:
                meta.append(i.split()[1][1:-1])
            line += 1
    with open("/Users/kvmilos/Desktop/PDB/meta/PDB_train.json", 'r') as plik:
        line = 0
        for i in plik:
            if line%5 == 4:
                meta.append(i.split()[1][1:-1])
            line += 1


    n = 0
    lib2 = [[]]
    for i in lib:
        if not i:
            n += 1
            lib2 += [[]]
        else:
            lib2[n] += [i]
    lib2.remove([])
    tabela = []
    j = 0
    k = 0
    for zdanie in lib2:
        licznik = []
        for _ in zdanie:
            licznik.append([0])
        for slowo in zdanie:
            numer = 0
            for _ in licznik:
                if slowo[6] == str(numer) and slowo[7] == "conjunct":
                    licznik[numer][0] += 1
                    licznik[numer].append(slowo)
                numer += 1
        for i in range(len(licznik)):
            if licznik[i][0] == 2:
                tabela.append([])
                if int(zdanie[i-1][6]) == 0:  # gdy nie ma nadrzenika ponad spojnikiem
                    tabela[j].append(["0"])
                    tabela[j].append([""])
                    tabela[j].append([""])
                    tabela[j].append([zdanie[i-1][7]]) #etyk. koord - root
                else:
                    if int(zdanie[int(zdanie[i-1][6])-1][0]) > int(licznik[i][1][0]) and int(zdanie[int(zdanie[i-1][6])-1][0]) > int(licznik[i][2][0]):
                        tabela[j].append(["R"])
                    elif int(zdanie[int(zdanie[i-1][6])-1][0]) < int(licznik[i][1][0]) and int(zdanie[int(zdanie[i-1][6])-1][0]) < int(licznik[i][2][0]):
                        tabela[j].append(["L"])
                    else:
                        tabela[j].append(["M"])
                    tabela[j].append([zdanie[int(zdanie[i-1][6])-1][1]])  # nadrzednik
                    tabela[j].append([zdanie[int(zdanie[i-1][6])-1][3]])  # kat nadrzednika
                    tabela[j].append([zdanie[i-1][7]])  # etykieta koord
                new = pod(licznik[i][1], zdanie)
                for x in range(len(new)):
                    if new[x - 1] == 0 and new[x] == 1 or x == 0 and new[x] == 1:
                        a = x
                        break
                for x in range(len(new)):
                    if new[x] == 1 and x == len(new) - 1 or new[x] == 1 and new[x + 1] == 0:
                        b = x
                new_list = [zdanie[i][1] for i in range(len(zdanie))]
                tabela[j].append([zdanie[i-1][2]])  # spojnik/interp
                tabela[j].append([zdanie[i-1][3]])  # kat spojnika/interp
                if zdanie[a][1] != zdanie[b][1]:
                    tabela[j].append([len(get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1]).split(sep = ' ' ))])
                else:
                    tabela[j].append([zlicz(zmien2(zdanie, pod(licznik[i][1], zdanie)))[0]]) # pierwsze - slowa
                tabela[j].append([zlicz(zmien(zdanie, pod(licznik[i][1], zdanie)))[0]])  # pierwsze - tokeny
                if zdanie[a][1] != zdanie[b][1]:
                    tabela[j].append([len(get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1]))])
                    tabela[j].append([get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1])])
                else:
                    tabela[j].append([len(zlacz(zdanie, pod(licznik[i][1], zdanie)))])
                    tabela[j].append([zlacz(zdanie, pod(licznik[i][1], zdanie))])
                tabela[j].append([licznik[i][1][1]])  # glowna pierwszego czlonu
                tabela[j].append([licznik[i][1][3]])  # tag glowy p. cz.
                new2 = pod(licznik[i][2], zdanie)
                for x in range(len(new2)):
                    if new2[x - 1] == 0 and new2[x] == 1 or x == 0 and new2[x] == 1:
                        a = x
                        break
                for x in range(len(new2)):
                    if new2[x] == 1 and x == len(new2) - 1 or new2[x] == 1 and new2[x + 1] == 0:
                        b = x
                if zdanie[a][1] != zdanie[b][1]:
                    tabela[j].append([len(get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1]).split(sep=' '))])
                else:
                    tabela[j].append([zlicz(zmien2(zdanie, pod(licznik[i][2], zdanie)))[0]]) # drugie - slowa
                tabela[j].append([zlicz(zmien(zdanie, pod(licznik[i][2], zdanie)))[0]])  # drugie - tokeny
                if zdanie[a][1] != zdanie[b][1]:
                    tabela[j].append([len(get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1]))])
                    tabela[j].append([get_part(phr[k], new_list, zdanie[a][1], zdanie[b][1])])  # drugie - caly czlon
                else:
                    tabela[j].append([len(zlacz(zdanie, pod(licznik[i][2], zdanie)))]) # drugie - znaki
                    tabela[j].append([zlacz(zdanie, pod(licznik[i][2], zdanie))])
                tabela[j].append([licznik[i][2][1]])  # glowa drugiego czlonu
                tabela[j].append([licznik[i][2][3]])  # tag glowy d. cz.
                tabela[j].append([phr[k]])
                tabela[j].append([meta[k]])
                j += 1
        k += 1
    ile = 0
    with open("wyniki_0401.csv", "w") as f:
        f.write("pozycja nadrzędnika\tnadrzędnik\ttag nadrzędnika\tetykieta koordynacji\tspójnik\ttag spójnika\tsłowa pierwszego członu\ttokeny pierwszego członu\tznaki pierwszego członu\tpierwszy człon\tgłowa pierwszego członu\ttag głowy pierwszego członu\tsłowa drugiego członu\ttokeny drugiego członu\tznaki drugiego członu\tdrugi człon\tgłowa drugiego członu\ttag głowy drugiego członu\tzdanie\tsent_id\n")
        for i in tabela:
            a = 0
            ile += 1
            for j in i:
                a += 1
                f.write(str(j[0]))
                if a != 20:
                    f.write("\t")
            f.write("\n")


main()
