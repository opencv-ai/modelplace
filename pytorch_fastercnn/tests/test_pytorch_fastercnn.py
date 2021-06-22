import json
import os
import pytest

import pydantic
import torch
from modelplace_api import Device
from modelplace_api.utils import is_equal
from PIL import Image

from pytorch_fastercnn import InferenceModel

BACKEND = Device.gpu if torch.cuda.is_available() else Device.cpu


@pytest.fixture()
def prepare_data():
    data_dir = os.path.abspath(os.path.dirname(__file__))
    test_image_path = os.path.join(data_dir, "pytorch_fastercnn.jpg")
    test_result_path = os.path.join(data_dir, "pytorch_fastercnn_gt.json")
    test_image = Image.open(test_image_path).convert("RGB")
    with open(test_result_path, "r") as j_file:
        test_result = json.loads(j_file.read())
    return test_image, test_result


def test_process_sample(prepare_data):
    test_image, test_result = prepare_data

    model = InferenceModel()
    model.model_load(BACKEND)
    ret = model.process_sample(test_image)
    ret = [pydantic.json.pydantic_encoder(item) for item in ret]
    assert is_equal(ret, test_result)


def test_batch_inference(prepare_data):
    test_image, test_result = prepare_data
    batch_input = [test_image, test_image, test_image, test_image]
    expected_output = [test_result, test_result, test_result, test_result]

    model = InferenceModel()
    model.model_load(BACKEND)
    preprocessed_data = model.preprocess(batch_input)
    forwarded_data = model.forward(preprocessed_data)
    postprocessed_data = model.postprocess(forwarded_data)

    results = [[pydantic.json.pydantic_encoder(item) for item in image_result] 
               for image_result in postprocessed_data]
    assert is_equal(results, expected_output)


def test_process_empty_input():
    empty_input = Image.new("RGB", (1280, 720), (128, 128, 128))

    model = InferenceModel()
    model.model_load(BACKEND)
    ret = model.process_sample(empty_input)
    assert ret == []
