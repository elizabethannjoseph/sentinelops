import { useEffect, useState } from "react";
import "./App.css";

interface HealthResult {
  id: number;
  service_name: string;
  status: string;
  response_time_ms: number;
  checked_at: string;
}

function App() {
  const [results, setResults] = useState<HealthResult[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/health")
      .then((response) => response.json())
      .then((data) => setResults(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container">
      <h1>🛡️ SentinelOps</h1>
      <p className="subtitle">
        DevSecOps Health Monitoring Dashboard
      </p>

      <div className="grid">
        {results.map((result) => (
          <div className="card" key={result.id}>
            <h2>{result.service_name}</h2>

            <div className="status">
              <span
                className={
                  result.status === "Healthy" ? "dot green" : "dot red"
                }
              ></span>

              <span>{result.status}</span>
            </div>

            <div className="info">
              <p>
                <strong>Response Time</strong>
              </p>
              <p>{result.response_time_ms.toFixed(3)} ms</p>
            </div>

            <div className="info">
              <p>
                <strong>Last Checked</strong>
              </p>
              <p>{new Date(result.checked_at).toLocaleString()}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;