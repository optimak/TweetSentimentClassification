import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression

# File paths
train_text_file = "train_text.txt"
train_labels_file = "train_labels.txt"
adj_word_list_file = "adj_2000.tsv"
general_word_list_file = "f_words_2000.tsv"

# Preprocessing
def preprocess_tweet(tweet):
    # Remove @user mentions and characters before that
    tweet = ' '.join(word for word in tweet.split() if not word.startswith('@'))
    
    # Tokenize tweet into individual words
    words = tweet.split()
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    return ' '.join(words)

# Load tweet text and labels
tweets = pd.read_csv(train_text_file, header=None, names=["tweet"])["tweet"].apply(preprocess_tweet)
labels = pd.read_csv(train_labels_file, header=None, names=["label"])["label"]

# Feature Extraction
def compute_initial_features(tweets):
    features = pd.DataFrame()
    
    # f10: Log count of words in each tweet
    features["f10"] = np.log(tweets.apply(lambda tweet: len(tweet.split())))
    
    # f11: Log of the length of the longest word in each tweet
    features["f11"] = np.log(tweets.apply(lambda tweet: max(len(word) for word in tweet.split())))
    
    # f12: Log count of words with 5 or more characters in each tweet
    features["f12"] = np.log(tweets.apply(lambda tweet: len([word for word in tweet.split() if len(word) >= 5])))
    
    return features

def load_word_list(file_path):
    return set(pd.read_csv(file_path, sep="\t", header=None, names=["word"])["word"])

def compute_word_list_features(tweets, word_list):
    features = pd.DataFrame()
    
    for feature_num in range(1, 10):
        feature_name = "f{}".format(feature_num)
        features[feature_name] = tweets.apply(lambda tweet: len(set(tweet.split()) & word_list))
    
    return features

# Load word lists
adj_word_list = load_word_list(adj_word_list_file)
general_word_list = load_word_list(general_word_list_file)

# Compute features
initial_features = compute_initial_features(tweets)
f1 = compute_word_list_features(tweets, adj_word_list)
f2 = compute_word_list_features(tweets, general_word_list)

# Combine feature sets
feature_matrix = pd.concat([initial_features, f1, f2], axis=1)

# Logistic Regression
model = LogisticRegression()

# Train the model
model.fit(feature_matrix, labels)

# Save the trained model
model_file = "trained_model.pkl"
joblib.dump(model, model_file)

print("Training completed. Model saved as '{}'.".format(model_file))
