import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

load_dotenv('.env')

# load the document as before
loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = loader.load()

# we split the data into chunks of 1,000 characters, with an overlap
# of 200 characters between the chunks, which helps to give better results
# and contain the context of the information between chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(documents)

# we create our vectorDB, using the OpenAIEmbeddings tranformer to create
# embeddings from our text chunks. We set all the db information to be stored
# inside the ./data directory, so it doesn't clutter up our source files
vectordb = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
    persist_directory='./data'
)
vectordb.persist()

# we create the RetrievalQA chain, passing in the vectorstore as our source of
# information. Behind the scenes, this will only retrieve the relevant
# data from the vectorstore, based on the semantic similiarity between
# the prompt and the stored information
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
    return_source_documents=True
)

# we can now exectute queries againse our Q&A chain
result = qa_chain({'query': 'Who is the CV about?'})
print(result['result'])
