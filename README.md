🤖 ChatBot AI - FastAPI

✨ About the Project

This is an AI-powered chatbot built with FastAPI and g4f (a free ChatGPT alternative), supporting both Persian and English languages. This project allows you to set up a chatbot API for natural conversations without requiring an OpenAI API key.

⚙️ Features

Supports both Persian and English

Uses g4f for natural language responses (no API key required)

Built with FastAPI for high performance and scalability

Comes with Swagger UI for automatic API documentation

Can be deployed locally or on a server

⛓ Prerequisites

To run this project, you need to have the following installed:

Python 3.8+

Git

Virtual Environment (optional but recommended)

⭐ Installation and Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/chat_IA.git
cd chat_IA

2️⃣ Create and Activate Virtual Environment (Optional but Recommended)

python -m venv env
# On Windows:
.env\Scripts\activate
# On macOS and Linux:
source env/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run FastAPI Server

uvicorn main:app --reload

✅ The server should now be running at http://127.0.0.1:8000!

🔍 Testing the API

Once the server is running, you can check the Swagger UI documentation at:

http://127.0.0.1:8000/docs

Or send a test request using cURL:

curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"message\": \"Hi , how are you?\"}"


🚀 Deploying on a Server

This project can be deployed on a server or within Docker. Some deployment methods include:

Using Gunicorn with Uvicorn:

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

Running inside Docker (in development)

🛠️ Developers

Abbas Salahi (@abbas-salahi-code)

Other contributors 🚀

🌟 Contributions

If you have any ideas to improve this project, feel free to Fork and submit a Pull Request!

⚖️ License

This project is released under the MIT License.

✨ Enjoy and enhance this project! 🎉

