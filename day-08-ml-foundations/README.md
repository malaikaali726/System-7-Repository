Core Concepts in AI and Machine Learning

1. Artificial Intelligence (AI) is a branch of computer science that builds machines and software capable of tasks that normally require human intelligence, such as learning, reasoning, problem-solving, and understanding language.

Examples: ChatGPT answering questions, virtual assistants responding to voice commands, self-driving cars recognizing roads and pedestrians, and recommendation systems suggesting movies or products.

In simple words: AI lets machines perform tasks that usually need human intelligence.

2. Machine Learning (ML) is a branch of AI in which computers learn patterns from data and use them to make predictions or decisions, without being explicitly programmed for every situation.

Examples: Predicting house prices, detecting spam emails, forecasting customer behavior, and recommending products.

In simple words: ML lets computers learn from data and make predictions or decisions.

3. Deep Learning (DL) is a subfield of ML that uses artificial neural networks with many layers to learn complex patterns from large amounts of data. It is widely used for image recognition, speech recognition, and natural language processing.

Examples: Facial recognition, speech recognition, image classification, and large language models (LLMs).

In simple words: Deep Learning uses multi-layered neural networks to learn complex patterns.

	AI	ML	Deep Learning
Definition	Enables machines to perform intelligent tasks	Enables machines to learn from data	Uses multi-layered neural networks to learn complex patterns
Scope	Broadest field	A subfield of AI	A subfield of ML
Examples	AI assistants, rule-based systems	House price prediction, spam detection	Image recognition, speech recognition, LLMs

Relationship: AI → Machine Learning → Deep Learning. Deep Learning is a subset of ML, and ML is a subset of AI.

Types of Learning

4. Supervised Learning is a type of ML in which the model learns from labeled data, meaning each input comes with its correct answer. The model finds patterns in the training data and applies them to new data.

Examples: Predicting house prices, classifying emails as spam or not spam, predicting students’ exam scores, and detecting objects in images.

There are two main types:

Regression predicts continuous numerical values, such as house prices, temperature, or salaries.
Classification predicts categories, such as spam or not spam, whether a customer will leave or stay, or whether an image shows a cat or a dog.

In simple words: Supervised learning learns from data that already includes the correct answers.

5. Unsupervised Learning is a type of ML in which the model finds patterns and relationships in unlabeled data. There are no predefined correct answers, so the model discovers groups or structure on its own.

Examples: Grouping customers by purchasing behavior, grouping similar documents, and identifying unusual data points.

Common techniques:

Clustering groups similar data points together, such as customers with similar spending habits.
Dimensionality reduction reduces the number of features while keeping as much useful information as possible, such as reducing hundreds of features to a few for visualization.

In simple words: Unsupervised learning discovers hidden patterns or groups in data without labels.

6. Reinforcement Learning (RL) is a type of ML in which an agent learns to make decisions by interacting with an environment and receiving rewards or penalties. The goal is a strategy that maximizes total reward over time.

Main components:

Agent: the learner or decision-maker
Environment: the world the agent operates in
Action: a move the agent makes
Reward: feedback on how good an action was
State: the current situation of the environment
Policy: the strategy the agent uses to choose actions

Examples: Training an agent to play a video game, teaching a robot to navigate, and training systems to make decisions through repeated interaction.

In simple words: Reinforcement learning lets an agent learn through actions and feedback.

	Supervised	Unsupervised	Reinforcement
Data	Labeled data	Unlabeled data	Experience from interactions
Goal	Predict outputs	Discover patterns	Maximize rewards
Feedback	Correct answers	No predefined labels	Rewards or penalties
Common tasks	Regression and classification	Clustering and dimensionality reduction	Sequential decision-making
Example	House price prediction	Customer segmentation	Training a game-playing agent
Dataset Terminology

7. Dataset: A dataset is a collection of related data organized for analysis or model training. It can contain numbers, text, images, audio, or other information, and is commonly stored as CSV, Excel, JSON, or database tables.

Consider this house price dataset:

Size (sq ft)	Bedrooms	Age (years)	Price
1000	2	10	5,000,000
1500	3	5	7,000,000
2000	4	2	9,000,000
1200	2	8	5,500,000
Data: individual values, such as 1500, 3, or 7,000,000.
Dataset: the complete table.
Row: one record or observation, such as the first house’s details.
Column: one attribute or variable, such as Bedrooms.
Feature: an input variable the model uses to predict, such as size or age.
Target variable: the value a supervised model is trained to predict, here Price.
Label: the correct answer for an example in labeled data. In classification, labels are categories like “Spam.” In regression, the target is a number.
Observation: one complete example or record.

Data types describe what a column holds, such as integers (25), floats (25.5), strings (“Pakistan”), booleans (True or False), and dates (2026-10-26).

Categorical data represents groups, such as city (Multan, Lahore, Karachi), color, or house type. It often must be converted to numbers before a model can use it.

Numerical data represents measurable quantities and is either:

Discrete: countable, such as the number of bedrooms.
Continuous: measurable, such as house size or temperature.

Training, validation, and test datasets:

Training dataset: used to teach the model.
Validation dataset: used to evaluate performance during development, compare models, and tune hyperparameters.
Test dataset: used to evaluate the final model on data it has never seen.

For example, 1000 house records might be split 70% training (700), 15% validation (150), and 15% testing (150). The right split depends on the dataset and problem.

Preparing Data

8. Missing Values occur when some entries have no recorded value, often shown as NaN. They can be handled by:

Removing affected rows or columns when appropriate
Filling numerical values with the mean or median
Filling categorical values with the mode
Using other imputation techniques

9. Outliers are observations that differ substantially from the general pattern, such as one house priced at 100,000,000 among prices near 5,000,000. An outlier is not always an error, so it should be investigated before you decide whether to keep or remove it.

10. Data Preprocessing is the preparation of raw data before training a model. Common steps include:

Handling missing values
Removing duplicate records when appropriate
Investigating outliers
Encoding categorical variables
Scaling numerical features when needed
Splitting data into training, validation, and test sets

11. Data Leakage occurs when information that would not be available at prediction time influences training or evaluation. This can make a model look more accurate than it will be in real use. For example, if a feature contains information derived from the actual future house price, the model effectively receives the answer.

To prevent leakage, split the data first and fit preprocessing steps, such as scaling, using only the training data
