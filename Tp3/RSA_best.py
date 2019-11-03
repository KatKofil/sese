# Ayadi Emna 16700056 Exercice 2
import random
import time 


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, modulo):
    g, x, y = egcd(a, modulo)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % modulo

def modexp (base, puissance, modulo):
	res = 1
	base = base % modulo
	while puissance != 0:
		if puissance & 1 == 1:
			res = (res * base) % modulo
		base = (base * base) % modulo
		puissance >>= 1
	return res



p = 178655983816562256022408092633422595713229107114519518605896607081251752416328869605529671823778041606438375282652300454455710405067116463343031940742450604977296076806651049403592029426173609044020114342966120917054579340511624555884118062875992540479181371532898389769308203352500335383970181386455599273743
q = 176971306794047764150323685671937496182886713210614637864922648834239445521454421085736049372770691546509598662869330547799522521030080715949305569792630508260506069671578338543338755329805493383257333284700846667530105830998001733633149574832756755997234103673286233544270901824671021881678072519234331575963
𝑒 = 65537
n = p * q

def chiffre(message, p,q,d_p,d_q,i_q):
	s_p = modexp(message,d_p,p)
	s_q = modexp(message,d_q,q)
	return s_q + q*(i_q*(s_p - s_q)% p)

        

def dechiffre(secret, clededechiffrement):
        return modexp(secret, clededechiffrement, n)


phi_n = (p - 1) * (q - 1)
d = modinv(e,phi_n)
d_p = d%(p-1)
d_q = d%(q-1)
i_q = modinv(q,p)
i = 0

message = random.getrandbits(2048)
print("message: ",message)
print("\n")

start_t = time.time()
while(i != 100):

	message_chiffre = chiffre(message,p,q,d_p,d_q,i_q)
	print("Message chiffre: ",message_chiffre)
	print("\n")
	i +=1 

end_t = time.time()
total = end_t - start_t
print("Temp = ",total)

message_dechiffre = dechiffre(message_chiffre,e)
print("Message dechiffre ",message_dechiffre)
print("\n")




