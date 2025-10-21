precios_frutas={'Banana':1200,'Ananá':2500,'Melón':3000,'Uva':1450}
precios_frutas.update({'Naranja':1200,'Manzana':1500,'Pera':2300})
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
frutas=list(precios_frutas.keys())
print('Punto 1-3:',precios_frutas,frutas)

phone={}
print('Cargar 5 contactos en formato Nombre,numero')
for _ in range(5):
    try:
        s=input().strip()
        if not s: continue
        n,num=s.split(',')
        phone[n.strip()]=num.strip()
    except:
        continue
q=input('Buscar nombre: ').strip()
print(phone.get(q,'No existe'))

s=input('Frase: ')
words=[w.strip().lower() for w in s.split() if w.strip()]
print('Palabras únicas:',set(words))
from collections import Counter
print('Conteo:',dict(Counter(words)))

for _ in range(3):
    name=input('Alumno nombre: ').strip()
    notas=list(map(float,input('3 notas separadas por espacio: ').split()))
    avg=sum(notas)/len(notas) if notas else 0
    print(name,round(avg,2))

a=set(map(int,input('Set1 nums separados por espacio: ').split()))
b=set(map(int,input('Set2 nums separados por espacio: ').split()))
print('A y B:',sorted(a&b))
print('Solo uno:',sorted(a^b))
print('Al menos uno:',sorted(a|b))

stock={'lapiz':10,'cuaderno':5,'goma':3}
stock['cuaderno']-=2
stock['regla']=stock.get('regla',0)+1
stock['goma']=0
print('Stock:',stock)

agenda={('2025-01-01','09:00'):'Reunion'}
dici={'Argentina':'Buenos Aires','Chile':'Santiago'}
invertido={v:k for k,v in dici.items()}
print('Invertido:',invertido)
