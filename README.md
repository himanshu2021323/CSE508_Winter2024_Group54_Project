#Information Retrieval Project
##Intelligent Teaching Assistant chatbot

ITA Chatbot Code File Repository : https://github.com/param934/ITA-Chatbot.git

Welcome to our innovative AI-powered application, designed to offer a versatile and user-friendly experience. Our application integrates multiple advanced technologies, allowing users to interact with audio, images, and PDFs with ease. This README provides an overview of our methodologies, key features, and how the application works.

Key Features
1. Quantized Model Integration
   - Our application uses quantized models—optimized versions of larger AI models—to ensure efficient performance on consumer-grade hardware. This allows for accessibility to a wider user base without requiring high-end computing resources.

2. Audio Chatting with Whisper AI
   - We integrate Whisper AI to provide an enhanced audio chatting experience. Its robust transcription capabilities allow for accurate interpretation and response to voice inputs, facilitating smooth and natural conversations.

3. Image Chatting with LLaVA
   - The application integrates LLaVA, a fine-tuned LLaMA model, to enable image-based chatting. It understands image embeddings created using a CLIP model, enabling users to discuss and share visual content within the chat.

4. PDF Chatting with Custom ITA Model
   - The custom ITA Chatbot allows users to upload PDFs and ask questions about the content. This involves:
     - Data Extraction: The chatbot extracts text from PDFs, segmenting each page and structuring the data for processing.
     - Text Cleaning: The text is cleaned to remove unwanted characters and ensure consistency (e.g., standardizing to lowercase).
     - Text Vectorization: The cleaned text is converted into numerical vectors through tokenization, word embeddings, and document vectorization.
     - Knowledge Base Storage: The vectorized data is stored in a knowledge base with relevant metadata for quick retrieval and efficient search.
     - Similarity Search: When a user asks a question, the chatbot finds the most relevant information through similarity matching. It converts the user's query into a vector representation and matches it with similar vectors in the knowledge base.

5. SQLite Database for Chat History
   - We use a SQLite database to store and manage chat history. This ensures that users can access their past interactions, providing a seamless and continuous user experience.

 How It Works
The application integrates these technologies to provide a cohesive and responsive user experience. Each component is designed to work in harmony with others, allowing users to interact with audio, images, and PDFs seamlessly. The following steps describe how these features work together:

1. Initialization: The application initializes the quantized models and establishes the required resources for audio, image, and PDF processing.

2. User Interaction: Users can interact with the application through various modes—audio, images, and PDFs. Each interaction mode has specific functionalities:
   - Audio: Users can send voice messages, which are transcribed by Whisper AI.
   - Images: Users can share images, which are processed by LLaVA.
   - PDFs: Users can upload PDFs and ask questions, which the custom ITA Chatbot answers through its knowledge base.

3. Processing and Response: Each interaction is processed according to its mode. The application uses advanced AI techniques to analyze the input and generate appropriate responses.

4. Chat History Management: The SQLite database stores chat history, enabling users to revisit past interactions. This feature ensures continuity and convenience for users.

**Link 1**
https://youtu.be/5P2ywmCIVgs (Presentation)
**Link 2**
https://youtu.be/-LhPY59WfBo (Chatbot Demonstration)

