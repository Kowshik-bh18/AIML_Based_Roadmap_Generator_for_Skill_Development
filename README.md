# 🧠 AIML_Based_Roadmap_Generator_for_Skill_Development

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</div>

<div align="center">
  <h3>A comprehensive Django-based web application for generating skill-development roadmaps, NotebookLM-style note integration, and AI-powered chat workflows.</h3>
  <p>Live demo: 🔗 <a href="https://rmpai.pythonanywhere.com/">https://rmpai.pythonanywhere.com/</a></p>
</div>

---

## 📋 Table of Contents

- [Features](#-features)  
- [Project Structure](#-project-structure)  
- [Technologies Used](#️-technologies-used)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Contact](#-contact)  
- [Contributors](#-contributors)  

---

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/🧭-Roadmap_Generator-blue?style=for-the-badge" alt="Roadmap"/>
        <br><strong>Skill Roadmap AI</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/📓-NotebookLM_Mini-green?style=for-the-badge" alt="NotebookLM"/>
        <br><strong>NotebookLM-style Notes</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/💬-AI_Chat_Integration-orange?style=for-the-badge" alt="Chat"/>
        <br><strong>AI Chat Interface</strong>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/🔒-User_Auth_and_Subscriptions-purple?style=for-the-badge" alt="Auth"/>
        <br><strong>User Authentication & Premium Access</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/📊-Usage_Limits_and_Tracking-red?style=for-the-badge" alt="Usage"/>
        <br><strong>Usage & Request Tracking</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/📁-Export_Chat_Downloads-yellow?style=for-the-badge" alt="Export"/>
        <br><strong>Export Chat History</strong>
      </td>
    </tr>
  </table>
</div>

### Additional Highlights:
- 🗂️ Secure Uploads & File Handling  
- 🛡️ Role-based Access (Free vs Premium)  
- 📱 Responsive Design – Works across devices  
- ⚡ Real-time Updates & Clean UI  

---

## 📁 Project Structure

```
AIML_Based_Roadmap_Generator_for_Skill_Development/
│
├── 📂 ai_app/                    # Core Django app (views, models, templates)
├── 📂 static/                    # Static assets (CSS, JS, images including logo.jpg)
├── 📂 templates/                 # HTML templates
├── 📂 media/                     # Uploaded files (e.g., payment proofs)
├── ⚙️ manage.py                  # Django management script
├── 📋 requirements.txt           # Python dependencies
└── 📖 README.md                  # Project documentation
```

---

## ⚙️ Technologies Used

### Backend  
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>  
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>

### Frontend  
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>  
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher  
- pip  
- Git  

### Step 1: Clone the Repository
```bash
git clone https://github.com/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development.git
cd AIML_Based_Roadmap_Generator_for_Skill_Development
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

### Step 7: Open Your Browser
Go to `http://127.0.0.1:8000` and explore the app.

---

## 🎯 Usage

- Register or Log in (Free access)  
- Use the Roadmap generator  
- Upload sources & chat with AI  
- Upgrade to Premium for unlimited access  

---

## 🤝 Contributing

We welcome your contributions! Please follow the steps:

1. Fork the repository  
2. Create your feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```  
3. Commit your changes  
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```  
4. Push to the branch  
   ```bash
   git push origin feature/AmazingFeature
   ```  
5. Open a Pull Request  

### Contributors

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/Kowshik-bh18.png" width="100px;" alt="Kowshik BH"/>
        <br />
        <sub><b>Kowshik BH</b></sub>
        <br />
        <a href="https://github.com/Kowshik-bh18">Developer</a>
      </td>
      <td align="center">
        <img src="https://github.com/madhusudhan-31.png" width="100px;" alt="MadhuSudhan"/>
        <br />
        <sub><b>Madhu Sudhan</b></sub>
        <br />
        <a href="https://github.com/madhusudhan-31">Developer</a>
      </td>
      <td align="center">
        <img src="https://github.com/MDGanesha.png" width="100px;" alt="MD Ganesha"/>
        <br />
        <sub><b>MD Ganesha</b></sub>
        <br />
        <a href="https://github.com/MDGanesha">🔧 Developer</a>
      </td>
    </tr>
  </table>
</div>

---

## 🌐 Live Demo

Check it out here: [https://rmpai.pythonanywhere.com/](https://rmpai.pythonanywhere.com/)

---

## 📞 Contact

<div align="center">
  <h3>Get in Touch</h3>
  
  **Kowshik BH**  
  [![Email](https://img.shields.io/badge/Email-kowshibh18@gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kowshibh18@gmail.com)  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kowshikbh)  
  [![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Kowshik-bh18)  
</div>

---

<div align="center">
  <h3>⭐ Star this repository if you found it helpful!</h3>
  <img src="https://img.shields.io/github/stars/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development?style=social" alt="GitHub forks"/>
  <img src="https://img.shields.io/github/watchers/Kowshik-bh18/AIML_Based_Roadmap_Generator_for_Skill_Development?style=social" alt="GitHub watchers"/>
</div>
