# #
# import cv2
# import tensorflow as tf

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from lib.roi_data_layer.layer import RoIDataLayer
# from lib.utils.timer import Timer
# from lib.model.config import cfg
# import lib.roi_data_layer.roidb as rdl_roidb

#
#
#
# try:
#   import cPickle as pickle
# except ImportError:
#   import pickle
# import numpy as np
# import os
# import sys
# import glob
# import time
#
# import tensorflow as tf
# from tensorflow.python import pywrap_tensorflow

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import numpy as np
import numpy.random as npr
import cv2
# from cv2 import *
from lib.model.config import cfg
from lib.utils.blob import prep_im_for_blob, im_list_to_blob