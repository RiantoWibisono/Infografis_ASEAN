# ========================================================================================================
# Persentase Populasi ASEAN
# ========================================================================================================

import mysql.connector 
import matplotlib.pyplot as plt
import numpy as np 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'RiantoWibisono',
    passwd = 'Rianto12345',
    database = 'world'
)

mycursor = mydb.cursor()
mycursor.execute('select * from daftarasean order by name')
hasil = mycursor.fetchall()

negaraAsean = []
populasiAsean = []
for i in hasil:
    negaraAsean.append(i[1])
    populasiAsean.append(i[6])

warna = ['black', 'lightblue', 'green', 'red', 'yellow', 'cyan', 'pink', 'grey', 'brown', 'blue', 'lightgreen']
autotexts = plt.pie(populasiAsean, labels=negaraAsean, colors=warna,
    autopct='%1.1f%%',
    textprops={'fontsize': 8})

plt.title('Persentase Penduduk ASEAN') 
plt.tight_layout()   

plt.show()
