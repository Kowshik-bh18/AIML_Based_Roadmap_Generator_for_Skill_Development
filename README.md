# AIML-Based Roadmap Generator for Skill Development (Endee + RAG Version)

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/RAG-LLM-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Endee-Vector_DB-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/Bootstrap-Frontend-563D7C?style=for-the-badge&logo=bootstrap" />
</div>

---

## Overview

This project is an AI-powered personalized learning roadmap generator built using Retrieval-Augmented Generation (RAG), Large Language Models, and Vector Databases.
It helps students, professionals, and learners generate structured learning roadmaps, analyze documents, and interact with AI-driven assistants.

Originally implemented using Pinecone, this final evaluation version uses the Endee vector database deployed via Docker as required for project evaluation.

---

## Live Demo

[https://rmpai.pythonanywhere.com/](https://rmpai.pythonanywhere.com/)

---

## Core Features

### AI / RAG Capabilities

* Personalized AI-generated skill roadmaps
* Retrieval-Augmented Generation (RAG) architecture
* Endee vector database for semantic search
* Local embedding models for document understanding
* NotebookLM-style document assistant
* Context-aware AI chat responses

---

### User System

* Secure login and registration
* Premium subscription workflow
* Admin approval/rejection system
* Email notifications for:

  * Registration success
  * Subscription approval/rejection
  * Admin alerts

---

### AI Chat & Notebook Assistant

* Persistent AI chat history
* Document upload and analysis
* Semantic search over uploaded notes
* Export chat responses (PDF / JSON / TXT / PPTX)

---

### Admin Dashboard

* Subscription approval interface
* User monitoring
* Email notification automation
* Premium request management

---

### Deployment & Infrastructure

* Dockerized Endee vector DB
* Django backend
* Bootstrap frontend
* Local LLM hosting via Colab / API endpoint
* Production deployment on PythonAnywhere

---

## System Architecture (RAG Pipeline)

User Query
→ Embedding Model
→ Endee Vector DB Retrieval
→ Relevant Context
→ LLM Generation
→ Final AI Response

This ensures:

* Contextually accurate answers
* Reduced hallucinations
* Domain-aware roadmap generation

---

## Screenshots

### Docker + Vector Database

(Add your images here)

* Docker container running Endee
* Vector index creation dashboard
* Vector insertion logs

Example:

```
![Docker Container](screenshots/docker_container.png)
![Endee Dashboard](screenshots/endee_dashboard.png)
![Vector Insert](screenshots/vector_insert.png)
```

---

### AI Application UI

(Add screenshots)

* Login page
* Roadmap generator chat
* RAG chatbot interface
* NotebookLM document assistant

Example:

```
![Login](screenshots/login.png)
![Roadmap Generator](screenshots/roadmap_chat.png)
![RAG Chatbot](screenshots/rag_chat.png)
![Notebook Assistant](screenshots/notebook_ai.png)
```

---

### Subscription & Admin Workflow

(Add screenshots)

* User profile page
* Subscription request
* Admin approval dashboard
* Email notification samples

Example:

```
![User Profile](screenshots/profile.png)
![Subscription Request](screenshots/subscription.png)
![Admin Dashboard](screenshots/admin_dashboard.png)
![Approval Email](screenshots/email_notification.png)
```

---

## Technology Stack

### Backend

* Django
* Python
* REST APIs
* Endee Vector Database
* Docker Containerization

### Frontend

* HTML5 / CSS3
* Bootstrap
* JavaScript

### AI/ML Components

* Sentence Transformers embeddings
* RAG architecture
* Local or hosted LLM endpoint
* Notebook-style AI assistant

---

## Installation Guide

### Clone Repository

```
git clone https://github.com/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development.git
cd AIML_Based_Roadmap_Generator_for_Skill_Development
```

---

### Create Virtual Environment

```
python -m venv myenv
myenv/Scripts/activate
pip install -r requirements.txt
```

---

### Run Endee Vector DB (Docker)

```
docker run -d ^
  --name endee-db ^
  -p 9090:8080 ^
  -v endee-data:/data ^
  endee-local
```

This ensures vector data persistence across restarts.

---

### Django Setup

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

### Configure Environment Variables

Example `.env`:

```
ENDEE_BASE_URL=http://localhost:9090/api/v1
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
```

---

## Project Structure

```
ai_app/
ai_notebook/
ai_roadmap_app/
media/
static/
docker/
notebook_files/
manage.py
requirements.txt
README.md
```

---

## Contribution Workflow

1. Fork repository
2. Create feature branch
3. Commit changes
4. Submit pull request

---

## Contributors

Kowshik BH — Lead Developer
Madhu Sudhan — Contributor
MD Ganesha — Contributor

---

## Contact

Email: [kowshikbh18@gmail.com](mailto:kowshikbh18@gmail.com)
GitHub: [https://github.com/Kowshik-bh18](https://github.com/Kowshik-bh18)
LinkedIn: [https://linkedin.com/in/kowshikbh](https://linkedin.com/in/kowshikbh)

---

## Important Note for Evaluators

This repository contains multiple experimental branches.

The final evaluation implementation uses:

* Endee vector database
* Docker deployment
* RAG architecture

Please refer to the Endee implementation branch for project evaluation.

---

If you found this project useful, please consider starring the repository.
