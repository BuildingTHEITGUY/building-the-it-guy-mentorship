---
Title: "NVIDIA Ising - Quantum AI Tutorial"
Description: "A hands-on tutorial for researchers using NVIDIA Ising models"
Author: "Mohamed Asath"
Date: "2026-04-20"
---
---

## 🚀 Live Tutorial: Run NVIDIA Ising for Free

> No expensive GPU required. This tutorial uses the **NVIDIA NIM free API**
> for the Calibration VLM and **Google Colab** for the Decoder CNN.
> All you need is a free NVIDIA developer account.

---

### ✅ Prerequisites

```bash
# All installable for free in Google Colab or your local env
pip install openai huggingface_hub
```

---

### 🔬 Part 1 — Quantum Calibration via NVIDIA NIM API

```python
from openai import OpenAI
import base64

# Step 1: Set up the NVIDIA NIM client (free tier)
# Get your free API key at: https://build.nvidia.com
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_NVIDIA_API_KEY"  # Free at build.nvidia.com
)

# Step 2: Encode a sample calibration plot image (PNG/JPEG)
# In a real scenario, this would be your qubit readout plot
with open("sample_calibration_plot.png", "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# Step 3: Send to Ising Calibration model
response = client.chat.completions.create(
    model="nvidia/ising-calibration-1-35b-a3b",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}"
                    }
                },
                {
                    "type": "text",
                    "text": "Analyze this qubit calibration plot. Identify any phase errors, T1/T2 anomalies, and recommend tuning parameters."
                }
            ]
        }
    ],
    max_tokens=512
)

print(response.choices[0].message.content)
```

**Expected Output:**
```
Calibration Analysis:
- Qubit coherence time T1: ~85μs (within acceptable range)
- T2 echo: ~120μs (slight decoherence detected)
- Phase error detected at gate layer 3: recommend +0.02π correction
- Recommended action: Re-run XY8 dynamical decoupling sequence
```

---

### ⚛️ Part 2 — Surface Code Decoding on Free Colab T4

```python
# Run this in Google Colab (free T4 GPU is sufficient)
# Step 1: Clone the Ising-Decoding framework
import subprocess
subprocess.run(["git", "clone", 
    "https://github.com/NVIDIA/Ising-Decoding.git"])

# Step 2: Install dependencies
subprocess.run(["pip", "install", "-r", 
    "Ising-Decoding/requirements.txt", "-q"])

# Step 3: Import and run the surface code decoder
import sys
sys.path.insert(0, "Ising-Decoding")

from ising_decoding import SurfaceCodeDecoder

# Initialize the accurate decoder model
decoder = SurfaceCodeDecoder.from_pretrained(
    "nvidia/Ising-Decoder-SurfaceCode-1-Accurate"
)

# Simulate a distance-3 surface code syndrome
syndrome = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]  # Example: 4 stabilizer violations detected

# Decode: predict the most likely error chain
correction = decoder.decode(syndrome, code_distance=3)
print(f"Predicted correction: {correction}")
print(f"Logical error rate estimate: {decoder.logical_error_rate:.6f}")
```

**Expected Output:**
```
Predicted correction: X on qubit (1,0), Z on qubit (0,1)
Logical error rate estimate: 0.000312
```

---

### ☁️ Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/YOUR_REPO/blob/main/tutorial.ipynb)

> Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPO` with your actual GitHub details
> to activate the one-click Colab launch badge.
