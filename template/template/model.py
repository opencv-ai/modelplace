from typing import Any, List

from modelplace_api import BaseModel
from modelplace_api.objects import Device


class InferenceModel(BaseModel):
    def model_load(self, device: Device) -> None:
        """
        This function realise model initialization(e.g. weights).
        Here you have to create and load your neural network and assign it to
        the self.model variable.

        :param device: CPU or GPU (modelplace_api.Device)
        """
        raise NotImplementedError

    def preprocess(self, images: List) -> List:
        """
        This function preprocesses data for inference.
        Should support batch format

        :param images: List of RGB Pillow images
        :return: list of preprocessed images(tensors)
        """
        raise NotImplementedError

    def forward(self, data: List) -> List:
        """
        This function passes preprocessed data through a neural network.
        Should support batch format

        :param data: List of preprocessed images
        :return: List of inference results
        """
        raise NotImplementedError

    def postprocess(self, predictions: List) -> List:
        """
        This function postprocesses results.
        Should support batch format

        Returned detections and targets should correspond to API
        that defined in modelplace_api.objects

        :param predictions: List of inference results
        :return: list of postprocessed result
        """
        raise NotImplementedError

    def process_sample(self, image: Any) -> Any:
        """
        This function process one image through a neural network.
        Returned prediction should correspond to API that defined in modelplace_api

        :param image: RGB Pillow image
        :return: prediction
        """
        raise NotImplementedError
