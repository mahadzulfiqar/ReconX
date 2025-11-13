# Contributing to ReconX

Thank you for your interest in contributing! 🎉  
ReconX is an open-source project focused on cybersecurity education and ethical reconnaissance automation.

We welcome contributions that improve code quality, add new features, or enhance documentation.

---

## 🧠 Code of Conduct
- Be respectful and professional.  
- Avoid toxic language or behavior.  
- Encourage learning and collaboration.

---

## 🛠 Prerequisites
- Python 3.10 or above  
- `pip`, `git`, and a GitHub account  
- Basic familiarity with Git branching and pull requests  

---

## 🧰 Code Style
- Follow **PEP8** standards.  
- Use **flake8** or **black** for formatting.  
- Keep functions small, readable, and well-commented.  
- Use **meaningful commit messages** (e.g., `fix:`, `feat:`, `docs:`).

**Example:**
```bash
git commit -m "feat: add threaded TCP port scanner module"
🔍 How to Contribute
1. Fork the repository
Click “Fork” at the top-right of the repo.

2. Clone your fork locally
bash
Copy code
git clone https://github.com/<your-username>/ReconX.git
cd ReconX
3. Create a feature branch
bash
Copy code
git checkout -b feature/<feature-name>
4. Set up your environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements-dev.txt
5. Run linters and tests
bash
Copy code
flake8 .
pytest
6. Commit and push changes
bash
Copy code
git add .
git commit -m "feat: added new recon module"
git push origin feature/<feature-name>
7. Create a Pull Request (PR)
Go to GitHub and click “Compare & pull request”.

Add a clear title and description.

Attach sample output or screenshots.

⚠️ Responsible Disclosure
ReconX is for educational use and authorized security testing only.

Do NOT use it on systems without explicit permission.

If you find a bug or potential vulnerability in ReconX itself, please report it privately via email:
📧 mahadzulfiqar2@gmail.com

🧾 Example Areas to Contribute
New passive/active reconnaissance modules

Code optimization or multithreading improvements

Report generation (JSON/HTML)

Documentation or example scripts

Unit tests (pytest)

Docker and CI enhancements

❤️ Thank You!
Your contributions help make ReconX a professional open-source tool for learners and ethical hackers around the world.

yaml
Copy code
