from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=400,chunk_overlap=0)

text = '''
    Artificial intelligence has rapidly transformed the technological landscape, becoming an integral part of modern software development. Machine learning algorithms, neural networks, and automated data processing tools allow companies to analyze vast datasets at unprecedented speeds. This evolution has driven significant advancements across multiple fields, ranging from healthcare diagnostics to automated financial trading.

    At the heart of these innovations are large language models, which process human language to generate conversational responses, write complex code, and summarize lengthy documents. To maximize the utility of these models, developers often rely on prompt engineering to guide the AI's output. By carefully crafting input instructions, users can steer the system to produce highly specific, accurate, and contextually relevant answers for a wide variety of tasks.
'''


chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)