## CLI cell classifier 

Can be used to determine the current embryonic stage the c.elegans worm in an image.

### Steps:

First make sure that you have the necessary libraries. If not, install the libraries with

* ``` pip install numpy```
* ``` pip install torch torchvision```
* ```pip install opencv-python```
* ```pip install argparse```


 1. Clone the repository <br>
 ``` git clone https://github.com/Mayukhdeb/adventures-with-augmentation.git```
2. Open the app's directory <br>
``` cd CLI-app```
3. Run the app on a sample image <br>
``` python3 cell_classifier_CLI.py sample.png```
4. The general command would be <br>
``` python3 cell_classifier_CLI.py <your_image_name>.png```



## What's under way ?
* The current CLI app works on a compact ensemble model which can only classify  between the embryonic stages of a certain cell, I plan to train more models which will be doing broader classification tasks.
* Add a feature where it can classify all the images in a certain directory and save the results in a CSV file.

