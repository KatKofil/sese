import random

sbox = [9, 0xb, 0xc, 4, 0xa, 1, 2, 6, 0xd, 7, 3, 8, 0xf, 0xe, 0, 5]

# EX1.3 - la boîte S inversée
xobs = [0xe, 5, 6, 0xa, 3, 0xf, 7, 9, 0xb, 0, 4, 1, 2, 8, 0xd, 0xc]

nbtour = 0

# EX1.1 - la fonction de tour
def round (state, rk):
	global nbtour
	nbtour = nbtour + 1
	t = state ^ rk
	return sbox[t]

# EX1.2 - l'algorithme de chiffrement
def enc (msg, key):
    t0 = round(msg, key[0])
    t1 = round(t0, key[1])
    return t1

def simplified_enc (msg, key):
    t0 = round(msg, key[0])
    return t0 ^ key[1]

# EX2.5.a - mise en oeuvre de la méthode pour formuler l'hypothèse
def find_key(key, msg, sortie):
	global nbtour
	for i in range(0, 16):
		for j in range(0, 16):
			res = enc(msg,[i,j])
			if res == sortie:
				print("clé trouvé : %x, %x" %(i,j))
				if i == key[0] and j == key[1]:
					print(" c'était celle-là la bonne : %x %x, %x %x" %(i,j,key[0],key[1]))
					nb_good_key = nbtour
					print(nb_good_key)
				else:
					print("c'était une collision..\n")

# EX2.6 - renvoie n paires de message aléatoirement choisi et du chiffré correspondant avec la clef donnée
def list_of_pairs(key, n):
	pairs = {}
	for i in range(0, n):
		msg = (random.randint(0, 15))
		pairs[msg] = enc(msg,key)
	return pairs

if __name__ == '__main__':
	key = (random.randint(0, 15), random.randint(0, 15))
	msg = 3
	sortie = enc(msg,key)
	nbtour = 0
	#find_key(key, msg, sortie)
	pairs = list_of_pairs(key, 10)
	print(pairs)
	#print(nbtour)
	
	
