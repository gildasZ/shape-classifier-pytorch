# Basic Shape Classifier

## Objective:
Develop a Jupyter Notebook that demonstrates the training, testing, and validation of a simple vision machine learning model to classify images into three categories: circles, squares, and triangles.

## Tools and Libraries Required:
* Python 3.x
* PyTorch
* torchvision
* matplotlib (for visualization)
* PIL (Python Imaging Library)
* Jupyter Notebook

## Dataset:
Generate a synthetic dataset using Python's PIL library, where each image will contain a single geometric shape (circle, square, or triangle) against a plain background. The dataset will be divided into four distinct conditions based on shape size and rotation.

Conditions for Dataset Splitting:

Fixed Length, Fixed Rotation: The shape will have a constant size and fixed rotation angle in each image.
Fixed Length, Random Rotation: The shape will have a constant size, but its rotation angle will be randomly assigned for each image.
Random Length, Fixed Rotation: The shape's size will vary randomly, but it will have a fixed rotation angle for all images.
Random Length, Random Rotation: Both the shape's size and its rotation angle will vary randomly for each image.

[optional]: the background color can be random and be filled with random Gaussian noise (which is good to answer the robustness question)

# Task Description:

## Data Generation and Preprocessing:
Write a function to generate images of circles, squares, and triangles. Each shape should be randomly placed within the image frame.

## Ensure a balanced dataset: generate an equal number of images for each shape.
Normalize the images and split the dataset into training, validation, and testing sets.
Create DataLoader for each dataset subset with a suitable batch size.

# Model Architecture:

## Design a useful vision model that:

You can design any machine learning-based vision model, such as a CNN-based model, Transfermer-based model, etc.

Kindly provide the reason why you want to choose this model.

## Training the Model:

Define the loss function (e.g., cross-entropy loss).
Select an optimizer (e.g., Adam or SGD).
Train the model for a suitable number of epochs (e.g., 10-20 epochs).
Choose the training strategy (e.g., early stopping, learning rate scheduling).
Implement checkpoints to save the model at regular intervals.
Include inline comments explaining the choice of hyperparameters.

Kindly explain the reasons behind choosing these training settings.

## Testing and Validation:

Evaluate the model on the test dataset.
Calculate and print the classification accuracy.
Display a confusion matrix.

## Visualization:

Plot training and validation loss over epochs.
Visualize some sample predictions with actual labels vs. predicted labels.

## Explanation:

Free to tell us, how can we learn from these dataset and examples.
How can we improve the accuracy of the model?

## Documentation and Code Quality:

Include detailed comments and explanations in the Jupyter Notebook, describing each step of the workflow.
Ensure the code is clean, modular, and well-organized.

## Deliverables:
A Jupyter Notebook containing the completed assignment.
A brief report summarizing the methodology, results, and any observations or conclusions.

## Evaluation Criteria:
Correct implementation of the model.
Accuracy of the model on the test dataset.
Quality and clarity of the code and comments.
Effective use of PyTorch and other libraries.
Insightful analysis and presentation of the results.

# How to Submit Your Assignment
To ensure a smooth submission process and proper evaluation of your work, please follow the steps outlined below:

## Create a Repository:

Set up a new GitHub repository for this assignment in your github personal account. Name the repository as `ShapeClassifierPyTorch`.
Initialize the repository with a README.md file that briefly describes the project and its structure. Include any necessary instructions for running the notebook and any dependencies that need to be installed.

## Commit Your Jupyter Notebook:

Develop your solution in a Jupyter Notebook named Shape_Classifier.ipynb.
Ensure that your notebook includes comprehensive comments and explanations as specified in the assignment.
Commit and push your completed notebook to the repository. Make sure that the notebook is well-documented and easy to understand.

## Include Additional Resources:

If your project uses any additional scripts or data files, make sure they are included in the repository and properly referenced in the notebook.
Ensure that all necessary files to run the notebook and replicate the results are available in the repository.

## Prepare for Submission:

Double-check your repository to ensure that it is public and accessible. This allows the evaluation team to review your work without any issues.
Review your email to ensure that it includes the repository link and any other required information as specified in the assignment guidelines.

## Submit Your Work:

Send an email to service@smartsurgerytek.com with the subject line "Mid-Level Machine Learning Engineer Technical Assignment Submission".

## In the body of the email, include:
Your full name and contact information.
A brief introduction or cover letter that provides context about your submission.
The link to your GitHub repository containing the completed assignment.

## Follow Up:

After submitting your assignment, you may follow up with an email if you have not received an acknowledgment within a reasonable time frame (e.g., one week).
Be prepared to discuss your project and answer any questions that may arise during the review process.
By following these steps, you can ensure that your submission is organized and professional, reflecting your abilities and attention to detail. Good luck with your assignment!

----

# Bonus 1. The Problem of Waiting for My Luggage (optional)

Today, you’re a traveler.
After a long journey, you finally get off the plane, and then you watch a pile of luggage spinning around.
But after a long wait, your luggage still hasn’t come.
How much longer do you have to wait?

We may create some assumptions to solve this problem.

1. The luggage must be on the airplane before it can be transferred to the baggage claim area. 

2. The conditional probability of receiving the luggage increases linearly over time. After 10 minutes, the probability becomes 1:

3. We have ignorance about whether the luggage is still in the airplane or not (time-independent).

$$
P(S=1)=0.5
$$

Kindly provide your thoughts and conducts on these questions.

A. After 5 minutes, what is the conditional probability that the luggage is still on the airplane? (It means I can't see the luggage in these five minutes.)

B. How does the conditional probability change over time? Use a plot to show the change in probability.


# Bonus 2. Simpson’s Paradox in Clinical Studies: When the Treatment Effect Reverses (optional)


|            | Control Group (No Medication) |               | Treatment Group (Medication) |               |
|------------|-----------------------------|---------------|-----------------------------|---------------|
|            | Disease = 0                 | Disease = 1   | Disease = 0                 | Disease = 1   |
| Male       | 19                           | 1             | 37                           | 3             |
| Female     | 28                           | 12            | 12                           | 8             |
| Total      | 47                           | 13            | 49                           | 11            |


Today, you are a doctor: you may face a problem that the treatment effect reverses.

The key observation is that, when controlling for gender, the drug has a negative effect on the disease, but when considering the total population without controlling for gender, the effect seems reversed. The doctor is confused by the existence of a drug that has harmful effects on both genders but is beneficial for everyone. 

How can we explain the result? Is that a paradox? 

This can be explained in several ways depending on the assumptions made about the relationships between the variables.

Kindly explain the result and provide the numerical results over these following different causal assumptions:

A. Take the gender as a confounding factor on both drug and disease: gender is considered a confounder, meaning it affects both the treatment (drug) and the outcome (disease). The drug has a direct effect on the disease.

B. Take the gender as a mediator (Suppose drug have super power change the gender): meaning that the drug has effects both on gender and disease, and gender then affects the disease only. 

C. Do A and B have different results? If yes, which should we trust and explain?
