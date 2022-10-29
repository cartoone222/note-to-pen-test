import requests

url = input("entrer la cible : ")

while True:

    #_____________________________________________________________________________

    r = requests.options(url)

    if r.status_code == 200:
        print("options [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("options [NOP]")

    #_____________________________________________________________________________

    r = requests.get(url)

    if r.status_code == 200:
        print("get [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("get [NOP]")

    #_____________________________________________________________________________

    r = requests.head(url)

    if r.status_code == 200:
        print("head [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("head [NOP]")

    #_____________________________________________________________________________

    r = requests.post(url)

    if r.status_code == 200:
        print("post [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("post [NOP]")

    #_____________________________________________________________________________

    r = requests.put(url)

    if r.status_code == 200:
        print("put [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("put [NOP]")

    #_____________________________________________________________________________

    r = requests.delete(url)

    if r.status_code == 200:
        print("delete [OK]")
        try:
            print(r.text)
            break
        except:
            print("echeque")

    else:
        print("delete [NOP]")
    
    break
