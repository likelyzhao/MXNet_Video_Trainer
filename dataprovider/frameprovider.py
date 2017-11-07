


def provider_run(dataprovider):
	dataprovider.run()


class dataprovider():
	def __init__(self):
		pass

	def run(self):
		pass


class frameprovider(dataprovider):

	def __init__(self,queue_in,queue_out):
		self.q_in = queue_in
		self.q_out = queue_out
		pass

	def run(self):
		while True:
			deq = self.q_in.get()
			if deq is None:
				print("provider recive None")
				print("provider put None")
				break
			item = deq
			print("frame " + str(item))


			self.q_out.put("frame + " + item)

