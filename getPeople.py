import requests

#inisialisasi
page       = 5
url        = "https://swapi.co/api/"
processA   = ['films','species','vehicles','starships',]
processB   = ['homeworld','url']
maxPerFile = 15
directori  = 'output/'
#get Data dan memasukan dalam 1 variabel untuk diolah
data = []
for i in range(1,page+1):
    objek = requests.get(url+'people/?page='+str(i)).json()['results']
    [data.append(objek[n]) for n in range(len(objek))]
print(len(data))

#prepocessing (Menyederhanakan URL)
for i in range(len(data)):
    for x in processA:
        for y in range(len(data[i][x])):
            data[i][x][y] = data[i][x][y][len(url):]
    for x in processB:
        data[i][x] = data[i][x][len(url):]

#grouping : mencari jenis homeworld dan  gender dari data
gender    = []
homeworld = []
group     = {}

for i in range(len(data)):
    if data[i]['homeworld'] not in group.keys():
        group[data[i]['homeworld']] = {}
    if data[i]['gender'] not in group[data[i]['homeworld']].keys():
        group[data[i]['homeworld']][data[i]['gender']] = []
    group[data[i]['homeworld']][data[i]['gender']].append(data[i])

#membuat file untuk menyimpan hasil grouping
list = open('list','w')
for i in group.keys():
    for j in group[i]:
        num = (len(group[i][j])//maxPerFile) + 1
        for idx in range(num):
            temp = i+'_'+j+'_'+str(num)+'.json'
            temp = temp.replace('/','#')
            temp = directori+temp
            list.write(temp+'\n')
            file = open(temp,'w')
            results = {}
            results['results'] = []
            for x in range(len(group[i][j])):
                results['results'].append(group[i][j][x])
                #file.write(str(group[i][j][x])+'\n')
            file.write(str(results).replace("'",'"'))
            file.close()


list.close()




