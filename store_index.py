from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings

import time
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

import os
from dotenv import load_dotenv
load_dotenv()

# pinecone_instance = pinecone.Pinecone(
#     api_key=os.getenv("PINECONE_API_KEY"),
#     environment=os.getenv("PINECONE_ENV"),
# )

pinecone_api_key = os.environ.get("PINECONE_API_KEY")

extracted_data = load_pdf_file(data = 'Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"
pc = Pinecone(api_key = pinecone_api_key)
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name=index_name, 
    embedding=embeddings
)
