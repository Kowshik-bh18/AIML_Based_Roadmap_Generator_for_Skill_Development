 <div align="center">
  <h1>AIML-Based Roadmap Generator for Skill Development</h1>
</div>


<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LLM-RAG-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Endee-Vector_DB-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/HuggingFace-Models-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-Mistral_7B-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
</div>

<div align="center">
  <h3>
    An intelligent AI-powered personalized roadmap generator designed for students,
    professionals, and learners using Retrieval Augmented Generation (RAG),
    Vector Databases, Large Language Models, and AI-driven document assistance.
  </h3>

  <p>
    Built using Django, Python, Endee Vector Database (Docker),
    Sentence Transformers, RAG-based roadmap generation chatbot,
    NotebookLM-style document assistant, authentication & subscription system,
    admin approval workflow, automated email notifications,
    and LLM integration via API/local deployment.
    Deployed on PythonAnywhere.
  </p>

  <br>

  <a href="https://rmpai.pythonanywhere.com/" style="font-size:22px; font-weight:bold;">
     Live Demo
  </a>

  <p style="margin-top:10px; font-size:14px;">
    Note: Live demo requires the AI endpoint to be active.
    If it is not responding, please ping me using the contact details below —
    I’ll start the endpoint so you can experience the full features.
  </p>
</div>


