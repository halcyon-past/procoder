# ProCoder - AI Chat App

ProCoder is an AI-powered chat application built with Streamlit and OpenAI's API. This app allows users to interact with AI models from OpenAI in a conversational interface. Users can select different models, engage in conversation, and receive responses from the AI in real-time.

## Features

- **Model Selection**: Choose from multiple AI models.
- **Conversational Memory**: Keeps track of conversation history during the session.
- **User-Friendly Interface**: Built with Streamlit for a responsive and interactive chat experience.
- **Customizable Design**: Clean, modern layout with footer links for easy navigation.
- **Password Protection**: Added Password protection to make sure your api is not used by someone else.

## Setup

### Prerequisites

- **Python Version**: Ensure you have Python 3.10.15 installed.
- **Conda**: To manage dependencies and environments.

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:halcyon-past/procoder.git
   cd procoder
   ```

2. **Create a Conda Environment**:
   ```bash
   conda create -n procoder python=3.10.15
   conda activate procoder
   ```

3. **Install Required Libraries**:
   Install the libraries from the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     PASSWORD=your_password_here
     ```

5. **Run the App**:
   Launch the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```

### Usage

- Once the app is running, open it in a browser.
- Choose your preferred AI model from the dropdown menu.
- Type messages in the chat input box, and ProCoder will respond based on the selected model.

## Project Structure

- **app.py**: Main application file.
- **requirements.txt**: List of required Python packages.
- **.env**: Environment variables (API keys).
- **README.md**: Documentation file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

Made with ❤️ by Aritro Saha  
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/halcyon-past)      [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aritro-saha/)    [![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=#FF7139)](https://aritro.tech/)    [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@veripyed)
