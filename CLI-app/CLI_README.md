## CLI cell classifier 

Can be used to determine the current embryonic stage the c.elegans worm in an image.

### Steps:
 1. clone the repository
 ``` git clone https://github.com/Mayukhdeb/adventures-with-augmentation.git```
2. open the app's directory 
``` cd CLI-app```
3. run the app on a sample image
``` python3 cell_classifier_CLI.py sample.png```
4. The general command would be 
``` python3 cell_classifier_CLI.py <your_image_name>.png```

## what's under way ?
* The current CLI app works on a compact ensemble model which can only classify  between the embryonic stages of a certain cell, I plan to train more models which will be made usable by the community in oderto classify cells
* Add a feature where it can classify all the images in a certain directory and save the results in a CSV file.

