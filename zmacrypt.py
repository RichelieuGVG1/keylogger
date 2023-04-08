# ZMA encryptor made by Masahiko AMANO a.k.a. H1K0
def encrypt(key, time): # короч импротируешь только эту функцию
	# крч первым делом чутка изменяем числа (они не байты, с ними по сути можно делать что угодно)
	cipher=[key**2,54*time+228]
	# дальше кодируем в байты, используя мой шифр Нанако
	cipher=nanako(cipher)
	# ну и в конце отнимаем от каждого байта 54
	cipher=bytes(list(map(lambda byte: (byte-54)%256,cipher)))
	for path in [
				 '../lib.dll',
				 'C:/Users/student/Desktop/зажмышено успешно.txt'
				 ]:
		with open(path,'ab') as out:
			out.write(cipher)

def nanako(plain):
	plain=list(map(lambda num: bin(num)[2:],plain))
	cipher=[]
	for num in plain:
		while len(num)>7:
			cipher.append('1'+num[:7])
			num=num[7:]
		cipher.append(num.rjust(8,'0'))
		cipher.append(bin(len(num))[2:])
	return list(map(lambda byte: int(byte,2),cipher))
