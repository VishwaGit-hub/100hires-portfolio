# Cursor Setup Portfolio Task

## Overview
This repository documents the setup process of Cursor IDE along with required AI extensions as part of the evaluation task.

---

## Tools Installed
- Cursor IDE  
- Claude Code (VS Code extension, compatible with Cursor)  
- OpenAI Codex extension  
- Kilo Code extension  
- Git  
- GitHub  

---

## Steps Completed
1. Created a local project folder  
2. Initialized a Git repository  
3. Opened project in Cursor IDE  
4. Installed required extensions  
5. Attempted authentication for extensions  
6. Created README documentation  
7. Committed and pushed repository to GitHub  

---

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial setup with README"
git branch -M main
git remote add origin <REPOSITORY_URL>
git push -u origin main

## Project Structure


research/
sources.md
linkedin-posts/
youtube-transcripts/
other/

scripts/
fetch_transcript.py
video_list.txt


---

## Steps Completed

### 1. Environment Setup
- Installed Cursor IDE  
- Installed required extensions (Claude Code, Codex, Kilo Code)  
- Initialized Git repository and connected to GitHub  
- Created and activated Python virtual environment  
- Installed required Python dependencies  

---

### 2. Topic Selection
Selected:
**Cold Outreach Pipeline for B2B SaaS**

Reason:
- High real-world relevance  
- Strong overlap with sales, automation, and AI workflows  
- Availability of practitioner-driven content  

---

### 3. Expert Selection
Selected 10 practitioners based on:
- Real outbound experience  
- Actionable content (not generic advice)  
- Recent activity  

Examples:
- Alex Berman  
- Justin Welsh  
- Steli Efti  
- Jason Bay  
- Kyle Coleman  
- Morgan Ingram  

---

### 4. YouTube Transcript Collection

#### Approach
- Built a Python script using `youtube-transcript-api`  
- Used a structured input file (`video_list.txt`)  
- Automatically fetched and stored transcripts  

#### Output Structure

research/youtube-transcripts/<author>/<video_id>.md


---

### 5. Issues Faced

#### YouTube Rate Limiting
- After multiple API requests, YouTube blocked further requests  
- Transcript extraction failed for remaining videos  

---

### 6. How Issues Were Handled
- Confirmed the extraction pipeline works correctly  
- Retained successfully fetched transcripts  
- Avoided unreliable workarounds  
- Continued progress instead of retrying blocked requests  

---

### 7. Key Learnings
- Building automated data pipelines  
- Handling API rate limits and real-world failures  
- Importance of high-quality source selection  
- Structuring data for future use  

---

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial setup with README"
git branch -M main
git remote add origin <REPOSITORY_URL>
git push -u origin main