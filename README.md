# The Master PYQ Maker
### For lazy but ambitious engineers. 😸
> Automatically download and merge RGPV Previous Year Question Papers into one clean PDF.

<img width="360" height="480" alt="LonelyGirlDanceGIF" src="https://github.com/user-attachments/assets/0c85aacd-973d-4a83-848f-b1b41d63ec8a" />

---

## Features

- Search papers by branch, semester, and subject
- Automatically download matching PYQs
- Merge all papers into one Master PDF
- Automatically clean temporary downloaded files
- Simple terminal interface
- Written completely in Python

---

## Why tho??
<img width="476" height="480" alt="ConfusedAnimationGIFbyKETNIPZ" src="https://github.com/user-attachments/assets/bbd6b243-0124-481d-8cb6-2fba0221f4a1" />

Cuz I got tired of downloading every PYQ manually before exams 😐

Instead of:

Website → Click → New tab → Download → Repeat 20 times

I wanted:

Run script → Enter subject → Done.

So... I automated my laziness.

---

## 🛠 Requirements

- Python 3.10+
- requests
- beautifulsoup4
- pypdf

Install dependencies:

```bash
pip install requests beautifulsoup4 pypdf
```

---

## How to use?

1. Clone this repository

```bash
git clone <repo-url>
```

2. Run the script

```bash
python main.py
```

3. Select:

- Branch
- Semester
- Subject

4. Wait for the download to finish.

5. Your merged PDF will appear in the project folder.

Time to study. (You no longer have the excuse of "collecting PYQs." 😼)

---

## Output

Example:

```
Control_Systems_Master_PYQ.pdf
```

---

## ⚠ Notes

- Works with the current structure of the RGPV Online website.
- If the website changes, the scraper may need to be updated.
- Currently downloads papers from 2022-2025.

---

## 💡 Future ideas

Contributions are welcome!

<img width="320" height="180" alt="Suggestion" src="https://github.com/user-attachments/assets/91ab042c-7d44-47c1-bcb9-b86e0b9ae70b" />

Some ideas:

- GUI version
- Progress bar
- Download older papers
- Better error handling
- Automatic bookmarks
- Topic-wise paper analysis
- Config file
- Smarter subject search

Feel free to open an Issue or submit a Pull Request.

I made the base...

Now build the skyscraper. 🏙️
