<div align="center">
  
  # 🌌 NVIDIA Ising: The Quantum-AI Control Plane
  
  [![Audience](https://img.shields.io/badge/Target_Audience-Researchers_&_Academics-blue?style=for-the-badge)](#)
  [![Cost](https://img.shields.io/badge/Cost-100%25_Open_Source-brightgreen?style=for-the-badge)](#)
  [![Tech](https://img.shields.io/badge/Technology-Quantum_&_AI-purple?style=for-the-badge)](#)

  *Accelerating the path to useful, fault-tolerant quantum computers.*
</div>

---

## 🧭 Context & Overview

**NVIDIA Ising** is the world's first family of open AI models specifically designed to accelerate the development of useful, fault-tolerant quantum computers. Rather than building quantum hardware itself, NVIDIA has created the AI infrastructure needed to operate quantum processors at scale.

Historically, quantum computing has faced massive bottlenecks in two areas: **quantum error correction (QEC)** and **processor calibration**. NVIDIA released the Ising model family, training frameworks, and cookbooks to solve these exact problems using AI.

> **The Open-Source Advantage:** By open-sourcing these tools, NVIDIA is democratizing access to quantum-AI workflows, allowing universities, student researchers, and academics to push the boundaries of quantum physics without needing proprietary, closed-door enterprise software.

---

## 🎓 Why It Matters for Researchers & Universities

For academics and students, NVIDIA Ising is a career-accelerating toolkit. It bridges the gap between classical AI and quantum mechanics, making it an invaluable asset for modern research.

- **Career Advancement:** Mastering AI-driven quantum error correction makes you a highly sought-after candidate in both academia and the rapidly growing quantum tech industry.
- **Institutional Benefits:** Universities can integrate NVIDIA Ising into their physics and computer science curricula, providing students with hands-on experience using state-of-the-art, industry-standard tools.
- **Accelerated Publishing:** Instead of writing calibration algorithms from scratch, researchers can leverage pre-trained vision-language models (VLMs) to calibrate quantum processors, drastically reducing the time from hypothesis to publication.

---

## 💡 Ecosystem Summary & Resources

<details>
<summary><b>Click to expand the NVIDIA Ising Resource Table</b></summary>
<br>

| Resource / Model | Platform | Primary Use Case | Target Audience |
| :--- | :--- | :--- | :--- |
| **NVIDIA/ising** | GitHub | Central landing page, cookbooks, and documentation | All researchers and students |
| **NVIDIA/Ising-Decoding** | GitHub | Training framework for AI QEC decoders | Quantum algorithm developers |
| **Ising-Calibration-1-35B-A3B** | Hugging Face | Vision-language model for quantum processor calibration | Experimental physicists |
| **Ising-Decoder-SurfaceCode-1-Accurate** | Hugging Face | Pre-trained model for accurate surface code decoding | Fault-tolerance researchers |

</details>

---

## 🛠️ Real-World Tutorial: Getting Started with NVIDIA Ising

To use NVIDIA Ising in your research, you will interact primarily with their official GitHub repositories and Hugging Face model hubs. Here is a practical workflow to get you started.

### 1. Accessing the Core Frameworks

The central hub for all code and documentation is the main GitHub repository. You can clone the primary tools directly to your local machine or high-performance computing (HPC) cluster.

```bash
# Clone the central NVIDIA Ising repository
git clone https://github.com/NVIDIA/ising.git

# Clone the specific framework for AI Quantum Error Correction Decoders
git clone https://github.com/NVIDIA/Ising-Decoding.git
```
### 2. Loading Models from Hugging Face

NVIDIA hosts the pre-trained models on Hugging Face. For example, if you are working on quantum processor calibration, you can pull the `Ising-Calibration-1-35B-A3B` model, which is a vision-language model built specifically for quantum calibration tasks.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the NVIDIA Ising Calibration model
model_id = "nvidia/Ising-Calibration-1-35B-A3B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# Example: Processing a calibration readout (pseudo-code)
readout_data = "Analyze the following qubit state readout for phase errors..."
inputs = tokenizer(readout_data, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=100)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### 3. Running Quantum Error Correction

If your research focuses on fault tolerance, you can utilize the `Ising-Decoder-SurfaceCode-1-Accurate` model. This allows you to simulate surface code decoding, a critical step in maintaining stable quantum states over time.

---
---

## 📖 Full Tutorial

Ready to run NVIDIA Ising in your own environment? The complete hands-on tutorial covers:

- 🔑 Setting up your free NVIDIA NIM API key
- 🔬 Running quantum calibration via the VLM
- ⚛️ Surface code decoding on free Google Colab
- ☁️ One-click Colab launch badge

<div align="center">

[![Read the Full Tutorial](https://img.shields.io/badge/📖_Read_the_Full_Tutorial-TUTORIAL.md-blue?style=for-the-badge)](./TUTORIAL.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/tutorial.ipynb)

</div>
<div align="center">
  <i>This ecosystem provides a robust foundation for anyone looking to merge deep learning with quantum mechanics. By integrating these tools into your university lab or personal research, you are positioning yourself at the absolute cutting edge of the quantum computing revolution.</i>
</div>


