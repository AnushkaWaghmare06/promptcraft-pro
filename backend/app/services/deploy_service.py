# def generate_project(prompt: str, language: str):
#     # 🚧 Mock logic for now
#     return {
#         "project_name": "demo_project",
#         "files": {
#             "main.py": f"# Generated project for prompt: {prompt}\nprint('Hello from {language}!')"
#         }
#     }



import os
import subprocess
from typing import Optional

def deploy_frontend(project_path: str, provider="vercel") -> str:
    """
    Deploy frontend to Vercel or Netlify using CLI.
    Returns deployment URL.
    """
    try:
        if provider == "vercel":
            result = subprocess.check_output(
                ["vercel", "--prod", "--cwd", project_path],
                stderr=subprocess.STDOUT
            )
        elif provider == "netlify":
            result = subprocess.check_output(
                ["netlify", "deploy", "--dir=dist", "--prod", "--cwd", project_path],
                stderr=subprocess.STDOUT
            )
        else:
            return "Unsupported provider"
        
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Deployment failed: {e.output.decode()}"

def build_docker_image(project_path: str, image_name: str) -> str:
    """
    Build and tag Docker image for backend.
    """
    try:
        result = subprocess.check_output(
            ["docker", "build", "-t", image_name, project_path],
            stderr=subprocess.STDOUT
        )
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Docker build failed: {e.output.decode()}"

def push_docker_image(image_name: str) -> str:
    """
    Push Docker image to registry (Docker Hub).
    """
    try:
        result = subprocess.check_output(
            ["docker", "push", image_name],
            stderr=subprocess.STDOUT
        )
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Docker push failed: {e.output.decode()}"
