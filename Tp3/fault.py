#Ayadi Emna 16700056 Exercice 3
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

n = 47775493107113604137
s = 0x3f010be37eb5eca9
s_b = 0x7323fd5ef5440fbc
e = 17

r_s = s - s_b
p_q =egcd(n,r_s)[0]
print(p_q)

q_p = n // p_q
print(q_p)

phi_n = (p_q - 1) * (q_p - 1)
d = modinv(e,phi_n)
print(d)

