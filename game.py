import numpy as np
import random

class Game:
	def __init__(self):
		self.row = 4
		self.col = 4
		self.setup()
		while True:
			legal = self.get_legal_moves()
			print(legal)
			if not legal:
				print("Game over!")
				exit()
			m = self.get_move()
			if m not in legal:
				print("Illegal move. Please input another move.")
				continue
			self.shift_board(m)				
			self.spawn_tile()
			self.show_board()

	def setup(self):
		self.board = np.zeros(shape=(self.row, self.col), dtype=int)
		self.spawn_tile()
		self.spawn_tile()
		self.show_board()

	def spawn_tile(self):
		empty_spots = []
		for i in range(self.row):
			for j in range(self.col):
				if self.board[i, j] == 0:
					empty_spots.append([i, j])
		# DEBUG
		assert(empty_spots)
		new_spot = random.choice(empty_spots)

		new_tile = random.choices([2, 4], weights=[9, 1])[0]
		self.board[new_spot[0], new_spot[1]] = new_tile

	def show_board(self):
		for row in self.board:
			print(*row, sep="|")

	def get_move(self):
		return input("input an direction wasd style...")

	def get_legal_moves(self):
		legal = set()
		for i in range(self.row - 1):
			for j in range(self.col):
				if self.board[i, j] != 0 and self.board[i + 1, j] != 0 and self.board[i, j] == self.board[i + 1, j]:
					legal.update(['w', 's'])
				elif self.board[i, j] != 0 and self.board[i + 1, j] == 0:
					legal.add('s')
				elif self.board[i, j] == 0 and self.board[i + 1, j] != 0:
					legal.add('w')
		for j in range(self.col - 1):
			for i in range(self.row):
				if self.board[i, j] != 0 and self.board[i, j + 1] != 0 and self.board[i, j] == self.board[i, j + 1]:
					legal.update(['a', 'd'])
				elif self.board[i, j] != 0 and self.board[i, j + 1] == 0:
					legal.add('d')
				elif self.board[i, j] == 0 and self.board[i, j + 1] != 0:
					legal.add('a')
		return legal

	
	def shift_array(self, arr, to_front):
		arr = arr if to_front else arr[::-1]
		new_arr = np.zeros(arr.shape, dtype=int)
		new_pos = 0
		can_merge = False
		for i in range(arr.size):
			if arr[i]:
				if can_merge and arr[i] == new_arr[new_pos-1]:
					new_arr[new_pos-1] *= 2
					can_merge = False
				else:
					new_arr[new_pos] = arr[i]
					new_pos += 1
					can_merge = True
		return new_arr if to_front else new_arr[::-1]

	def shift_board(self, m):
		if m == 'w':
			for j in range(self.col):
				self.board[:, j] = self.shift_array(self.board[:, j], to_front=True)
		elif m == 's':
			for j in range(self.col):
				self.board[:, j] = self.shift_array(self.board[:, j], to_front=False)
		elif m == 'a':
			for i in range(self.row):
				self.board[i, :] = self.shift_array(self.board[i, :], to_front=True)
		elif m == 'd':
			for i in range(self.row):
				self.board[i, :] = self.shift_array(self.board[i, :], to_front=False)

def main():
	Game()

if __name__ == "__main__":
	main()