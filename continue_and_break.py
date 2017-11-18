x = 1

while (x <= 200):
	if (x % 2) == 0:
		x += 1
		continue

	if x == 15:
		break

	print("Odd : ", x)

	x += 1