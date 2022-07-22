import string

def dict():
    l = string.ascii_lowercase
    l = list(l)
    d = {}

    for i in range(len(l)):
        d[l[i]] = l[(i+3)%26]
    return d

f = open("sherlock.txt", "r")
g = open("enc.txt", "w")
d = dict()

c = f.read(1) 
while(c!=''):
    g.write(d[c])
    c = f.read(1)

f.close()
g.close()