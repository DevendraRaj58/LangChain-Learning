from langchain_community.document_loaders import WebBaseLoader
url='https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7w4hn-a/p/itma22c00e6cdaf0'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs)
print(docs[0].page_content)