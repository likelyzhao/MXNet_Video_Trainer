


class trainer():
	def __init__(self,queue_in , symbol,params):
		self.q_in = queue_in
		self.symbol = symbol
		self.params = params

	def run(self):
		while True:
			deq = self.q_in.get()
			if deq is None:
				print("recive None")
				break

			item = deq
			print("training + " + item)

