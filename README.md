These are instructions on how to submit a model for listing on [Modelplace.AI](https://modelplace.ai/), the AI model marketplace.

Modelplace currently supports [PyTorch](https://pytorch.org/), [Tensorflow](https://www.tensorflow.org/), [OpenVINO](https://docs.openvinotoolkit.org/latest/index.html) and [ONNXRuntime](https://www.onnxruntime.ai/) backends.

# How Do I submit a model to Modelplace?

To provide a model we ask you to do the following:
1. Provide [required model publishing information](#model-publishing-information) about yourself and each model you want to publish
2. Set up [environment](#evironment-setup) and try our [example model (PyTorch Faster R-CNN)](pytorch_fastercnn)
3. Implement your model in a similar way to the given [example model (PyTorch Faster R-CNN)](pytorch_fastercnn)
4. Create a Python wheel [package](#package) with your model
5. [Send your model to us](#send-your-model-to-us) with the above information and package you have created

## Model publishing information
### Required
- **Model description** - The whole description of what the model does. Example: See the [example model page](https://modelplace.ai/models/2) - this is the text under the "Summary" heading.
- **Model description preview short** - The text people see on the "card" for each model on the [model list page](https://modelplace.ai/models). A short (one sentence) description of your model.
- **Model name (Full)** - Shown on the individual model page ([example model page](https://modelplace.ai/models/2)), e.g. `Faster region-based convolutional neural network with ResNet-50 FPN backbone` 
- **Model name (Short)** - A much shorter model name shown on the [model list page](https://modelplace.ai/models), e.g. `Faster R-CNN`
- **Dataset name** - Specify if your model uses public data e.g. MSCOCO or Open images, or a custom dataset
- **Preview image** - we will run a model on the image and will use its output for visualization. This image will be both on the [model list pages](https://modelplace.ai/models) and on the [model page](https://modelplace.ai/models/2)
- **License** - License type e.g. Apache 2.0, MIT, Proprietary, etc.
- **Number of classes** - For classifier models, how many distinct classes does it detect?
- **Author** - Your name or organization name (e.g. University)
- **Metrics** - The accuracy of your model

### Optional
- **Dataset link** - The link to a dataset that you use for training and testing of your model
- **Homepage link** - The link to your project page, source code or website for this model
- **System requirements** - What system setup (e.g. CPU, GPU, and RAM specifications) we should use to serve your model
- **Logo** - The logo will be added to model previews on listing pages and individual model pages  
_Note: This should be svg (png is possible) image with circle shape and size 128x128 pixels at least_
- **Avatar image** - Shown next to your name or organization name on the model listing and indivudal model pages (by default, shows OpenCV logo)  
_Note: This should be svg (png is possible) image with circle shape and size 128x128 pixels at least_
![](imgs/explanation.png)

## Environment Setup
- Install venv  
```python3.7 -m pip install virtualenv```
- Create an empty virtual environment for python3.7  
```python3.7 -m  virtualenv  venv```
- Activate it  
```source venv/bin/activate```
- Install pytest and wheel  
```python3.7 -m pip install pytest wheel```
- Install git and git-lfs  
```sudo apt install git git-lfs```
- Clone the repo   
```git clone https://github.com/opencv-ai/modelplace.git```

## Example Model
For package and style guidelines see the [example package (Faster R-CNN)](pytorch_fastercnn).
- Change directory to the package folder (`pytorch_fastercnn`)
```cd modelplace/pytorch_fastercnn```
- Install the package
```python3.7 setup.py bdist_wheel && rm -R build/ *.egg-info && pip3 install dist/*.whl```
- Run tests
```python3.7 -m pytest```

To see how this example model is represented on the site, view its page: [https://modelplace.ai/models/2](https://modelplace.ai/models/2)

## Packaging Models for Modelplace
Modelplace uses Python Wheels to simplify model serving. You should [create a wheel package](https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files) with our interfaces. See the [example (Faster R-CNN)](pytorch_fastercnn).

To create a package, follow these steps:
- Copy [the template folder](template)
- Extend model.py as shown in [the example](pytorch_fastercnn/pytorch_fastercnn/model.py)
- Update [the setup.py](template/setup.py)
- Copy your checkpoints to [the template/checkpoints](template/template/checkpoints) folder
- Rename "template" to your package name in all locations, including the folder name, e.g. template -> pytorch_fastercnn
- Install the package locally  
```python3.7 setup.py bdist_wheel && rm -R build/ *.egg-info && pip3 install dist/*.whl```
- Update tests in [test_model.py](template/tests/test_model.py)
- Run tests  
```python3.7 -m pytest```
- Make sure that the tests are working correctly and all tests pass

## Send Your Model To Us

Once you've done all that, to submit your package simply:

- Zip the folder you created in the above steps
- [Send us](mailto:modelplace@opencv.ai) this zip and information about package as described above

That's it! If anything is unclear, please [contact us](mailto:modelplace@opencv.ai) and we'll help you along.
