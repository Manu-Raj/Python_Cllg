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
songs=list(songs_NoDuplicates)
print(songs)


rotate_n=int(input("Enter rotate n positions: "))
print(songs[rotate_n:]+ songs[:rotate_n])

for i in songs:
    if(i[0] in "AEIOUaeiou"):
        vSongs.append(i)
    else:
        cSongs.append(i)

print("Songs Titles starting with vowel",vSongs)
print("Songs Titles starting with consonants",cSongs)