# Бинго-сортировка - https://habr.com/ru/post/422085/
def bingo(data):
	max = len(data) - 1
	nextValue = data[max]
	for i in range(max - 1, -1, -1):
		if data[i] > nextValue:
			nextValue = data[i]

	while max and data[max] == nextValue:
		max -= 1

	# Последующие проходы.

	while max:
		value = nextValue
		nextValue = data[max]
		for i in range(max - 1, -1, -1):
			if data[i] == value:
				data[i], data[max] = data[max], data[i]
				max -= 1
			elif data[i] > nextValue:
				nextValue = data[i]
		while max and data[max] == nextValue:
			max -= 1

	return data
