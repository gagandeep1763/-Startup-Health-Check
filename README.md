# Startup Health Check

This is a simple web application that predicts whether a startup will be acquired (success) or close down (failure) based on a few key metrics.

## 📸 Demo Screenshot

![Startup Health Check UI](https://github.com/gagandeep1763/Startup-Health-Check/blob/main/Image.png?raw=true)

## Project Overview

The application is built with Flask and uses a pre-trained machine learning model to make predictions. The model takes the following inputs:

## Objectives
Build a machine learning model to classify startup outcomes.

Develop a user-friendly web interface using Flask and HTML/CSS.

Provide insights for investors, entrepreneurs, and analysts.

Host the application online using Render for public use.


- **Name of Organization:** The name of the startup.
- **Total Funding (USD):** Higher funding often indicates investor confidence and more resources to grow.
- **Milestones:** More milestones show progress and achievements, suggesting a healthy trajectory.
- **Funding Rounds:** Multiple rounds suggest sustained investor interest and validation over time.
- **Relationships:** Strong networks (e.g., founders, advisors, investors) can boost growth and opportunity.
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

Developed By

Gagandeep D

Google Certified UI/UX Designer
