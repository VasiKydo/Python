l = {'τραπέζι' : 'table' , 'καρέκλα' : 'chair', 'σκύλος' : 'dog' , 'γάτα' : 'cat' ,  'κούκλα' : 'doll' ,  'υπολογιστής' : 'computer' }
sosta = lathos = 0
for leksi in l.keys():
 print (leksi, end=':')
 a = input()
 if a==l[leksi]:
   print('bravo')
   sosta+=1
 else:
   print ('lathos, i sosti apantisi einai:', l[leksi])
   lathos+=1

print('se synolo', sosta+lathos, 'erotiseon brikes', sosta, 'sostes lekseis')
