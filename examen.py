def run():
	dic_x = {value*2 : value for value in range(1,5) if value % 2 != 0}
	print(dic_x)

	list_x = list({"1" : 29})
	print(list_x)

	list_y = [i for i in range(1,5) if i % 2 == 0]
	print(list_y)
	
if __name__ == '__main__':
	run()