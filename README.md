# MedicalChatBot 🤖⚕️

This is a conversational AI chatbot designed for medical purposes. It helps users by providing health-related information and advice, utilizing natural language processing (NLP) models. The chatbot is powered by state-of-the-art machine learning techniques to interpret and respond to user queries related to healthcare, symptoms, medications, and general medical knowledge.

## Features

- **Health Assistance:** Provides general information about symptoms, diseases, and medications.
- **Medical Query Responses:** The chatbot answers user queries based on an indexed medical knowledge base.
- **State-of-the-art AI:** Uses Pinecone for vector search, Groq API for language model processing, and Hugging Face embeddings for semantic understanding.
- **Customizable and Scalable:** Easy to extend for additional models or data sources.

## Technologies Used

- **Python:** Programming language.
- **Flask:** Web framework for serving the chatbot interface.
- **Langchain:** A framework that simplifies the creation of LLM-based applications.
- **Pinecone:** Vector database for efficient semantic search.
- **Groq API:** Powerful API for running AI models like `llama3-8b-8192`.
- **Hugging Face:** Used for downloading and using pre-trained embeddings for text.
- **Dotenv:** To manage sensitive environment variables.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/M-Awais-Hussain/MedicalChatBot.git
   cd MedicalChatBot
   ```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Set up environment variables:
```
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```
4. Run the application:
```
python app.py
```

## Contributing
- Fork the repository.

- Create a new branch (git checkout -b feature-branch).

- Make your changes.

- Commit your changes (git commit -am 'Add new feature').

- Push to the branch (git push origin feature-branch).

- Open a pull request.

## License
This project is licensed under the MIT License
