import multiprocessing
from dataprovider.frameprovider import provider_run
class master:
	def __init__ (self,config=None):
		pass;

	def run(self,config):
		# step 1 get the json infos and convet it into the training lists
		f = open(self.data_json)
		infos  = f.readlines()
		print(infos)

		# step2 create the data provider
		p_all = []
		read_process = []
		for provider in self.provider_list:
#			for i in range(config.num_provider_thread):
			read_process.append(multiprocessing.Process(target=provider.run))

		for p in read_process:
			p_all.append(p)
			p.start()


		# step3 create the trainer
		training_process = multiprocessing.Process(target=self.trainer.run)
		training_process.start()


		# step4 feed the cut params
		for i, item in enumerate(infos):
			self.queue_list[i % len(self.queue_list)].put((item))

#		for info in infos:
#			for q in self.queue_list:
#				print(info)
#				q.put((info))

		for q in self.queue_list:
			q.put(None)

		for p in p_all:
			p.join()

		for q in self.queue_out_list:
			q.put(None)

		training_process.join()


	def set_training(self,data_json,queue_list,queue_out_list,provider_list,trainer,config):
		self.data_json = data_json
		self.provider_list = provider_list
		self.trainer = trainer
		self.queue_list = queue_list
		self.queue_out_list = queue_out_list


