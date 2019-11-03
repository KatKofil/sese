affiche:
	mov r1 #27
	mov r2 #28
	mov r3 #29
	prn r1
	prc #32
	prn r2
	prc #32
	prn r3
	prc #10
	ret

change:
	mov r1 #27
	prn r1
	prc #32
	mov r1 #28
	prn r1
	prc #10
	ret

use_instr:
	mov r1 #27
	mov r2 #28
	add r3 r1 r2
	prn r3
	prc #32
	not r4 r3
	prn r4
	prc #32
	xor r5 r4 r3
	prn r5
	prc #10
	ret

hello:
	prc #72
	prc #101
	prc #108
	prc #108
	prc #111
	prc #32
	prc #87
	prc #111
	prc #114
	prc #108
	prc #100
	prc #33
	prc #10
	ret 

condition:
	mov r29 r31
	mov r1 #1
	mov r2 #2
	beq hello r1 r2
	mov r31 r29
	ret

boucle:
	mov r1 #10
	mov r29 r31
debut:
	beq fin r1 #0
	sub r1 r1 #1
	cal hello
	jmp debut
fin:
	mov r31 r29
	ret

main:
	cal affiche
	;cal change
	;cal use_instr
	;cal hello
	;cal condition
	;cal boucle
