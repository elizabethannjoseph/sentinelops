import { Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import History from "./pages/history";
import "./App.css";
function App(){

  return (
    <>
      <nav className="navbar">
        <Link to="/">Dashboard</Link>
        <Link to="/history">History</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </>
  );
}

export default App;