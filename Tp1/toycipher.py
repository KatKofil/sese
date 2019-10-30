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
		pairs[i] = (msg, enc(msg,key))
	return pairs

# Génère les masks
def generate_masks():
	mask_in = []
	for i in range(0, 16):
		mask_in.append(i)
	mask_out = mask_in
	return mask_in, mask_out

# EX3.2 - calcule pour les couples(maski, masko)
def pair_masks(mask_in, mask_out):
	pair_mask = {}
	k = 0
	for i in range(0,16):
		for j in range(0,16):
			pair_mask[k] = (mask_in[j], mask_out[i])
			k = k+1
	return pair_mask

# EX3.3 - trouve la meilleure paire
def parite(key, pair_mask):
	res = []
	for i in pair_mask:
		res.append(0)
		for j in range(0,16):
			mask = pair_mask[i]
			res_in = bin(j & mask[0]).count('1')
			res_out = bin(sbox[j] & mask[1]).count('1')
			if res_in %2 == res_out %2:
				res[i] = res[i] +1
	return res

# EX3.3 - trouve la meilleure paire
def best_mask(res):
	tmp = 0
	ret = []
	for i in range(1,len(res)):
		if res[i] > tmp:
			tmp = res[i]
			ret.clear()
			ret.append(i)
		elif res[i] == tmp:
			ret.append(i)
	return ret

if __name__ == '__main__':
	# Generate random key
	key = (random.randint(0, 15), random.randint(0, 15))
	# Generate message
	msg = 3
	# Generate encrypted message
	sortie = enc(msg,key)
	
	nbtour = 0

	#find_key(key, msg, sortie)

	# Generate pairs
	pairs = list_of_pairs(key, 16)
	print(pairs)
	
	# Generate masks
	mask_in, mask_out = generate_masks()
	les_pairs = pair_masks(mask_in, mask_out)
	#print(les_pairs)

	# Parite
	res = parite(key, les_pairs)
	print(res)

	# Best pair
	res2 = best_mask(res)
	print(res2)
	print("Les best mask pour une parité sont: ")
	for i in res2:
		tmp = les_pairs[i]
		print(tmp)

	#print(nbtour)
	
	
