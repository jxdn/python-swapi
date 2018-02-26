## Get Data and Grouping Swapi

### File
* [getPeople.py](https://github.com/jxdn/python-swapi/blob/master/getPeople.py)   :  Proses mendapatkan data, memprosessnya (menghilangkan Url yang terlalu panjang) dan melakukan grouping berdasarkan homeworld dan gender
* [Output](https://github.com/jxdn/python-swapi/tree/master/output) : Folder untuk menyimpan hasil grouping dalam bentuk json
* [README.md](https://github.com/jxdn/python-swapi/blob/master/README.md)   : Manual


### CARA PENGGUNAAN
* buat folder output jika tidak ada
* Jalankan saja [getPeople.py](https://github.com/jxdn/python-swapi/blob/master/generate.py) 

## Keterangan :
Format nama file ex: planets#1#_female_1
* planets#1# : menunjukan homeworld (berasal dari https://https://swapi.co/api/planets/1, penamaan file tidak dapat menggunakan '/') 
* female   : jenis kelamin
* 1   : jumlah file (karena maksimal 1 homeworld 1 gender hanya 15 anggota )
