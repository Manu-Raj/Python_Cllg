n=int(input("Enter Num of Songs"))
lst=[]
vSongs=[]
cSongs=[]

songs2 = ["BeatIt","Bille Jean","Part-Time-Lover", "Blinding Lights","Shake It Off","Levitating"]

for i in range(n):
    lst.append(input("Enter Song Title: "))

songs=lst+songs2
print(songs)

songs_NoDuplicates=set(songs)
print(songs_NoDuplicates)

songs=list(songs_NoDuplicates)
rotate_n=int(input("Enter rotate n positions: "))
print(songs[rotate_n:]+ songs[:rotate_n])