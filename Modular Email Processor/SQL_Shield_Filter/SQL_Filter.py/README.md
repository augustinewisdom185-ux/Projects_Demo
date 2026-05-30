# SQLi Shield Filter 🛡️🐍

A lightweight, rule-based security filter designed to detect and block basic SQL Injection (SQLi) payloads hidden inside user input datasets.

## 🔍 Overview

When software applications accept user inputs—such as a list of emails—without checking them first, malicious actors can insert harmful database commands. This is known as a **SQL Injection** attack. 

This Python script simulates an inline input scanner. It iterates through a incoming dataset, sanitizes potential payload keywords, and flags unauthorized database control characters (like the SQL statement terminator `;`) before they can reach a backend database server.

---

## 🛠️ System Architecture & Logic

The security filter processes data through three distinct defensive logical steps:

1. **Input Ingestion:** Accepts an array of text inputs (e.g., email strings).
2. **Payload Neutralization & Normalization:** It uses `.replace('DROP TABLE USERS', 'wisdom@gmail.com')` to strip out dangerous commands, swapping a known threat vector with a safe, standardized mock address.
3. **Signature Analysis:** It scans the normalized text for the `;` character. In SQL databases, a semicolon tells the system to run a brand-new command immediately. Finding one in an email field triggers an instant security alert, isolates the payload, and skips processing.

---

## 🚀 Key Learning Takeaways
​Input Validation & Sanitization: Practiced implementing security constraints directly into data loops to ensure input hygiene.
​Cybersecurity Awareness: Explored how database management languages (SQL) can be exploited via unchecked text forms, a critical concept when designing backend APIs or handling data science storage layers.
​Defensive Coding: Leveraged basic pattern recognition loops (if ';' in email) to act as a preventative software firewall layer.
