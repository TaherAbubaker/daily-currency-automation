# 💱 Currency Rate Agent — USD to JOD & NIS

An AI agent that fetches live exchange rates daily and logs them to an Excel sheet automatically.

---

## 📁 Files
| File | Purpose |
|---|---|
| `currency_agent.py` | The agent — fetches rates & writes to Excel |
| `scheduler.py` | Keeps it running and triggers at 08:00 daily |
| `currency_rates.xlsx` | The output Excel (auto-created on first run) |

---

## ⚡ Quick Start

### 1. Install dependencies
```bash
pip install requests openpyxl schedule
```

### 2. Run manually (test it)
```bash
python currency_agent.py
```

### 3. Run on schedule (Option A — Python scheduler)
```bash
python scheduler.py
```
Leave this terminal open. It runs forever and fetches at 8am each day.

---

## ⏰ Better Option: System Scheduler (runs even if terminal is closed)

### Windows — Task Scheduler
1. Open **Task Scheduler** → Create Basic Task
2. Trigger: **Daily at 08:00**
3. Action: **Start a program**
   - Program: `python`
   - Arguments: `C:\path\to\currency_agent.py`
4. Save ✅

### Linux/Mac — Cron
```bash
crontab -e
```
Add this line:
```
0 8 * * * /usr/bin/python3 /full/path/to/currency_agent.py
```

---

## 📊 Excel Output Format

| Date | Day | USD → JOD | USD → NIS (ILS) | Note |
|---|---|---|---|---|
| 2026-05-06 | Wednesday | 0.7090 | 3.6821 | |
| 2026-05-07 | Thursday | 0.7090 | 3.6954 | |

- **Rows auto-append** — never overwrites existing data
- **Duplicate-safe** — won't add the same date twice
- **Alternating row colors** for readability
- **Auto-filter** on headers

---

## 🌐 Data Source
Uses the free **Fawaz Ahmed Currency API** (no API key needed):
- `https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json`
- Falls back to: `https://latest.currency-api.pages.dev/v1/currencies/usd.json`

---

## 🧠 How it works (for the professor)
1. Agent fetches live JSON data from a free currency API
2. Parses JOD and ILS (NIS) rates for 1 USD
3. Checks if today's row already exists in the Excel file
4. If not → appends a new formatted row with date, day name, and rates
5. The scheduler triggers this at 08:00 every day automatically


## How to make it fully automated and work by it self
   Windows Task Scheduler ✅ (recommended, no terminal needed ever again)
   This is the proper way. Windows itself will wake up at 8am and run currency_agent.py directly, even if VS Code is closed, even if you're sleeping.
   Search "Task Scheduler" in Windows start menu
   Click "Create Basic Task"
   Name it: Currency Agent
   Trigger: Daily → set time to 8:00 AM
   Action: Start a program
   Program/script: python
   Add arguments: C:\full\path\to\currency_agent.py
   Finish ✅