def is_palin(word):
	return word == word[::-1]

def str_02(word):
  return word[:2] + word[-2:]

def str_03(tpl):
	return (tpl[2], tpl[-5])

def str_04(list):
	return not list

def str_05(list):
	return "".join(list)

def str_06(list):
	list.sort()
	return list[1]

def str_07(dic):
	return (dic["teste"] if "teste" in dic else "Error")


if __name__ == "__main__":
	print(is_palin("radar"))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(is_palin("abc"))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_02("abcde"))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_03((1,2,3,4,5,6,7,8)))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_04([]))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_04([1, 2]))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_05(["aa", "cc"]))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_06([1, 5, 6, 3, 10]))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_07({"one":"two", "teste":"aew"}))
	print("=-=-=-=-=-=-=-=-=-=-=-")
	print(str_07({"one":"two", "s":"aew"}))


