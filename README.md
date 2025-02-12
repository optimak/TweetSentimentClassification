# 🌟 NLP Project Summary: Understanding Tweet Sentiment 🌟

🏆 This project crushed the competition when it came to classification accuracy, with F1 score of **86.47 %**! 

In this project, I sift through tweets and figure out if they’re giving good or bad vibes! 💬✨


## 📝 Tweet Sentiment Classification

Logistic regression was utilized to classify tweets based on their sentiment.

### 🚀 Preprocessing

Before analyzing the tweets, they had to undergo some wrangling.  

1. **Importing Libraries**: First, the libraries needed for the analysis were brought in.

2. **Reading the Data**:
   - Tweets were pulled from `train_text.txt`.
   - The tweets were matched with their sentiment labels from `train_labels.txt`.

3. **Cleaning Up**:
   - @user mentions and other distractions were removed, to focus on the content of the tweets.
   - the tweets were broken down into individual words, or tokens, to make them easier to analyze.
   - common stop words were filtered out.
   - empty tweets were filtered out, ensuring that every piece of data analyzed is useful.

### 🔍 Feature Extraction

With the transformed data, features related to positive and negative sentiments can now be extracted:

1. **Initial Features**:
   - **f10**: calculates the log count of words in each tweet.
   - **f11**: measures the log of the length of the longest word in each tweet.
   - **f12**: counts the number of words with five or more characters—because sometimes, the longer words hold deeper meaning.

2. **Creating Feature Sets**:
   - **f1**: scores from an adjective word list to capture emotional tones.
   - **f2**: scores from a general word list for a broader context.
   - **f3 to f9**: create several additional feature sets from specific word lists that further enrich the analysis.

3. **Combining Features**:
   - All of these features come together in a single feature matrix named **Xtrain**.

### 📈 Logistic Regression

With the features ready, the model can be trained. Here’s the step-by-step:

1. **Reshaping Labels**: sentiment labels are converted into a format the model can work with, known as **Ytrain**.

2. **Training the Model**:
   - batch gradient descent is used to train the logistic regression model, improving it iteratively to get better predictions.
   - the model’s weights are updated using the training data and a learning rate.

3. **Mapping and Optimizing**:
   - the sigmoid function is used to translate features into probabilities between 0 and 1.
   - By minimizing the cost function, the model is optimized for more accurate predictions.

4. **Saving Our Progress**: 
   - Once trained, the model is saved, along with the learned weights, for future use.

### 📚 Usage

Want to try this out yourself? Here’s what you need to do:

1. **Prepare Your Dataset**:
   - Create a `train_text.txt` file with the tweet text.
   - Create a `train_labels.txt` file with the corresponding sentiment labels.

2. **Modify File Paths**:
   - Update the file paths in the code to match where your files are saved.

3. **Run the Code**:
   - Execute the code to carry out the preprocessing, feature extraction, and training.

4. **Start Classifying**:
   - With your trained model ready, you can classify new tweets and discover the sentiments behind them.

---

This README gives you an overview of the code and its capabilities. The original code can be found [here](https://drive.google.com/file/d/1en5J_872O4hb4iGydoHP7nb-lBXp_R2J/view?usp=sharing)
For a shortened version, check out the [Tweet_Classification.py](https://github.com/optimak/NLP-Project/blob/main/Tweet_Classification.py) code, where you’ll find more details in the comments and variable names.
