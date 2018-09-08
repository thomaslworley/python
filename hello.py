import sys


def main():
	name = input("Please type your name: ")
	if name is not None:
		print('Hello %s!' % name)

	name = input("What day is it?")
	if name is not None:
		print('Do you have anything to do this %s?' % name)


	if __name__ == '__main__':
		main()

