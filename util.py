import multiprocessing
from dataprovider import frameprovider
from trainer import trainer


def create_queue(queue_len):
	return multiprocessing.Queue(queue_len)
	pass;


def create_provider(queue_in, queue_out, provide_type):
	if provide_type == "frame_provider":
		provider = frameprovider(queue_in,queue_out)
		return provider



def create_trainer(queue_in, symbol, config):
	return trainer(queue_in,symbol,config)

	pass;