from sentence_transformers import SentenceTransformer, util
import torch
import joblib

# Load model components once
import os
current_dir = os.path.dirname(__file__)
bundle = joblib.load(os.path.join(current_dir, "..", "semantic_specialist_model.pkl"))

model = SentenceTransformer(bundle["model_name"])
known_embeddings = bundle["known_embeddings"]
symptom_specialist_pairs = bundle["symptom_specialist_pairs"]

def predict_specialist(symptom_text: str):
    input_embedding = model.encode(symptom_text, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(input_embedding, known_embeddings)[0]
    top_idx = similarities.argmax().item()
    specialist = symptom_specialist_pairs[top_idx][1]
    score = similarities[top_idx].item()
    return specialist, score
