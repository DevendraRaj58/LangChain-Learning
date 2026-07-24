from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(
    file_path=r'E:\Langchain\doc_loaders\first 3 page.pdf',
)


docs = loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)


 