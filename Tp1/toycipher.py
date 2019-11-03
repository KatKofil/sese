import random

sbox = [9, 0xb, 0xc, 4, 0xa, 1, 2, 6, 0xd, 7, 3, 8, 0xf, 0xe, 0, 5]

# EX1.3 - la boîte S inversée
xobs = [0xe, 5, 6, 0xa, 3, 0xf, 7, 9, 0xb, 0, 4, 1, 2, 8, 0xd, 0xc]

nbtour = 0

# EX1.1 - la fonction de tour
def round (state, key):
	global nbtour
	nbtour = nbtour + 1
	t = state ^ key
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

# EX3.2 - fait la parite
def parite(pair_mask):
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

# EX3.3 - trouve les meilleurs masks
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

# EX4.3 - trouve des candidats pour ko
def find_ko(pairs, top_masks):
	n = 16
	t = [[0] * n for _ in range(n)]
	count = 0
	res = []
	for i in pairs:
		for k in range(n):
			tmp = k ^ pairs[i][0]
			t[i][k] = sbox[tmp]

	for i in pairs:
		for k in range(n):
			res_in = bin(t[i][k] & top_masks[0]).count('1')
			res_out = bin(pairs[i][1] & top_masks[1]).count('1')
			if res_in %2 == res_out %2:
				count = count +1
			if count == 2 or count == 14:
				res.append(k)
				
	return res

# EX5.2 - trouve la cle
def search_key(potential_ko, pairs):
	msg = pairs[0][0]
	print("MESAGE",msg)
	for i in potential_ko:
		count = 0
		encrypted_msg = round(msg, i)
		xobs1 = xobs[pairs[0][1]]
		k1 = xobs1 ^ encrypted_msg
		for j in pairs:
			test_encrypted = enc(pairs[j][0] , [i, k1])
			#print("encrypted: ",test_encrypted)
			#print(pairs[j][1])
			#print("")
			if test_encrypted == pairs[j][1]:
				count = count + 1
		if count >= 15:
			print("la cle trouvé est : ko=", i, " k1 =", k1)
			break
		else:
			print("la cle k0=",i, " n'est pas bonne")
	
	
if __name__ == '__main__':
	# Generate random key
	key = (random.randint(0, 15), random.randint(0, 15))
	# Generate message
	msg = 3
	# Generate encrypted message
	sortie = enc(msg,key)
	
	nbtour = 0

	# EX2.5.a
	#find_key(key, msg, sortie)

	# EX4.1 - Generate pairs
	pairs = list_of_pairs(key, 16)
	print("16 paires de message/chiffré :")
	print(pairs)
	
	# Generate masks
	mask_in, mask_out = generate_masks()
	les_pairs = pair_masks(mask_in, mask_out)
	#print("Tous les masks :")
	#print(les_pairs)

	# Parite
	parity = parite(les_pairs)
	print("Parite pour chaque mask :")
	print(parity)

	# Best pair
	top_masks = best_mask(parity)
	print("Meilleures mask :")
	print(top_masks)
	print("Les best paires pour une parité sont: ")
	for i in top_masks:
		print(les_pairs[i])

	#print(nbtour)

	# trouver les k0 potentiels
	potential_ko = find_ko(pairs, les_pairs[187])
	print(potential_ko)
	
	# trouver la cle potentiel
	search_key(potential_ko, pairs)
	print(key)
