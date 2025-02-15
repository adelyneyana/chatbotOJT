# Chatbot System

**Description:**  
This project is a simple backend for a chatbot that uses the Hugging Face `transformers` library to answer user questions based on predefined contexts. The backend uses Flask for handling API requests and supports communication with the frontend to simulate a conversation.

## Table of Contents

1. Prerequisites
2. Backend Setup (Flask)  
   - Clone Repository  
   - Install Dependencies  
   - Environment Configuration  
   - Run the Flask Server  
3. Testing the Backend  
   - Using Thunder Client (VS Code Extension)  
4. Frontend Setup (React)  
   - Clone Repository  
   - Install Dependencies  
   - Environment Configuration  
   - Run the React App  
5. Push Updates to the Repository

## Prerequisites

Ensure you have the following installed on your computer:

- **Python** (v3.8 or higher)
- **pip** (Python package manager)
- **Virtual Environment (venv)**
- **TensorFlow** (for Hugging Face transformers)  
  - Run `pip install tensorflow` if not already installed.
- **Flask**  
  - Run `pip install flask` if not already installed.
- **Hugging Face Transformers**  
  - Run `pip install transformers` if not already installed.

## Backend Setup (Flask)

### 1. Clone Repository

- Clone the backend repository using:
  ```bash
  git clone https://github.com/adelyneyana/chatbotOJT.git
  cd chatbotOJT/backend
  ```

### 2. Install Dependencies

- Create a virtual environment and activate it:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate  # For Windows
  source venv/bin/activate  # For macOS/Linux
  ```

- Install the necessary dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Environment Configuration

- Create a `.env` file in the root directory (if not already present) and add your configuration if needed. Currently, no specific environment variables are required for this setup.

### 4. Run the Flask Server

- After setting up the environment and dependencies, you can start the Flask server:
  ```bash
  python app.py
  ```

- The server will start and listen on `http://127.0.0.1:5000`.

## Testing the Backend

You can test the backend API by sending POST requests to `http://127.0.0.1:5000/chat`.

### Using Thunder Client (VS Code Extension)

1. **Install Thunder Client**:
   - Open VS Code and go to the Extensions tab (Ctrl+Shift+X).
   - Search for **Thunder Client** and install it.

2. **Send a POST Request**:
   - Open Thunder Client from the sidebar in VS Code.
   - Click on the **+ New Request** button.
   - Set the **Request Type** to **POST**.
   - Enter the URL `http://127.0.0.1:5000/chat`.
   
3. **Configure Request Body**:
   - In the **Body** section, choose **JSON** as the format.
   - Add the following JSON data:
     ```json
     {
       "message": "What is France known for?"
     }
     ```
   
4. **Send the Request**:
   - Click **Send** to test the backend.
   - The response should contain the chatbot's answer and suggestions.

## Frontend Setup (React)

### 1. Clone Repository

- Clone the frontend repository using:
  ```bash
  git clone https://github.com/adelyneyana/chatbotOJT.git
  cd chatbotOJT
  ```

### 2. Install Dependencies

- Install the necessary dependencies:
  ```bash
  npm install
  ```

### 3. Environment Configuration

- Navigate to the `src/constants/constant.js` file.
- Update the `API_URL` variable to match your backend server URL (e.g., `http://127.0.0.1:5000`).

### 4. Run the React App

- To start the React app:
  ```bash
  npm start
  ```
- The app will be accessible on `http://localhost:3000`.

## Push Updates to the Repository

Before making any changes or pushing updates to the repository, always make sure to pull the latest changes from the `master` branch.

### 1. Pull Latest Changes

```bash
git pull origin master
```

### 2. Push Your Changes

After making changes, commit and push to the `master` branch:

```bash
git add .
git commit -m "Your commit message"
git push origin master
```

---

