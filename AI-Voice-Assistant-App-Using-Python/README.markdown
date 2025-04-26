# AI Text-to-Speech Assistant

Welcome to the AI Text-to-Speech Assistant, a sophisticated voice-enabled chatbot that combines the power of OpenAI's GPT-3 for natural language processing with IBM Watson's Speech-to-Text and Text-to-Speech capabilities. This project delivers a user-friendly web application that allows users to interact with a virtual assistant through text or voice inputs, receiving contextually relevant responses in both text and audio formats. Designed to emulate the functionality of modern voice assistants like Google Assistant, this project showcases the integration of AI, web development, and speech processing technologies to create an engaging conversational experience.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Project Overview

The AI Text-to-Speech Assistant is a web-based chatbot that enables users to engage in natural, human-like conversations using both text and voice inputs. Powered by OpenAI's GPT-3 for generating intelligent responses and IBM Watson's speech processing for converting speech to text and text to speech, the assistant provides a seamless and accessible user experience. The frontend, styled with Bootstrap and enhanced with Font Awesome icons, offers a modern interface with light and dark mode options. The backend, built with Flask, handles API requests and integrates with external services to process user inputs and deliver responses. This project is ideal for learning about AI-driven applications, web development, and speech processing.

## Features

- **Voice and Text Interaction**: Users can communicate with the assistant via typed messages or voice recordings, with responses delivered in both text and audio formats.
- **Natural Language Processing**: Leverages OpenAI's GPT-3 to generate contextually relevant and coherent responses to user queries.
- **Speech Processing**: Utilizes IBM Watson's Speech-to-Text to transcribe user audio inputs and Text-to-Speech to convert responses into spoken audio.
- **Modern Web Interface**: Features a responsive UI with Bootstrap styling, Font Awesome icons, and a toggle for light/dark mode, ensuring an intuitive user experience.
- **Multilingual Support**: Supports multiple languages for speech recognition, including English, French, and more, as provided by Watson's models.
- **Customizable Responses**: Enables prompt engineering to tailor the assistant for specific roles, such as a therapist, mechanic, storyteller, or professor.
- **Cross-Platform Consistency**: Uses Docker to package the application and its dependencies, ensuring reliable performance across different environments.

## How It Works

The AI Text-to-Speech Assistant operates through a modular architecture that integrates frontend, backend, and external AI services:

1. **Frontend**: The web interface, built with HTML, CSS (styled via Bootstrap), and JavaScript (powered by jQuery), captures user inputs through a text box or microphone. The `script.js` handles interactivity, such as sending messages, recording audio, and toggling light/dark mode, while `style.css` manages visual aesthetics, including loading animations via CSS keyframes.
2. **Backend**: A Flask server (`server.py`) manages HTTP requests and routes. It includes:
   - A root endpoint (`/`) to serve the frontend (`index.html`).
   - A `/speech-to-text` endpoint to process audio inputs using Watson's Speech-to-Text API.
   - A `/process-message` endpoint to handle text inputs, query GPT-3 for responses, and convert responses to audio using Watson's Text-to-Speech API.
3. **Speech Processing**: The `worker.py` module contains functions to interact with Watson's APIs. The `speech_to_text` function transcribes audio, and the `text_to_speech` function generates audio from text, supporting various voices (e.g., Emily, Michael).
4. **Natural Language Processing**: The `openai_process_message` function sends user inputs to OpenAI's GPT-3, which generates intelligent responses based on the prompt and context.
5. **Deployment**: Docker containers package the application, ensuring consistent execution. Three containers run simultaneously: one for the Flask app, one for Speech-to-Text, and one for Text-to-Speech, orchestrated to handle all functionalities.

When a user interacts with the assistant, their input (text or voice) is sent to the Flask backend, which processes it through the appropriate APIs, generates a response, and returns it to the frontend for display and playback.

## Technologies Used

- **Python**: Core programming language for the backend and API integrations.
- **Flask**: Lightweight web framework for handling routes and HTTP requests.
- **OpenAI GPT-3**: Provides advanced natural language processing for response generation.
- **IBM Watson Speech Libraries**: Powers Speech-to-Text and Text-to-Speech functionalities.
- **HTML/CSS/JavaScript**: Builds the responsive and interactive frontend.
- **Bootstrap**: Enhances UI styling and responsiveness.
- **Font Awesome**: Adds icons for a polished interface.
- **jQuery**: Simplifies JavaScript operations for interactivity.
- **Docker**: Ensures consistent deployment across environments.

