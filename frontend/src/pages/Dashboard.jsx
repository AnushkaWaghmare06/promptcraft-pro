// frontend/src/pages/Dashboard.jsx


import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Dashboard() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    const res = await axios.get("/api/v1/projects/user/1"); // replace with current user id
    setProjects(res.data);
  };

  const exportProject = (id) => {
    window.open(`/api/v1/projects/${id}/export`);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">My Projects</h2>
      <ul>
        {projects.map((p) => (
          <li key={p.id} className="flex justify-between items-center mb-2 border p-2 rounded">
            <span>{p.name}</span>
            <button onClick={() => exportProject(p.id)} className="bg-green-500 text-white p-1 rounded">
              Export ZIP
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
