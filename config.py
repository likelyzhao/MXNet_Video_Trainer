from easydict import EasyDict as edict

config = edict()
config.QUEUELEN = 1024

config.TRAINING = edict()
config.C3D = edict()
config.RUNTIMECONFIG = edict()
config.RUNTIMECONFIG.num_provider_thread = 10

config.FEATURE_CODING = edict()
config.FEATURE_CODING.MODEL_PREFIX = 'models/netvlad'
config.FEATURE_CODING.MODEL_EPOCH = 50
config.FEATURE_CODING.FEATURE_DIM = 512
config.FEATURE_CODING.SYNSET='lsvc_class_index.txt'