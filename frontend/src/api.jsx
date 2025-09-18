import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import GenerateProject from "./components/GenerateProject";
import ProjectsList from "./components/ProjectsList";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        {/* Navbar */}
        <nav className="bg-blue-600 text-white p-4 flex gap-6">
          <Link to="/" className="hover:underline">Generate</Link>
          <Link to="/projects" className="hover:underline">Projects</Link>
        </nav>

        {/* Pages */}
        <Routes>
          <Route path="/" element={<GenerateProject />} />
          <Route path="/projects" element={<ProjectsList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
