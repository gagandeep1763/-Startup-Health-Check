# Startup Health Check

This is a simple web application that predicts whether a startup will be acquired (success) or close down (failure) based on a few key metrics.

## Project Overview

The application is built with Flask and uses a pre-trained machine learning model to make predictions. The model takes the following inputs:

## Objectives
Build a machine learning model to classify startup outcomes.

Develop a user-friendly web interface using Flask and HTML/CSS.

Provide insights for investors, entrepreneurs, and analysts.

Host the application online using Render for public use.


- **Name of Organization:** The name of the startup.
- **Total Funding (USD):** The total amount of funding the startup has received.
- **Milestones:** The number of milestones the startup has achieved.
- **Funding Rounds:** The number of funding rounds the startup has gone through.
- **Relationships:** The number of relationships the startup has.

The model then predicts the outcome for the startup.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/startup-prediction.git
   cd startup-prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the Flask development server, run the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Model

The prediction model is a pre-trained Random Forest classifier saved in `model.pkl`. The features used by the model are stored in `features.pkl`.

### Model Performance

- **Accuracy:** 0.77
- **Classification Report:**
  ```
                 precision    recall  f1-score   support

             0       0.68      0.63      0.66        65
             1       0.81      0.84      0.82       120

      accuracy                           0.77       185
     macro avg       0.75      0.74      0.74       185
  weighted avg       0.76      0.77      0.77       185
  ```
