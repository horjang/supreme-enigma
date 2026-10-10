# Activity 12 — Streamlit Web Apps

> **🛠️ Stack for this lesson** — Python / Streamlit · runs on your own computer (a Streamlit app opens in a browser tab; Colab can only show it through a tunnel).
> 📥 Template: [/learn/ai2/template/activity-12-streamlit](/learn/ai2/template/activity-12-streamlit)

This folder holds two ways to practise. The **numbered scripts** are the main path: five small apps that add one widget each, ending with a chatbot page. The **optional notebook** adds three more apps that you write from inside Jupyter with `%%writefile`. In both you write the Streamlit code; the folder supplies the file shells, the finished chatbot model (`chatbot.py` with `intents.json`, from Project 04) and the install list.

**Time:** ~100 minutes (core path ~40) · **Concept:** Concept 12 — Streamlit

---

## What You'll Build

**Main path: the numbered scripts** (one TODO per file; `1-Setup.py` already runs):

| File | TODO | What the app does when you finish |
|------|------|-----------------------------------|
| `2-Question1.py` | 1 | A page with a title, a header, plain text and a blue line made with markdown |
| `3-Question2.py` | 2 | A "Say Hello" button: "Goodbye" until it is clicked, "Hello" after |
| `4-Question3.py` | 3 | A form (name, age, address, gender, camera photo, agreement tick) that prints a personal thank-you on submit |
| `5-Question4.py` | 4 | A sidebar selectbox that switches the page between "Home" and "About me" |
| `6-Advanced1-Chatbot.py` | 5 | A two-page app (Home with a video, Chatbot) that sends your text to `chatbot.py` and shows a spinner while the bot replies |

**Optional extra: `activity-12-streamlit.ipynb`** (its TODOs are numbered 1 to 3 inside the notebook, separate from the script TODOs above). Each one writes its own `.py` file:

| Notebook TODO | Writes | What the app does |
|---------------|--------|-------------------|
| 1 | `todo1_my_hobby.py` | A page about your own hobby: emoji title, "Why I Love It" header, a description and a coloured quote |
| 2 | `todo2_quiz_app.py` | A one-question quiz with answer choices and a "Check Answer" button that says right or wrong |
| 3 | `todo3_portfolio.py` | A three-page portfolio (Home, Projects, Contact) with a contact form |

Read each file, work out what the TODO asks for, and write it. The finished versions are tutor-only.

## Run It

```bash
pip install -r requirements.txt
streamlit run 1-Setup.py        # prints your package versions
streamlit run 2-Question1.py    # then 3-Question2.py, and so on
```

Streamlit opens `http://localhost:8501`. Every time you save, the page offers a rerun, so keep the browser beside your editor. Stop an app with Ctrl+C in the terminal.

`requirements.txt` pins versions from 2022 to 2023, and some have no build for a recent Python (`numpy==1.24.1` has none for Python 3.13). If `pip` fails on a pin, install the packages without pins instead: `pip install streamlit pandas numpy scikit-learn nltk`. The chatbot page downloads NLTK's tokeniser data the first time it runs, so it needs an internet connection once; on macOS, if that fails with a certificate error, run the `Install Certificates.command` file that came with your Python.

The notebook runs in local Jupyter or VS Code. Its first cell installs Streamlit; then run each `%%writefile` cell and start the file it wrote with `streamlit run <file>.py` in a terminal.

## Verify

Your activity is done when:

- [ ] `streamlit run 1-Setup.py` prints the package versions with no `ModuleNotFoundError`.
- [ ] `2-Question1.py` shows a title, a header, plain text and a blue line, not raw markdown symbols.
- [ ] `3-Question2.py` shows "Goodbye" at first and "Hello" after the button is clicked.
- [ ] `4-Question3.py` collects every field and prints a thank-you that includes your name, age, address and gender.
- [ ] `5-Question4.py` changes the page content when you pick the other sidebar option.
- [ ] `6-Advanced1-Chatbot.py` loads the model, accepts your text and shows a bot reply with a spinner while it waits.
- [ ] If you did the notebook, each `todo*.py` file runs and does what its table row says.

## Stretch

Pick one and note what you tried in your Notes doc:
- Keep the form entries from `4-Question3.py` alive across reruns, without a global variable.
- Show a table of how many example sentences each chatbot intent has, on the Home page.
- On the chatbot page, show the intent the model picked beside each reply.

## 🪞 Reflect on Your Work

Answer in 2-3 sentences each, in your Notes doc. Your tutor reads these as part of grading.

1. **What did you learn that you didn't know before?** Name the most surprising thing, such as the way Streamlit reruns the whole script on every click.
2. **How did you collaborate with AI?** If you used Claude / ChatGPT / Cursor / Copilot, what part of the work did *you* contribute — the prompt, the verification, the design decision, the bug-fix? If you didn't use AI, what was the hardest thing to figure out alone?
3. **How do you know your code works?** Describe one specific thing you did to confirm it, such as the button test "I clicked ___ and saw ___", a screenshot of the running app, or a message you read in the terminal.

> AI is a great collaborator. Owning your thinking, verifying the output, and explaining your design choices is what *learning* looks like in this course.

## Submit

When the Verify checklist is green, add two screenshots of your running apps to your Notes doc, submit the link to your Notes doc, then Mark as Complete.

<!-- claude-template-fix: readme-v3 -->
