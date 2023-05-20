from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader

load_dotenv('.env')

pdf_loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = pdf_loader.load()

chain = load_qa_chain(llm=OpenAI())
query = 'Who is the CV about?'
response = chain.run(input_documents=documents, question=query)
print(response)