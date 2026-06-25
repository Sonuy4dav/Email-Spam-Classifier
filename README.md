# Email Spam Classifier

A Machine Learning-based web application that classifies messages as **Spam** or **Not Spam (Ham)** using NLP techniques and a trained classification model.

## Features

* Spam and Ham message detection
* Text preprocessing and cleaning
* TF-IDF vectorization
* Fast predictions
* Simple web interface built with Flask

## Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* NLTK
* HTML & CSS

## Project Structure

```text
Email-Spam-Classifier/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── static/
└── templates/
```

## Installation

```bash
git clone https://github.com/Sonuy4dav/Email-Spam-Classifier.git
cd Email-Spam-Classifier
pip install -r requirements.txt
python app.py
```

## Example

**Input:**

```text
Congratulations! You have won ₹10,000.
```

**Output:**

```text
Spam
```

## Future Improvements

* Deep Learning models
* Multi-language support
* Cloud deployment
* Real-time email filtering

## Author

**Sonu Yadav**
B.Tech Data Science Student

