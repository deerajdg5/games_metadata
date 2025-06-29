# Game Metadata Strategist
An AI-assisted, multi-format metadata parsing and normalization tool for games. Designed to help catalog, clean, and structure metadata across platforms — ideal for roles like Game Metadata Strategist at Netflix, Ubisoft, and more.

Overview:
This project is a flexible, Python-based tool that parses, cleans, and normalizes game metadata from various file formats (JSON, CSV, XML, HTML) and APIs. It standardizes fields like genre, platform, developer, and release dates — streamlining ingestion for search, categorization, and compliance across publishing platforms.

Key Features:
- AI Integration (Pluggable with OpenAI/Cohere) for metadata enhancement and tagging
- Multi-format Support: JSON, CSV, XML, HTML parsing
- Smart Field Normalization (e.g., “PS5” → “PlayStation 5”)
- Exports clean structured output as CSV/JSON
- Optional Streamlit UI for real-time metadata preview
- Designed for real-world roles in game metadata ops, publishing, and catalog strategy

Tech Stack
- Python 3.10+
- pandas, bs4, lxml, openai (optional)
- streamlit (for optional UI)
- re, json, os, datetime

Author:
Deeraj Ganesh M
