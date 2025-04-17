# How to Run `app,py`

Follow these steps to run the `app.py` file using Uvicorn. Instructions are provided for macOS, Windows, and Linux.

## 1. Install Dependencies  
Ensure you have Python installed. Install Uvicorn by running the following command in your terminal or command prompt:

### macOS/Linux:
```bash
pip3 install uvicorn
```

### Windows:
```bash
pip install uvicorn
```

## 2. Run the Application  
Use the following command to start the application:

### macOS/Linux:
```bash
python3 -m uvicorn app:app --reload
```

### Windows:
```bash
python -m uvicorn app:app --reload
```

## 3. Access the Application  
Open your web browser and navigate to:
```
http://127.0.0.1:8000
```

## 4. Development Mode  
The `--reload` flag enables automatic reloading when code changes are detected.
