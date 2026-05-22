import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // Upload PDF
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "https://banking-rag-chatbot-0ki1.onrender.com/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      alert(response.data.message);
    } catch (error) {
      console.error(error);
      alert("File upload failed");
    } finally {
      setLoading(false);
    }
  };

  // Ask Question
  const handleAsk = async () => {
    if (!question) {
      alert("Please enter a question");
      return;
    }

    try {
      setLoading(true);

      const response = await axios.post(
        "https://banking-rag-chatbot-0ki1.onrender.com/chat",
        {
          session_id: "user1",
          question: question,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      alert("Error getting answer");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🏦 Banking RAG Chatbot</h1>

      <div className="card">
        <h2>Upload Banking PDF</h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button onClick={handleUpload}>
          Upload PDF
        </button>
      </div>

      <div className="card">
        <h2>Ask Questions</h2>

        <textarea
          rows="4"
          placeholder="Ask something about banking..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={handleAsk}>
          Ask Question
        </button>
      </div>

      {loading && <p>Loading...</p>}

      {answer && (
        <div className="answer">
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;