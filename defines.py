from datetime import datetime
PARAM_ACTION = 1 							# 1 for training, 2 for testing
#PARAM_CP = 1								# 1 for cartesian, 2 for polar
PARAM_BATCHES = 2
PARAM_N_EPOCHS = 50
PARAM_N_TESTS = 100
PARAM_EPOCH_STEPS = 100
PARAM_BETA1 = [0.2, 0.4, 0.6, 0.4]
PARAM_BETA2 = [0.8, 0.4, 0.8, 0.999]

PARAM_SAVE_BEST_ONLY = True
PARAM_SYSTEM_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")
PARAM_PATH_TRAIN_C = './data/endoscopic/cartesian/train'
PARAM_AUG_FOLDER_C = './data/endoscopic/cartesian/train/aug_' + PARAM_SYSTEM_TIME
PARAM_PATH_TEST_C =  './data/endoscopic/cartesian/test'
PARAM_PATH_TEST_RESULTS_C = './data/endoscopic/cartesian/test/predict_' + PARAM_SYSTEM_TIME
PARAM_PATH_TEST_NPY_C = './data/endoscopic/cartesian/test/predict_' + PARAM_SYSTEM_TIME + '.npy'
PARAM_PATH_TEST_ALL_IMG_C = './data/endoscopic/cartesian/test/predict_' + PARAM_SYSTEM_TIME + '.png'
PARAM_PATH_TRAIN_P = './data/endoscopic/polar/train'
PARAM_AUG_FOLDER_P = './data/endoscopic/polar/train/aug_' + PARAM_SYSTEM_TIME
PARAM_PATH_TEST_P =  './data/endoscopic/polar/test'
PARAM_PATH_TEST_RESULTS_P = './data/endoscopic/polar/test/predict_' + PARAM_SYSTEM_TIME
PARAM_PATH_TEST_NPY_P = './data/endoscopic/polar/test/predict_' + PARAM_SYSTEM_TIME + '.npy'
PARAM_PATH_TEST_ALL_IMG_P = './data/endoscopic/polar/test/predict_' + PARAM_SYSTEM_TIME + '.png'
PARAM_SAVED_MODEL = 'unet_' + PARAM_SYSTEM_TIME + '.hdf5'
PARAM_IMG_FOLDER = 'image'
PARAM_MSK_FOLDER = 'label'
PARAM_METRICS = 'loss'								# TODO: motitor more metrics... look up the options.
PARAM_DATA_ARGS = dict(rotation_range = 80,      	# TODO: improve the data augmentation
                width_shift_range =		0.02,
                height_shift_range =	0.02,
                shear_range	= 			0.35,
                zoom_range = 			0.075,
                horizontal_flip = 		True,
                fill_mode = 			'nearest',
                rescale =                   1./255)