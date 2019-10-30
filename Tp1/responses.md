# TPs SESE

## Exercice 2

### 1a)

- Les attaque de type KPA (known-plaintext attack)

### 1b)

En supprimant un tour on reduit le probleme a un simple xor qui nous permet de récupérer K0:
    - T0 = msg ^ K0
    - T'0 = sbox[T0] or nous possédons la sbox inversée.
    - d'où  K0 = msg ^ T0 où T0 = xobs[T'0]

### 2

On ne peut pas répété deux fois l'opération suivante car on ne connait pas T'0. On ne peut donc pas inversé la sbox.

## 3a)

Oui le nombre de clefs est raisonnable, il est seulement de 16.

### 3b)

Il est possible des toutes les essayer mais ce serais une perte d'energie et de temps pour la réusite de l'attack. Le temps mis pour récupérer les inforamtions exèderais surment la validitée de celles-ci.

### 4

Il faudrais 2⁸ * 2 (512) étapes au maximum pour réaliser un brute force sur notre algorithme de chiffrement.
Par contre pour tester le brute force nous serons obligé de passer à une attack de type CPA, une "pause déjeuné" devrais suffir si l'on récupère 256 message.

**réponse après questions 5**

Il faut donc 2⁸ * 2 * 16 itération maximun pour toruver la clef du fait des nombreuse colition on dois donc créé un protocole permetant de retiré les colision. Pour cela on peut les créé 16 msg possible au quel on appliquera la meme méthode.

### 5b)

Nous remarquons que la méthode brute force fonctionne mais que le nombre de collition est important pendant les testes.

### 5c)

Notre première hypothèse est réfuté car le nombre de colision étant important on ne peut que réduire le nombre de clef possible. Et pas trouver la bonne. En seulement 512 itération.

## Exercice 3

### 1

La fonction de tour n'est pas lineaire du fait de la présnece d'une boite de supstitution dont la fonction est justement de casser la linéarité du cryptosystème.
