
***Explain Like I'm 5 (ELI5) Learning Copilot - MVP***

An AI-powered assistant that explains complex topics in easy language, as if you are 5 years old.  
Frontend is deployed on Vercel, backend on Render, and explanations are generated using OpenAI GPT models.

---

## 🚀 Tech Stack

- **Frontend:** Static HTML, CSS, JavaScript (Vercel)
- **Backend:** FastAPI (Python) (Render)
- **AI Integration:** OpenAI API (GPT)
- **Other Python Packages:** python-dotenv, httpx, beautifulsoup4
- **Deployment:** GitHub, Vercel (Frontend), Render (Backend)
- **CORS:** Enabled for smooth frontend-backend requests

---

## 📁 Project Structure

```
eli5-copilot/
│
├── main.py              # FastAPI backend application
├── ai_client.py         # OpenAI API requests & prompt logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (OPENAI_API_KEY, etc.)
├── .gitignore           # Files and directories ignored by Git
├── README.md            # Project documentation (this file)
│
├── frontend/
│   ├── index.html       # Main HTML file for user interface
│   ├── style.css        # Styling for the frontend
│   └── script.js        # Client-side logic: API calls & interaction
```

---

## 🌐 Live Demo

- Frontend: [https://mvp-project-one.vercel.app](https://mvp-project-one.vercel.app)
- Backend: [https://mvp-project-wop0.onrender.com](https://mvp-project-wop0.onrender.com)

---

