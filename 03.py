# ========================================================================================================
# Gross National Product ASEAN
# ========================================================================================================

import mysql.connector 
import matplotlib.pyplot as plt

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
    populasiAsean.append(i[8])

plt.style.use('seaborn')

warna = ['black', 'blue', 'green', 'red', 'yellow', 'cyan', 'pink', 'grey', 'brown', 'lightblue', 'lightgreen']
plt.bar(negaraAsean, populasiAsean, color = warna) 


for titik in range(len(negaraAsean)):
    plt.text(negaraAsean[titik], populasiAsean[titik], populasiAsean[titik], ha='center', va='bottom')

plt.title('Pendapatan Bruto Nasional ASEAN')    
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
plt.xticks(rotation = 45)
plt.subplots_adjust(bottom=.18, right=.93)
plt.tight_layout() 

plt.show()