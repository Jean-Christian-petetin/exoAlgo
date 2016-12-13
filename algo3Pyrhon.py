#cette algo trouve une lettre défini dans un mot et affiche le nombre de fois ou la lettre apparait dans le mot.

word = "anticonstitutionnellement"
char = "n"
result = 0
i = 0

while i < len(word):
	if word[i] == char:
		result += 1
	i += 1

print result
