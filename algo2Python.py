# cet algo sert a trier des nombres dans un tableau dans l'ordre croissant.

tableau = [3,25,1,6,23,56]
switch = ""
sorted = "false"

while sorted == "false":
	moved = "false"
	i = 0
	while i < len(tableau):
		if tableau[i+1] < tableau[i]:
			switch = tableau[i]
			tableau[i] = tableau[i+1]
			tableau[i+1] = switch
			moved = true
	i += 1

	if moved == "false":
		sorted = "true"

print tableau
