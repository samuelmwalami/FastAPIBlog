# FastAPIBlog
## Swagger UI link for the blog API Documentatiotion
[FastAPI Blog API Docs](https://fastapiblog-mt0i.onrender.com/docs)

## How to run the code in your local environment

1. Clone the repository to your local machine from your terminal.
 - ```git clone https://github.com/samuelmwalami/FastAPIBlog.git```

2. Navigate to FastAPIBlog directory
 - ```cd FastAPIBlog```
3. Create a virtual environment for the project.
 - ```python -m venv blogapi```

4. Activate your virtual environment.
On linux/macos:
 - ```source blogapi/bin/activate```
on windows:
 - ```blogapi\Scripts\activate```

5. Install all the project dependencies.
 - ```pip install -r requirements.txt```

6. Create a .env file with the following fields.
```
DATABASE_URL = "your-db url"
JWT_ALGORITHM = "HS256"
JWT_SECRET = "your_secret"
```

7. Run the main.py file.
 - ```uvicorn app.main:app --reload --host 0.0.0.0 --port 8000```

8. Voila, your project is live. Open http://127.0.0.1:8000/docs#/ to view swagger UI docs.