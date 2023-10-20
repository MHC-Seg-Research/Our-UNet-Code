from datetime import datetime

PARAM_SYSTEM_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")
PARAM_PATH_CARTE = './data/endoscopic/cartesian'
PARAM_PATH_POLAR = './data/endoscopic/polar'
PARAM_PATH_SCORES = './prev-analysis'
PARAM_PATH_TEMP_POLAR = './temp/polar_Dom'
PARAM_PATH_TEMP_CARTE = './temp/cartesian_Dom'

PARAM_BETA1 = [0.2, 0.4, 0.6, 0.4, 0.2, 0.5, 0.5]
PARAM_BETA2 = [0.8, 0.4, 0.8, 0.999, 0.999, 0.5, 0.999]

PARAM_SUB_FOLDER_POLAR = 'polar'
PARAM_SUB_FOLDER_CARTE = 'cartesian'
PARAM_IMG_FOLDER = 'image'
PARAM_MSK_FOLDER = 'label'

PARAM_RESULTS = 'results'
PARAM_SPLIT_NUM = 5


TARGET_HEIGHT = 256
TARGET_WIDTH = 256
CHANNEL_NUM = 3
