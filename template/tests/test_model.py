import pydantic
from modelplace_api import Device
from modelplace_api.utils import is_equal
from template.model import InferenceModel

test_result = None
test_image = None


def test_process_sample():
    model = InferenceModel()
    model.model_load(Device.cpu)
    ret = model.process_sample(test_image)
    ret = [pydantic.json.pydantic_encoder(item) for item in ret]
    assert is_equal(ret, test_result)
