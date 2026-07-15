from langchain_classic.text_splitter import RecursiveCharacterTextSplitter,Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)

text = '''
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        # Remove empty values
        return [d for d in self.data if d is not None]

    def process_all(self):
        cleaned = self.clean_data()
        results = []
        for item in cleaned:
            results.append(item * 2)
        return results

def main():
    processor = DataProcessor([1, 2, None, 4])
    print(processor.process_all())

if __name__ == "__main__":
    main() 

'''

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0])
