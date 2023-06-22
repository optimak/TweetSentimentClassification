# NLP-Project Summary
Uses Tweet Data to classify as positive or negative

# Tweet Sentiment Classification

In this NLP project, I perform tweet sentiment classification using logistic regression. The code takes a dataset of tweets and their corresponding sentiment labels and performs various preprocessing steps, feature extraction, and training of a logistic regression model.

## Preprocessing

1. The code starts by importing the necessary libraries and setting up the file paths for the dataset.
2. The tweet text is read from the file `train_text.txt`, and the corresponding labels are read from `train_labels.txt`.
3. Preprocessing steps are applied to the tweet text:
   - Removing `@user` mentions and characters before that.
   - Tokenizing the tweets into individual words.
   - Removing stop words from the tweets.
4. Empty tweets and tweets with zero characters are removed from the dataset.

## Feature Extraction

1. Three initial features (f10, f11, f12) are computed:
   - f10: Log count of words in each tweet.
   - f11: Log of the length of the longest word in each tweet.
   - f12: Log count of words with 5 or more characters in each tweet.
2. Two feature sets (f1, f2) are created by matching words from the tweets with pre-defined word lists:
   - f1: Scores from an adjective word list (`adj_2000.tsv`).
   - f2: Scores from a general word list (`f_words_2000.tsv`).
3. Seven additional feature sets (f3-f9) are created by matching words from the tweets with pre-defined word lists specific to each feature set.
4. All the feature sets are combined into a single feature matrix (Xtrain).

## Logistic Regression

1. The labels (sentiment values) are reshaped into a row vector (Ytrain).
2. The logistic regression model is trained using batch gradient descent.
3. The weights (W) of the logistic regression model are updated iteratively using the training data and learning rate (l_rate) for a specified number of iterations (iters).
4. The sigmoid function is used to map the linear combination of features and weights to a probability score between 0 and 1.
5. The cost function (log loss) is minimized to optimize the model's predictions.
6. The trained logistic regression model is saved, along with the learned weights.

## Usage

To use this code for tweet sentiment classification:

1. Prepare the dataset:
   - Create `train_text.txt` file containing the tweet text.
   - Create `train_labels.txt` file containing the corresponding sentiment labels.
2. Modify the file paths in the code to match the locations of your dataset.
3. Run the code to perform preprocessing, feature extraction, and training.
4. The trained model and learned weights will be saved, which can be used for sentiment classification on new tweets.

Note: The code assumes the availability of pre-defined word lists for feature extraction. You may need to adjust the code or provide your own word lists depending on your specific requirements.

This README provides an overview of the code's functionality and usage. For more detailed and current information, refer to the `Tweet_Classification.py` code, comments and variable names.

Happy sentiment classification!
