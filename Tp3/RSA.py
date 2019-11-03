import random
import time 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def modexp (b, e, m):
	res = 1
	b = b % m
	while e != 0:
		if e & 1 == 1:
			res = (res * b) % m
		b = (b * b) % m
		e >>= 1
	return res

if __name__ == '__main__':

	q = 153913992087337632323856325535167134698095080265487697782446283149626790922054338896603372601701248192800221006576347314040816659302976199762035470757122629463456678269133200480357169321736362760934788789190740182901256963860061869620481609960370510030714750089180702939732729221296257214940229289705438006879
	p = 158830509839483660538353412378447400700107210968900092239591179911128667705234925924251344045049717336769031554144041134728268846983368928546770796843344423778338023815172845840730580759322444317036651307764297790101711811434976591831902924379463292108663467379931846166559498777380964112289086944467540107473
	𝑒 = 65537
	n = p * q

	phi_n = (p - 1) * (q - 1)
	d = modinv(e,phi_n)
	i = 0
	message = random.getrandbits(2048)
	print("message: ",message)

	start_t = time.time()
	while(i != 100):

		mc = modexp(message, d, n)
		print("Le message chiffre est: ",mc)
		i +=1

	end_t = time.time()
	total = end_t - start_t
	print("temp = ",total)

	md = modexp(mc, e, n)
	print("Le message dechiffre est : ",md)