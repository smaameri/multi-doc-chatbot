import os
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader

os.environ["OPENAI_API_KEY"] = "sk-"

loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = loader.load()

chain = load_qa_chain(llm=OpenAI(), verbose=True)
query = 'Who is the CV about?'
response = chain.run(input_documents=documents, question=query)
print(response)