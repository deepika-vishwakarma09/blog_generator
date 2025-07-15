
# LLaMA 2 Blog Generator with Streamlit

This project is a simple and interactive **blog generation app** powered by **Meta's LLaMA 2 7B** model. It uses `Streamlit` for the frontend and `LangChain` with `CTransformers` to run the model locally.

    
## Features

- ✅ Generate blog content from any topic
- ✍️ Choose target audience (Researchers, Data Scientists, Common People)
- 🔢 Specify the desired word count
- 🖥️ Runs fully offline using local `.bin` model
- 🧩 Built using: `LangChain`, `CTransformers`, `Streamlit`

## Project Structure

- BLOG_GENERATOR/
- ── blgenv/ # Python virtual environment  
- ── model/ # Folder for storing LLaMA model
-  └── llama-2-7b-chat.ggmlv3.q4_0.bin
- ── app.py # Streamlit application code
- ─ requirements.txt # Python dependencies



## 🛠️ Installation

## 1. Clone the repository
- git clone <(https://github.com/deepika-vishwakarma09/blog_generator.git)>
- cd <BLOG_GENERATOR>
## 2. Create and activate virtual environment (recommended)
   - python -m venv blogenv
- blogenv\Scripts\activate  # For Windows

## 3. Install requirements
- pip install -r requirements.txt
- ## requirements.txt

- sentence-transformers
- uvicorn
- ctransformers
- fastapi
- ipykernel
- langchain
- python-box
- streamlit
- langchain-community

## ▶️ Run the App

To run tests, run the following command

```bash
  streamlit run app.py

```


## Credits

- Model: Meta LLaMA 2
- Quantized format by ggml / ctransformers
- App built by: Deepika Vishwakarma
