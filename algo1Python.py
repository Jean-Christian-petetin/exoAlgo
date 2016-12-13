#cet algo sert a calculer l'age (en années uniquement) d'une personne en se basant sur deux date complete (dd/mm/yyyy).

actualYear = 2016
actualMonth = 12
actualDay = 13

birthYear = 1982
birthMonth = 9
birthDay = 28

age = actualYear - birthYear

if actualMonth < birthMonth:
	age -= 1
	
elif actualMonth == birthMonth:
	if actualDay < birthDay:
		age -= 1

print age
