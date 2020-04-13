from __future__ import absolute_import, division, print_function, unicode_literals
import argparse

import tensorflow as tf
from tensorrtserver.api import ProtocolType, InferContext
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action="store_true", required=False, default=False,
                        help='Enable verbose output')
    parser.add_argument('-u', '--url', type=str, required=False, default='localhost:8000',
                        help='Inference server URL. Default is localhost:8000.')
    parser.add_argument('-i', '--protocol', type=str, required=False, default='http',
                        help='Protocol ("http"/"grpc") used to ' +
                             'communicate with inference service. Default is "http".')

    FLAGS = parser.parse_args()
    protocol = ProtocolType.from_str(FLAGS.protocol)

    model_name = "mnist"
    model_version = -1
    batch_size = 1

    # Create the inference context for the model.
    ctx = InferContext(FLAGS.url, protocol, model_name, model_version, FLAGS.verbose)

    x_test = np.float32(x_test)
    result = ctx.run({'flatten_input': [x_test[0]]},
                     {'dense_1': InferContext.ResultFormat.RAW},
                     batch_size)

    print(result['dense_1'])
