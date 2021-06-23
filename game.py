import random

class Game:
	def __init__(self):
		self.setup()
		while True:
			input("press enter to continue...")
			self.show_board()
			self.spawn_tile()	
		
	def setup(self):
		self.board = [[0 for j in range(4)] for i in range(4)]
		self.spawn_tile()
		self.spawn_tile()

	def spawn_tile(self):
		empty_spots = []
		for i in range(4):
			for j in range(4):
				if self.board[i][j] == 0:
					empty_spots.append([i, j])
		# DEBUG
		assert(empty_spots)
		new_spot = random.choice(empty_spots)

		new_tile = random.choices([2, 4], weights=[9, 1])[0]
		self.board[new_spot[0]][new_spot[1]] = new_tile

	def show_board(self):
		for row in self.board:
			print(*row, sep="|")
	


def main():
	Game()

if __name__ == "__main__":
	main()