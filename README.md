# Job Description Matcher

A Python-based application that analyzes the similarity between a CV and a job description and identifies matched and missing skills.

## Features

* CV and job description similarity scoring
* TF-IDF based text analysis
* Cosine similarity calculation
* Matched skills identification
* Missing skills identification
* Simple and modular Python structure

## How It Works

The application processes the CV and job description using **TF-IDF vectorization** and calculates their similarity using **cosine similarity**.

In addition to the similarity score, the system analyzes predefined technical skills to identify:

* **Matched Skills:** Skills found in both the CV and job description
* **Missing Skills:** Skills required by the job description but not found in the CV

### Example

**CV:**

```text
Python FastAPI PostgreSQL Docker Git
```

**Job Description:**

```text
Python FastAPI Docker AWS Git
```

**Result:**

```text
Similarity Score: ...
Matched Skills: Python, FastAPI, Docker, Git
Missing Skills: AWS
```

## Project Structure

```text
job-description-matcher/
│
├── app/
│   ├── main.py
│   ├── matcher.py
│   ├── skills.py
│   ├── test_matcher.py
│   └── __init__.py
│
├── data/
│   ├── cv.txt
│   └── job_description.txt
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies

* Python
* Scikit-learn
* TF-IDF
* Cosine Similarity

## Installation

Clone the repository:

```bash
git clone https://github.com/silafidan/job-description-matcher.git
cd job-description-matcher
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/main.py
```

## Project Status

🚧 **In Development**

The current version uses TF-IDF and cosine similarity for text-based matching.

Planned improvements include:

* Semantic similarity using embeddings
* More advanced skill extraction
* Improved job requirement analysis
* Web-based interface
* Better scoring and ranking of job matches

## Purpose

This project was developed as a practical exercise in **Natural Language Processing (NLP), text similarity, and Python application development**, with the goal of building a simple tool for evaluating CV–job compatibility.
