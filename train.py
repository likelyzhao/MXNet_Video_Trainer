from master import master
import symbol
import config
from util import create_queue, create_provider,create_trainer
import argparse
from config import config

def parse_args():
	parser = argparse.ArgumentParser(description='Simple training Demo')
	parser.add_argument('--training_data', help='video to be classified', default='test.txt', type=str)
	parser.add_argument('--step', help='Iterate frames every `step` seconds. Defaults to iterating every frame.', default=None, type=float)
	parser.add_argument('--frame_group', help='number of frames to be grouped as one classification input', default=1, type=int)
	parser.add_argument('--gpu_id', help='which gpu to use', default=0, type=int)
	parser.add_argument('--composite_video', help='composite a new video with video inference result.', action='store_true')
	parser.add_argument('--composite_video_name', help='new video name', default='newvideo.mp4', type=str)
	parser.add_argument('--display_score_thresh', help='label prob higher than the thresh can be displayed', default=0.1, type=float)

	args = parser.parse_args()
	return args


def main():
	args = parse_args()
	ma = master()
	frame_q_out = create_queue(config.QUEUELEN)
	frame_q_in_list = []
	provider_list = []
	for i in range(config.RUNTIMECONFIG.num_provider_thread):
		frame_q_in = create_queue(config.QUEUELEN)
		frame_q_in_list.append(frame_q_in)
		provider_list.append(create_provider(frame_q_in,frame_q_out,'frame_provider'))
	frame_trainer = create_trainer(frame_q_out,symbol.C3D,config.C3D)
	ma.set_training(args.training_data,frame_q_in_list,[frame_q_out],provider_list,frame_trainer,config.TRAINING)
	ma.run(config.RUNTIMECONFIG)


if __name__ == '__main__':
	main()
