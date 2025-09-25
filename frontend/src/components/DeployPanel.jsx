import React, { useState } from "react";
import axios from "axios";

export default function DeployPanel() {
  const [logs, setLogs] = useState("");

  const deployFrontend = async () => {
    const res = await axios.post("/api/v1/deploy/frontend", {
      project_path: "./projects/frontend",
      provider: "vercel",
    });
    setLogs(res.data.deployment_result);
  };

  const deployBackend = async () => {
    const res = await axios.post("/api/v1/deploy/backend/docker", {
      project_path: "./projects/backend",
      image_name: "myusername/mybackend:latest",
    });
    setLogs(res.data.build_log + "\n" + res.data.push_log);
  };

  return (
    <div className="border p-4 rounded mt-4">
      <h3 className="font-bold mb-2">🚀 Deploy Your App</h3>
      <button onClick={deployFrontend} className="bg-green-500 text-white p-2 rounded mr-2">
        Deploy Frontend
      </button>
      <button onClick={deployBackend} className="bg-blue-500 text-white p-2 rounded">
        Deploy Backend
      </button>
      <pre className="bg-black text-white p-2 mt-4 overflow-x-auto">{logs}</pre>
    </div>
  );
}
