import React from "react";
import Dashboard from "./components/Dashboard.jsx";
import GenerateProject from "./components/GenerateProject.jsx";

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <h1 className="text-3xl font-bold p-4">PromptCraft Pro</h1>
      <GenerateProject />
      <Dashboard />
    </div>
  );
}

export default App;
