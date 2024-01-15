from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAI

load_dotenv('.env')

pdf_loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = pdf_loader.load()

chain = load_qa_chain(llm=OpenAI())
query = 'Who is the CV about?'
response = chain.invoke({"input_documents": documents, "question": query})
print(response["output_text"])
