"""converting decimal to binary.

@author Midhun Nair
"""

def decimal_to_bonary(number:int):
	if number >= 1:
		decimal_to_bonary(number // 2)
	print(number % 2, end = "")

if __name__ == "__main__":
	decimal_to_bonary(5)