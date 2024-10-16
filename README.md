# 🌟 NLP Project Summary: Understanding Tweet Sentiment 🌟

🏆 This project totally crushed the competition when it came to classification accuracy, with F1_score of **86.47 %**! 

In this project, I sift through tweets and figure out if they’re spreading good vibes or bad - unlocking the conversation happening online and tapping into the emotions behind those bite-sized 280-character tweets! 💬✨


## 📝 Tweet Sentiment Classification

In this project, I use logistic regression to classify tweets based on their sentiment. It’s not just about crunching numbers; it’s about tapping into what people are feeling and sharing their thoughts with the world.

### 🚀 Preprocessing

Before we can analyze the tweets, we need to get them ready. Here’s how we do that:

1. **Importing Libraries**: First, we bring in the libraries that we’ll need for the analysis.

2. **Reading the Data**:
   - We pull in the tweet text from `train_text.txt`.
   - We match it with the sentiment labels from `train_labels.txt`.

3. **Cleaning Up**:
   - We remove @user mentions and other distractions, so we can focus on the content of the tweets.
   - We break down the tweets into individual words, or tokens, to make them easier to analyze.
   - We filter out common stop words that don’t add much meaning.
   - Lastly, we get rid of any empty tweets, ensuring that every piece of data we analyze is useful.

### 🔍 Feature Extraction

Now that our tweets are clean, it’s time to extract features that help us understand their sentiment better:

1. **Initial Features**:
   - **f10**: We calculate the log count of words in each tweet.
   - **f11**: We measure the log of the length of the longest word in each tweet.
   - **f12**: We count the number of words with five or more characters—because sometimes, the longer words hold deeper meaning.

2. **Creating Feature Sets**:
   - **f1**: Scores from an adjective word list to capture emotional tone.
   - **f2**: Scores from a general word list for a broader context.
   - **f3 to f9**: We create several additional feature sets from specific word lists that further enrich our analysis.

3. **Combining Features**:
   - All of these features come together in a single feature matrix we call **Xtrain**.

### 📈 Logistic Regression

With our features ready, it’s time to train our model. Here’s the step-by-step:

1. **Reshaping Labels**: We convert our sentiment labels into a format the model can work with, known as **Ytrain**.

2. **Training the Model**:
   - We use batch gradient descent to train our logistic regression model, improving it iteratively to get better predictions.
   - We update our model’s weights using the training data and a learning rate.

3. **Mapping and Optimizing**:
   - We use the sigmoid function to translate our features into probabilities between 0 and 1.
   - By minimizing the cost function, we optimize our model for more accurate predictions.

4. **Saving Our Progress**: 
   - Once we’ve trained the model, we save it along with the learned weights, so we can use them later.

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

This README gives you an overview of the code and its capabilities. For a deeper dive, check out the [Tweet_Classification.py](https://github.com/optimak/NLP-Project/blob/main/Tweet_Sentiment_Classification.ipynb) code, where you’ll find more details in the comments and variable names.
