import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np
import time

MODEL_PATH = "models/summarizer.onnx"

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def generate_summary(text):

    session = ort.InferenceSession(MODEL_PATH)

    start = time.time()

    inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        max_length=512
    )

    ort_inputs = {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"]
    }

    outputs = session.run(None, ort_inputs)

    summary_ids = np.argmax(outputs[0], axis=-1)

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    latency = (time.time() - start) * 1000

    return summary, latency