---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [AI/ML Architecture](#aiml-architecture)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contributors](#contributors)
* [Contact](#contact)

---

## Features

### AI-Powered Learning

* Personalized **skill roadmaps** generated using LLMs with structured day-wise guidance  
* **RAG (Retrieval Augmented Generation)** pipeline for context-aware and accurate responses  
* Vector search using **Endee Vector Database (Docker-based persistent storage)**  
* Support for **Pinecone Vector DB (alternate branch implementation)**  
* AI-powered **NotebookLM-style document assistant** for analyzing uploaded notes, PDFs, and study materials  
* Custom AI query answering using **local/remote LLMs (Mistral / API-based models)**  
* Semantic search using **Sentence Transformers embeddings**

### User System

* Secure authentication (Login / Register / Guest mode)  
* Premium subscription workflow with **admin approval system**  
* Automated **email notifications** for:
  - Successful registration  
  - Subscription approval / rejection  
  - Admin alerts for new subscription requests  
* Usage/request limits for free users  

### Smart Chat System

* Persistent AI chat memory  
* RAG-powered intelligent chatbot for roadmap generation  
* Notebook document upload + contextual AI chat  
* Export chats as:
  - PDF  
  - JSON  
  - TXT  
  - PPTX  

### Admin Features

* Admin dashboard for subscription approval/rejection  
* Email notification system for admin actions  
* User activity and subscription monitoring  

### UI / UX

* Modern responsive Bootstrap interface  
* Smooth animations and interactive components  
* Clean dashboard layout  
* Dark mode support  

### Deployment & Infrastructure

* Django backend deployed on **PythonAnywhere**  
* Vector database via **Docker (Endee OSS)** with persistent volume storage  
* AI models runnable via:
  - Local LLM (Ollama / Colab / API endpoint)  
  - HuggingFace endpoints (optional)  
* Flexible architecture supporting multiple vector DBs and LLM providers  

---

## 📸 Project Screenshots

###  User Login Page
<img src="screenshots/login-page.png" width="900"/>

### Subscription Request System
<img src="screenshots/subscription-request.png" width="900"/>

### Subscription Approval System
<img src="screenshots/admin-dashboard.png" width="800"/>

### User Email Notification (Registration / Subscription Status)
<img src="screenshots/user-email-notification.png" width="900"/>

### Admin Email Notification for Approval
<img src="screenshots/admin-email-notification.png" width="900"/>

### Endee Vector DB Dashboard
<img src="screenshots/endee-dashboard.png" width="800"/>

### Docker + Endee Vector Database Setup
<img src="screenshots/docker-endee-setup.png" width="900"/>

### RAG Chatbot Roadmap Generator
<img src="screenshots/rag-chatbot.png" width="900"/>

### NotebookLM-Style Document Assistant
<img src="screenshots/notebooklm-dashboard.png" width="900"/>
<img src="screenshots/notebooklm-feature.png" width="900"/>
<img src="screenshots/notebooklm-feature-1.png" width="900"/>

---

## Tech Stack

### **Backend**

* Django (Python Web Framework)
* Python 3
* REST API Architecture
* Endee Vector Database (Docker-based persistent vector storage)
* Pinecone Vector DB (alternate implementation branch)
* Retrieval-Augmented Generation (RAG Pipeline)
* Local / Remote LLM Integration (Mistral, API endpoints, Colab-hosted models)

### **Frontend**

* HTML5, CSS3, JavaScript
* Bootstrap (Responsive UI Framework)

### **AI / ML**

* Sentence Transformers / Hugging Face Embeddings
* Mistral LLM (via Ollama / API endpoint)
* Semantic Vector Search + Context Retrieval
* NotebookLM-style Document Understanding Module

### **Deployment & Infrastructure**

* PythonAnywhere (Live Django Backend)
* Docker (Endee Vector DB deployment with persistent volumes)
* Ngrok / API Endpoint Exposure for remote LLM access
* HuggingFace Space / Local LLM hosting (Optional)

---


## AIML Architecture

```
User → Query → Embedding Model → Endee Vector DB → Relevant Chunks → LLM (Mistral 7B) → Final Answer
```

Flow:

1. User asks a question
2. Convert query to embedding
3. Search Endee vector DB
4. Retrieve top matches
5. Feed context to Mistral-7B (RAG)
6. AI produces a structured and accurate answer

---

## Project Structure

```
AIML_Based_Roadmap_Generator_for_Skill_Development/
│
├── ai_app/                 # Main app: roadmap AI, chat, premium
├── ai_notebook/            # NotebookLM-like AI processing
├── ai_roadmap_app/         # Django project settings
├── notebook_files/         # Uploaded documents
├── static/                 # JS/CSS/Images
├── media/                  # User uploads
│
├── manage.py
├── requirements.txt
├── test.py
└── README.md
```

---

## Installation

### Prerequisites

* Python 3.10+
* Git
* Docker Desktop (for Endee Vector DB)
* Ollama installed (optional – for local LLM)
* Hugging Face / API Endpoint Token (optional if using remote LLM)
### Step 1: Clone

```bash
git clone https://github.com/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development.git
cd AIML_Based_Roadmap_Generator_for_Skill_Development
```

### Step 2: Virtual Environment

```bash
python -m venv myenv
myenv/Scripts/activate
pip install -r requirements.txt
```

### Step 3: Django Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Step 4: Setup Endee Vector Database (Docker)

This project uses Endee OSS Vector Database for RAG storage instead of Pinecone.

# Substeps:

Clone Endee Repository

git clone [https://github.com/endee-ai/endee.git](https://github.com/endee-ai/endee.git)
cd endee

Build Docker Image

docker build -t endee-local .

Run Container With Persistent Volume

docker run -d 
--name endee-db 
-p 9090:8080 
-v endee-data:/data 
endee-local

Volume ensures:

 - Persistent vector storage

 - No data loss on restart

 - Local RAG database access

Base API URL:
[http://localhost:9090/api/v1](http://localhost:9090/api/v1)

Verify Container

docker ps

Health Check:
[http://localhost:9090/api/v1/health](http://localhost:9090/api/v1/health)

Expected Response:
{"status":"ok"}

### Step 5: Configure LLM (Local)

```bash
ollama run mistral
```

### Step 6: Run Project & Test RAG Pipeline

Start Django server

python manage.py runserver

Open in browser

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

 Login / Register:

* Create account or login as guest
* Access roadmap generator chat
* Upload notebook documents (NotebookLM feature)
* Test RAG roadmap generation

 Ensure These Services Are Running:

✔ Django server running
✔ Endee Docker container active
✔ LLM endpoint (Colab / local model) running

 Quick API Test (Optional)

curl [http://localhost:9090/api/v1/health](http://localhost:9090/api/v1/health)

Expected Output:
{"status":"ok"}

 If roadmap generation fails:

* Check Endee container → docker ps
* Check LLM endpoint → ngrok/colab running
* Check Django logs for API errors
---

## Contributing

Want to improve this project?

1. Fork repo
2. Create branch
3. Commit changes
4. Open Pull Request

---

## Contributors

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/Kowshik-bh18.png" width="100px;" />
        <br><b>Kowshik BH</b><br>
        <a href="https://github.com/Kowshik-bh18">Developer</a>
      </td>
    </tr>
  </table>
</div>

---

## Acknowledgement

This project is an enhanced version of my earlier AI roadmap generator.  
I would like to acknowledge my friends who supported me during the initial stages of development, especially in areas such as model fine-tuning experiments, data collection, and web scraping.  

Their inputs and feedback helped strengthen the foundation of this project.  
The current version builds upon that work with improved RAG architecture, NotebookLM-style document intelligence, better system design, and additional AI-driven features aimed at providing a more practical and production-ready learning assistant.

Grateful for their support and encouragement throughout this journey.

---

## Contact

<div align="center">

### **Kowshik BH**

[Email](mailto:kowshikbh18@gmail.com) | [LinkedIn](https://www.linkedin.com/in/kowshikbh) | [GitHub](https://github.com/Kowshik-bh18)

</div>

---

<div align="center">
  <h3>⭐ If you like this project, consider starring the repo!</h3>
</div>
