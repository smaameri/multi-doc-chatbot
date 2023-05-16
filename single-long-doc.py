import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "sk-"

loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = loader.load()

chain = load_qa_chain(llm=OpenAI(), verbose=True)
query = 'Who is the CV about?'
response = chain.run(input_documents=documents, question=query)
print(response)