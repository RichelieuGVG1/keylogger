input('Пока проверь, что рядом с разжмышером лежит файл lib.dll, который и является шифром. Как убедишься, нажми Enter.')

def denana(cipher):
	cipher=list(map(lambda byte: bin(byte)[2:].rjust(8,'0'),cipher))
	stack=''
	plain=[]
	i=0
	while i<len(cipher):
		byte=cipher[i]
		if byte[0]=='1':
			stack+=byte[1:]
		else:
			tail=int(cipher[i+1],2)
			plain.append(stack+byte[-tail:])
			stack=''
			i+=1
		i+=1
	return list(map(lambda num: int(num,2),plain))


with open('lib.dll','rb') as file:
	data=file.read()
data=list(map(lambda byte: (byte+54)%256,data))
data=denana(data)
log=[]
for i in range(0,len(data),2):
	key,time=data[i:i+2]
	key=chr(int(key**0.5))
	time=str((time-228)//54)
	time=time[:4]+'-'+time[4:6]+'-'+time[6:8]+'-'+time[8:10]+'-'+time[10:12]+'-'+time[12:14]
	log.append(f'({key}, {time})')

with open('log.txt','w',encoding='utf-8') as out:
	out.write('\n'.join(log))

print('Разжмышено успешно.')