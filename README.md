# Computer-Vision-OpenCv-SSD

To write this code, used a pre-trained deep learning model called Single Shot MultiBox Detector (SSD) to detect objects such as cars, pedestrians, and bicycles in real time. Also, it provides a basic implementation of real-time object detection. You can further customize it by adjusting parameters, using different models, or integrating it into a larger application for car-based object detection.

Explanation of the code:

- Loading the Pre-trained Model: We load a pre-trained SSD model trained on the COCO dataset for object detection. The model consists of two files; the model file containing the trained weights and the configuration file containing the network architecture.

  ![pre_trained_model](https://github.com/ProfUgur/Computer-Vision-OpenCv-SSD/assets/148859613/ae90b296-a3e2-4c6a-bc92-3533811d9d35)

- Setting Input Parameters: We set the input size, scale, mean, and swapRB parameters for the model. These parameters are necessary for preprocessing the input image.

  ![input_and_scale](https://github.com/ProfUgur/Computer-Vision-OpenCv-SSD/assets/148859613/8fbf53ed-c021-4083-a090-6d7cf8dfdd86)

- Opening Video Capture: We open a video capture object using OpenCV. You can use either a webcam or provide a file path to a video file.

  ![video_capture](https://github.com/ProfUgur/Computer-Vision-OpenCv-SSD/assets/148859613/fd42c814-1060-4b3b-bc50-861c20175ce7)

- Object Detection Loop: We continuously read frames from the video capture and perform object detection on each frame using the SSD model. Detected objects are annotated with bounding boxes and labels.

 ![loop](https://github.com/ProfUgur/Computer-Vision-OpenCv-SSD/assets/148859613/fda4c618-aa3d-4e15-b0ec-715322a8c329)

- Displaying the Frame: We display the annotated frame in a window named "Object Detection". 'Q' button is used to exit the loop and close the window.

 ![break_loop](https://github.com/ProfUgur/Computer-Vision-OpenCv-SSD/assets/148859613/c33bdc73-1eea-4e98-9f42-0d851f945ec1)

Here are a few sites I use during training where you can find information about OpenCV and SSD. These resources should provide you with ample information and guidance to get started with OpenCV and SSD-based object detection. Whether you're a beginner or an experienced developer, these sites offer valuable insights and practical examples to help you learn and implement computer vision applications.

OpenCV modules
Website: https://docs.opencv.org/4.x/index.html
The official documentation for OpenCV provides comprehensive guides, tutorials, and references for using the library for various computer vision tasks, including object detection.

PyImageSearch
Website: https://pyimagesearch.com/
PyImageSearch offers tutorials, articles, and guides on computer vision and deep learning topics using Python and OpenCV. It covers a wide range of topics, including object detection, and provides practical examples and code snippets.

TensorFlow Model Zoo
Website: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md
TensorFlow Model Zoo provides pre-trained models for various computer vision tasks, including object detection. You can find pre-trained SSD models along with their configurations and weights for use with frameworks like OpenCV.

SSD: Single Shot MultiBox Detector
Website: https://arxiv.org/abs/1512.02325
The original research paper on SSD published by the authors provides an in-depth explanation of the SSD algorithm, its architecture, and how it achieves real-time object detection.

MathWorks
Website: https://www.mathworks.com/help/deeplearning/ug/object-detection-using-ssd-deep-learning.html
This site shows how to train a Single Shot Detector (SSD). Also, you can get information about AI, Data Science, Statistics or Deep Learning in this site.
