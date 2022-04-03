#stuck
tumpukan = [1,2,3,4,5]
print(tumpukan)
#pop
out = tumpukan.pop()
print("data keluar:",out)
print("data sekarang:",tumpukan)

#top
print(len(tumpukan))

#push
tumpukan.append(5)
print("data masuk:",5)
print("data sekarang:",tumpukan)

#empty
def is_empty():
    return tumpukan == []
print(is_empty())

#size
jumlahData = len(tumpukan)
print(jumlahData)
