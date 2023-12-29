import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
import numpy as np

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the fine-tuned model
model_path = "model/bert-finetuned-sem_eval-english-final"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.to(device)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", problem_type='multi_label_classification')

# Load the dataset
dataset = load_dataset("sem_eval_2018_task_1", "subtask5.english")

# Define label mapping
labels = [label for label in dataset['train'].features.keys() if label not in ['ID', 'Tweet']]
id2label = {idx: label for idx, label in enumerate(labels)}
label2id = {label: idx for idx, label in enumerate(labels)}

# Function to get predictions
def get_predictions(text, threshold=0.5):
    encoding = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    encoding = {k: v.to(device) for k, v in encoding.items()}

    # Forward pass
    with torch.no_grad():
        outputs = model(**encoding)

    # Apply sigmoid to get probabilities
    probs = torch.sigmoid(outputs.logits.squeeze()).cpu().numpy()

    # Convert probabilities to binary predictions using the threshold
    predictions = (probs >= threshold).astype(int)

    # Map predicted labels to class names
    predicted_labels = [id2label[idx] for idx, label in enumerate(predictions) if label == 1]

    return predicted_labels

# Streamlit app
def main():
    st.title("BERT Multi-Label Text Classification")

    # Input text box
    text = st.text_area("Enter your text:", "")

    if st.button("Predict"):
        if text:
            # Get predictions
            predictions = get_predictions(text)

            # Display predictions
            st.subheader("Predicted Labels:")
            if predictions:
                st.success(", ".join(predictions))
            else:
                st.info("No labels predicted.")

if __name__ == "__main__":
    main()
