# Streamlit App Setup Guide

Welcome to the Streamlit app! Follow these steps to set it up on your local machine.

## Prerequisites

1. **Python**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Git**: If you don't have Git installed, download it from [git-scm.com](https://git-scm.com/).

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-streamlit-app.git
    cd your-streamlit-app
    ```

2. **Create a virtual environment:**

    ```bash
    # Install virtualenv (if not already installed)
    pip install virtualenv
    
    # Create a virtual environment
    virtualenv venv
    
    # Activate the virtual environment
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the App

1. **Run Streamlit App:**

    ```bash
    streamlit run streamlit_app.py
    ```

    This command will start the Streamlit development server and open the app in your default web browser.

2. **Access the App:**

    Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to view your Streamlit app.

## Customization

Feel free to customize the app by modifying the code in `streamlit_app.py` and adjusting any configuration files or static assets as needed.

## Troubleshooting

- If you encounter any issues, refer to the error messages and check the [Streamlit documentation](https://docs.streamlit.io/) for help.

- Make sure your virtual environment is activated when running the app.

## Feedback

If you encounter any problems or have suggestions for improvement, please [open an issue](https://github.com/aashishpnt/finetuning-llm/issues).

