from langchain_community .document_loaders import CSVLoader
loader = CSVLoader(file_path='E:\Langchain\doc_loaders\Telco-Customer-Churn.csv')

data = loader.load()

print(data[45]) # 45 represents the row number for our corresponding csv file.
print(data[:3].page_content) 
print(data[0].metadata)