## Setup Instructions

To set up and run the AI Text-to-Speech Assistant locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anoro-r/chatapp-with-voice-and-openai-outline.git
   cd chatapp-with-voice-and-openai
   ```

2. **Install Docker**:
   - Ensure Docker is installed on your system. Download it from [Docker's official site](https://www.docker.com/get-started) if needed.

3. **Build and Run the Application**:
   ```bash
   docker build -t voice-chatapp-powered-by-openai .
   docker run -p 8000:8000 voice-chatapp-powered-by-openai
   ```
   - The application will be accessible at `http://localhost:8000`.

4. **Allow Pop-ups**:
   - Your browser may block the application tab. Enable pop-ups for `localhost:8000` to ensure the interface loads.

5. **Test Speech Services**:
   - Verify Watson's Speech-to-Text by running:
     ```bash
     curl https://sn-watson-stt.labs.skills.network/speech-to-text/api/v1/models
     ```
   - Verify Watson's Text-to-Speech by running:
     ```bash
     curl https://sn-watson-tts.labs.skills.network/text-to-speech/api/v1/voices
     ```

6. **Stop the Container**:
   - Press `Ctrl+C` in the terminal to stop the Docker container when done.

**Note**: The project requires an internet connection to access OpenAI and Watson APIs. You may need API keys for OpenAI and access to Watson services (available via free trials; see [Next Steps](#next-steps)).

## Usage

1. **Access the Application**:
   - Open `http://localhost:8000` in a web browser after running the Docker container.
   - Allow pop-ups if prompted to load the interface.

2. **Interact with the Assistant**:
   - **Text Input**: Type a message in the input box (e.g., "What can you specifically do?") and press Enter.
   - **Voice Input**: Click the microphone icon to record a message, which will be transcribed automatically.
   - Responses appear as text and are played as audio using the selected voice (e.g., Emily or Michael).

3. **Toggle Modes**:
   - Use the light/dark mode toggle to switch the interface theme for better visibility.

4. **Test Features**:
   - Try prompts like "What are the most famous shops in the Distillery District?" to see context-aware responses.
   - Experiment with voice inputs in different languages supported by Watson.

5. **Stop and Rebuild**:
   - If you modify the code, rebuild the Docker image and restart the container to test changes.

## Future Enhancements

- **Prompt Engineering**: Customize the assistant for specific roles (e.g., therapist, mechanic, storyteller) by designing tailored GPT-3 prompts.
- **Enhanced UI/UX**: Add animations, custom themes, or a chat history pane to improve user engagement.
- **Multilingual Expansion**: Integrate additional languages for GPT-3 responses to match Watson's multilingual capabilities.
- **Local Model Support**: Replace GPT-3 with an open-source model (e.g., LLaMA) to reduce dependency on external APIs.
- **Offline Mode**: Cache common responses or use local speech models for limited offline functionality.
- **Analytics Dashboard**: Track user interactions and response quality to refine the assistant's performance.

## Contributing

Contributions are welcome to enhance the AI Text-to-Speech Assistant! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a clear description of your changes.

Please ensure your contributions align with the project's goals and maintain code quality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project is created by Faizan Saleem Siddiqui, a passionate developer with an interest in natural language processing and Artificial Intelligence. With a background in Python programming and machine learning, they enjoy building AI-driven applications that make technology accessible and engaging. Faizan Saleem Siddiqui is an M. Phil Research Scholar, a freelancer, and Visiting Faculty Member at Quaid-i-Azam University Islamabad. He has been working in the field of Artificial Intelligence for the last 2 years as a freelancer as well as a researcher. There are more than 10 industrial & commercial projects to his credit. Learn more about him on his [LinkedIn Profile](https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/).

## Next Steps

To extend this project or integrate IBM Watson Speech Libraries into your own applications, sign up for free trials:
- [IBM Watson Speech-to-Text](https://www.ibm.com/cloud/watson-speech-to-text)
- [IBM Watson Text-to-Speech](https://www.ibm.com/cloud/watson-text-to-speech)

Explore prompt engineering to customize the assistant for specialized tasks, such as education, mental health support, or storytelling. With a robust UI/UX and creative prompts, this assistant can evolve into a powerful tool for various applications.