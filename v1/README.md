# Sample-GPT

**Sample-GPT** is a lightweight implementation of a GPT-like model designed for educational purposes and experimentation. This repository provides a simple yet functional implementation of a transformer-based language model, inspired by OpenAI's GPT architecture. It is ideal for learning how GPT models work or for prototyping small-scale language models.

---

## Features

- **Transformer-based architecture**: Implements the core components of GPT, including multi-head attention and feed-forward layers.
- **Lightweight and easy to use**: Designed for simplicity and readability, making it a great starting point for beginners.
- **Customizable**: Easily modify model parameters, such as the number of layers, heads, and embedding size.
- **Training and inference scripts**: Includes scripts to train the model on custom datasets and generate text.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dash7ou/Sample-GPT.git
   cd Sample-GPT
   ```
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Training the Model

The model is trained on the **OpenWebText** dataset, a replication of OpenAI's WebText dataset, available on Hugging Face: [Skylion007/openwebtext](https://huggingface.co/datasets/Skylion007/openwebtext). To train the model, run:

```bash
python train.py
```

### Generating Text

After training, you can generate text using the trained model with the `generate.py` script:

```bash
python chatbot.py -batch_size 64
```

---

## Dataset

The model is trained on the **OpenWebText** dataset, which is a large-scale collection of web pages designed to replicate the dataset used to train OpenAI's GPT-2. The dataset is hosted on Hugging Face and can be accessed here: [Skylion007/openwebtext](https://huggingface.co/datasets/Skylion007/openwebtext).

---

## Contributing

Contributions are welcome! If you'd like to improve the code, fix bugs, or add new features, please open an issue or submit a pull request.

---


## Acknowledgments

- Inspired by OpenAI's GPT architecture.
- Built using PyTorch.
- Uses the **OpenWebText** dataset from Hugging Face: [Skylion007/openwebtext](https://huggingface.co/datasets/Skylion007/openwebtext).

---

## Contact

For questions or feedback, feel free to reach out:

- **Author**: Mohammed Zourob
- **GitHub**: [dash7ou](https://github.com/dash7ou)
