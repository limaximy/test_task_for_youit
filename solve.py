def set_default_test(): # Функция для загрузки в файл данных по умолчанию
	f = open("test.txt", "w") # открытие файла
	f.write("4\n5 3\nBBWBW\n5 5\nBBWBW\n5 1\nBBWBW\n1 1\nW") # загрузка данных
	f.close() # закрытие файла

def take_difference(cells, inp): # функция для нахождения количества различающихся элементов в двух строках
	min_cnt = 2 * 10**5 + 1 # установка максимального значения по условию
	buf_cnt = 0 
	for i in range(len(cells) - len(inp) + 1): # цикл прохода требуемого отрезка по изначальной строке без выхода за границы 
		for j in range(len(inp)): # цикл проверки каждого символа
			if cells[i+j] != inp[j]: # условие для поиска минимального значения
				buf_cnt += 1
		if buf_cnt < min_cnt: # обновление минимального значения
			min_cnt = buf_cnt
		buf_cnt = 0

	return min_cnt # возврат минимального количества различающихся элементов в двух строках


def algorithm():
	f = open("test.txt", "r")
	lines = f.readlines()
	f.close()

	lines = list(map(lambda x:x.rstrip('\n'), lines)) # обрезка полученных из файла данных
	# rstrip функция обрезки у строки справа 
	# lambda нужна, т.к. rstrip метод класса строк
	# map применяет lambda функцию к каждому элементу lines
	# list нужен для преобразования результата map в список


	num_all = int(lines[0]) # количество блоков данных

	for i in range(num_all):
		lll = lines[1 + i*2].split(' ') # split преобразовывает строку в список с определенным разделителем

		n = int(lll[0]) 
		k = int(lll[1])
		cells = lines[2 + i*2]
		
		inp_cells = 'B' * k

		print(take_difference(cells, inp_cells)) # вызов функции


set_default_test()
algorithm()

