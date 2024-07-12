# Big Cat Classifier

### Objective:
To develop an image classifier app that can accurately classify images of big cats into eight distinct classes: lions, tigers, puma, jaguar, leopards, cheetah, puma, and black panther.

### Background:
The project was initiated to create a tool that leverages computer vision to identify different species of big cats. The eight classes were selected based on the idea that different big cat species can look like another species at certain levels. For example, it is difficult for humans to distinguish between jaguars and leopards as their patterns can be very similar. Any black toned big cat can be classifies as black panther but there exist black cats too which can be misclassified. Lionesses look different then lions but a bit similar to pumas. Cubs of all these species look similar to each other and even similar to cats. So this was a good learning challenge to create a tool which can identify different species accurately. This tool can be utilized for educational purposes, wildlife monitoring, and creating engaging learning experiences for children.

### Technologies Used:
+ **Languages:** Python
+ **Frameworks and Libraries:** TensorFlow, Keras, Flask, OpenCV
+ **CNN Architectures:** MobileNet, VGG19, Xception

### Process:
+ Data Collection: Conducted web scraping to gather a dataset of over 1000 images of big cats.
+ Image Preprocessing: Applied techniques such as resizing, normalization, and augmentation to prepare the images for model training.
+ Model Selection: Experimented with various convolutional neural network architectures (MobileNet, VGG19, Xception) to determine the best performing model. Selected Xception based on its superior performance.
+ Model Training: Trained and fine-tuned the Xception model on the preprocessed dataset, achieving an accuracy of 87% on the validation set.
+ Error Analysis and Data Augmentation: Used domain knowledge to identify types of images the model was prone to misclassify. Augmented the dataset with more images of these types, improving the model's accuracy to 93%.
+ App Development: Developed a Flask web application that allows users to upload images from the web or local devices and receive predictions on the big cat species.

### Challenges:
+ Ensuring a diverse and representative dataset through web scraping as not a huge data was available.
+ Balancing the model's accuracy and computational efficiency.
+ Handling misclassifications by augmenting the dataset effectively.
+ Identifying the images on which model was prone to misclassify and then make the model performance better on those.

### Outcome:
Successfully developed an image classifier model with an accuracy of 93% on the validation set. Created a functional Flask web app that allows users to upload images and see predictions in real-time.

### Future Plans:
Plan to deploy the model online and scale the application to include more animal species, transforming it into a fun and educational learning app for kids.

### Learnings:
+ Enhanced skills in web scraping and data augmentation.
+ Gained experience in comparing and selecting deep learning models.
+ Improved understanding of developing a Flask application with deep learning model.
+ Improving the performance of model on data which it is prone to misclassify.
+ GAined idea about how to use domain knowledge for improving the model performance.

