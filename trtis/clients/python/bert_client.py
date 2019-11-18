from __future__ import absolute_import, division, print_function, unicode_literals

import argparse

import numpy as np
from tensorrtserver.api import ProtocolType, InferContext

import bert_embedding

FLAGS = None


def get_result(ctx, text):
    features = bert_embedding.get_embedding(text)
    result = ctx.run({'input_ids': [np.array(features.input_ids, dtype="int32")],
                      'input_mask': [np.array(features.input_mask, dtype="int32")],
                       'segment_ids': [np.array(features.segment_ids, dtype="int32")],
                      'label_ids': [np.array([features.label_id], dtype="int32")]},
                      {'probabilities': InferContext.ResultFormat.RAW}, 1)['probabilities']
    if result[0][0] >= result[0][1]:
        print("Not same, these sentences do not mean the same thing")
    else:
        print("Same, sentences essentially mean the same thing")
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action="store_true", required=False, default=False,
                        help='Enable verbose output')
    parser.add_argument('-u', '--url', type=str, required=False, default='localhost:8000',
                        help='Inference server URL. Default is localhost:8000.')
    parser.add_argument('-i', '--protocol', type=str, required=False, default='http',
                        help='Protocol ("http"/"grpc") used to ' +
                             'communicate with inference service. Default is "http".')
    parser.add_argument('-t', '--text', type=str, required=True)
    parser.add_argument('-f', '--file', action="store_true", required=False, default=False)

    FLAGS = parser.parse_args()
    protocol = ProtocolType.from_str(FLAGS.protocol)

    model_name = "bert"
    model_version = -1

    ctx = InferContext(FLAGS.url, protocol, model_name, model_version, FLAGS.verbose)
    if FLAGS.file:
        f = open(FLAGS.text, "r")
        for i in f.readlines():
            print(get_result(ctx, i))
            print(i)
        f.close()
    else:
        print(get_result(ctx, FLAGS.text))
