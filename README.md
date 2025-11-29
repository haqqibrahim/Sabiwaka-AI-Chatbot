# Sabiwaka AI API

The Sabiwaka API provides an AI-powered assistant for navigating transport routes in Abuja. It uses the Groq API to generate helpful responses based on predefined route information.

## API Usage (For Consumers)

If you are consuming the hosted API, here is how to interact with it.

**Base URL**: `http://localhost:8000` (Replace with actual host if deployed)

### 1. Health Check

Check if the API is running.

- **Endpoint**: `GET /`
- **Response**:
  ```json
  {
    "message": "Hello World"
  }
  ```

### 2. Get AI Response

Send a message to the AI assistant to get route directions.

- **Endpoint**: `POST /ai`
- **Headers**:
  - `Content-Type`: `application/json`
- **Request Body**:
  ```json
  {
    "message": "Your question here, e.g., How do I get from Nyanya to Wuse?"
  }
  ```
- **Response**:
  ```json
  {
    "response": "The AI's helpful response with directions..."
  }
  ```

### Example Request (cURL)

```bash
curl -X POST "http://localhost:8000/ai" \
     -H "Content-Type: application/json" \
     -d '{"message": "How do I get from Berger to Dutse?"}'
```

---

## Setup & Self-Hosting (For Developers)

If you want to host the API yourself or contribute to the development, follow these steps.

### Prerequisites

- Python 3.8 or higher

### Installation

1.  **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd sabiwaka
    ```

2.  **Create a virtual environment**:

    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `.env` file in the root directory.
2.  Add your Groq API key (required for the AI model):
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

### Running the Application

Start the server using `uvicorn`:

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
You can also view the interactive API docs at `http://127.0.0.1:8000/docs`.
