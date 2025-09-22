// frontend/src/context/ProjectContext.jsx
import React, { createContext, useState } from "react";
import axios from "axios";

// Create context
export const ProjectContext = createContext();

// Provider component
export const ProjectProvider = ({ children }) => {
  const [frontendCode, setFrontendCode] = useState("");
  const [backendCode, setBackendCode] = useState("");

  // Function to save project to backend
  const saveProject = async (projectId, name, description) => {
    try {
      const response = await axios.put(`/api/v1/projects/${projectId}/save`, {
        name,
        description,
        frontend_code: frontendCode,
        backend_code: backendCode,
      });
      return response.data; // return updated project
    } catch (error) {
      console.error("Error saving project:", error);
      throw error;
    }
  };

  return (
    <ProjectContext.Provider
      value={{
        frontendCode,
        backendCode,
        setFrontendCode,
        setBackendCode,
        saveProject,
      }}
    >
      {children}
    </ProjectContext.Provider>
  );
};
