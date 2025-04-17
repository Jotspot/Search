# Untitled Search Engine

This is a small, experimental search engine — currently unnamed, slow, and barely functional. It uses a basic FastAPI backend and a local SQLite database.

Feel free to explore it, tweak it, or laugh at its current performance. Improvements are welcome!

---

## 🖼️ Preview

<!-- Add a screenshot of the homepage UI -->
[![31K1YEN.md.jpg](https://iili.io/31K1YEN.md.jpg)](https://freeimage.host/i/31K1YEN)

<!-- Add a second image, e.g., search result view -->
[![31K17Bp.md.jpg](https://iili.io/31K17Bp.md.jpg)](https://freeimage.host/i/31K17Bp)
---

## ⚙️ How to Run `app.py`

Follow these steps to run the app using Uvicorn.

### 1. Install Dependencies

Make sure Python is installed. Then install Uvicorn:

**macOS/Linux:**

```bash
pip3 install uvicorn
```

**Windows:**

```bash
pip install uvicorn
```

---

### 2. Run the Application

**macOS/Linux:**

```bash
python3 -m uvicorn app:app --reload
```

**Windows:**

```bash
python -m uvicorn app:app --reload
```

---

### 3. Open in Your Browser

Go to:

```
http://127.0.0.1:8000
```

The `--reload` flag enables hot reloading when code changes.

---

## 📦 Database: `papers.db.zip`

The search index is stored in a large SQLite database named `papers.db.`

The compressed file `papers.db.zip` is included in this repository.
To run the app:
1. Unzip `papers.db.zip`
2. Place the extracted `papers.db` file in the root folder of the project (next to `app.py`)
