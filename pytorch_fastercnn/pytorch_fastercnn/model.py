import os

import torch
import torchvision
from modelplace_api import BaseModel, BBox, Device, TaskType
from torchvision.transforms import functional as F


class InferenceModel(BaseModel):
    class_names = {
        0: "background",
        1: "person",
        2: "bicycle",
        3: "car",
        4: "motorcycle",
        5: "airplane",
        6: "bus",
        7: "train",
        8: "truck",
        9: "boat",
        10: "traffic light",
        11: "fire hydrant",
        13: "stop sign",
        14: "parking meter",
        15: "bench",
        16: "bird",
        17: "cat",
        18: "dog",
        19: "horse",
        20: "sheep",
        21: "cow",
        22: "elephant",
        23: "bear",
        24: "zebra",
        25: "giraffe",
        27: "backpack",
        28: "umbrella",
        31: "handbag",
        32: "tie",
        33: "suitcase",
        34: "frisbee",
        35: "skis",
        36: "snowboard",
        37: "sports ball",
        38: "kite",
        39: "baseball bat",
        40: "baseball glove",
        41: "skateboard",
        42: "surfboard",
        43: "tennis racket",
        44: "bottle",
        46: "wine glass",
        47: "cup",
        48: "fork",
        49: "knife",
        50: "spoon",
        51: "bowl",
        52: "banana",
        53: "apple",
        54: "sandwich",
        55: "orange",
        56: "broccoli",
        57: "carrot",
        58: "hot dog",
        59: "pizza",
        60: "donut",
        61: "cake",
        62: "chair",
        63: "couch",
        64: "potted plant",
        65: "bed",
        67: "dining table",
        70: "toilet",
        72: "tv",
        73: "laptop",
        74: "mouse",
        75: "remote",
        76: "keyboard",
        77: "cell phone",
        78: "microwave",
        79: "oven",
        80: "toaster",
        81: "sink",
        82: "refrigerator",
        84: "book",
        85: "clock",
        86: "vase",
        87: "scissors",
        88: "teddy bear",
        89: "hair drier",
        90: "toothbrush",
    }

    def __init__(
        self,
        model_path: str = "",
        model_name: str = "",
        model_description: str = "",
        threshold: float = 0.1,
        **kwargs,
    ):
        model_path = (
            model_path
            if model_path != ""
            else os.path.join(os.path.abspath(os.path.dirname(__file__)), "checkpoints")
        )
        super().__init__(model_path, model_name, model_description, **kwargs)
        self.threshold = threshold

    @torch.no_grad()
    def preprocess(self, data):
        preproc_data = []
        for sample in data:
            sample = F.to_tensor(sample)
            sample = sample.to(device=self.device, non_blocking=True)
            preproc_data.append(sample)
        return preproc_data

    @torch.no_grad()
    def forward(self, data):
        result = self.model(data)
        return result

    @torch.no_grad()
    def postprocess(self, predictions):
        if not len(predictions):
            return [[]]
        predictions = [{k: v.to("cpu") for k, v in t.items()} for t in predictions]
        postprocessed_detections = []
        for prediction in predictions:
            image_predictions = []
            for box, score, label_id in zip(
                prediction["boxes"].tolist(),
                prediction["scores"].tolist(),
                prediction["labels"].tolist(),
            ):
                if score > self.threshold:
                    image_predictions.append(
                        BBox(
                            class_name=self.class_names[label_id],
                            x1=int(box[0]),
                            y1=int(box[1]),
                            x2=int(box[2]),
                            y2=int(box[3]),
                            score=score,
                        ),
                    )
            postprocessed_detections.append(image_predictions)

        return postprocessed_detections

    def model_load(self, device):
        self.task_type = TaskType.detection
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            num_classes=91, pretrained=False, pretrained_backbone=False,
        )

        self.model.load_state_dict(
            torch.load(
                os.path.join(
                    self.model_path, "fasterrcnn_resnet50_fpn_coco-258fb6c6.pth",
                ),
                map_location="cpu",
            ),
        )
        self.model.eval()
        if device == Device.cpu:
            self.device = "cpu"
        elif device == Device.gpu:
            self.device = "cuda"
        self.model = self.model.to(self.device)

    @torch.no_grad()
    def process_sample(self, image):
        data = self.preprocess([image])
        output = self.forward(data)
        results = self.postprocess(output)
        return results[0]
