# Adventures with augmentation :mag:

Exploring and experimenting with microscope imagery datasets. :microscope:

[![Binder](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/Mayukhdeb/adventures-with-augmentation/tree/master/)

## Simulating fluidity of cells with random distortions 

<img src="sample_images/blood.gif" width="40%" class = "center">.

## 

## [Parallel CNNs are just as good as they look](https://github.com/Mayukhdeb/adventures-with-augmentation/blob/master/parallel_CNNs.ipynb)


<img src="parallel_cnn.jpg" width="120%" class = "center">.

### But why use them anyways ?
* Because when two different architectures are trained on the same training set, they don't have the same weaknesses (i.e different confusion matrices) 
* This means that when both are combined, they tend to neutralise each other's weaknesses, which gives us a boost in accuracy.

## [Transfer learning with image resizing](https://github.com/Mayukhdeb/adventures-with-augmentation/blob/master/c_elegans_lifecycle.ipynb)

<img src="sample_images/transfer_learning.png" width="60%" class = "center">



* It aims to achieve the benefits of transfer learning on a large architecture on a smaller one
* It works by first training the model on smaller images, and then gradually increasing the size.
* Takes a lot less time than conventional training approaches, in this case it achieved 12% more accuracy (98% instead of 86%) in one fifth of the time.

<img src="sample_images/training_curve.png" width="100%" class = "center">

## [Class activation heatmaps on deep neural networks](https://github.com/Mayukhdeb/adventures-with-augmentation/blob/master/visualise_cnn_layers.ipynb)



<img src="sample_images/original_comma.png" width="40%"> <img src="sample_images/heatmap.png" width="50%">.

* Shows the regions of the image which gave the most activations for a certain label in a trained classification model
* In simpler words, it tells us about the regions of the image which made the model decide that it belongs to a certain label "x"

## Determining location of cells from images 
<img src="sample_images/cell_detect_pipeline.png" width="100%" class = "center">

#### And when the heatmap is superimposed upon the real image, it gives us an insight on how the CNN "looked" at the image
<img src="sample_images/superimposed.png" width="60%" class = "center">

## What's under way :chart_with_upwards_trend:
1. Trying to find out which augmentation technique works best for the cell images 
2. Experiment with the augmentation techniques and reach a high accuracy on the test set
3. Implement transfer learning with image resizing to reach high accuracies in less that half the time it's supposed to take
4. Trying to implement parallel CNNs for better accuracies on smaller architectures
5. Plotting and comparing confusion matrices of different architectures 



