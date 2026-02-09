Project Synopsis: Hybrid Disease Prediction & Decision Support System

1. Project Overview

This project aims to build a smart healthcare diagnostic tool that uses a Hybrid AI approach. It combines traditional Machine Learning (ML) for high-accuracy disease classification with a Large Language Model (LLM) for personalized medical guidance. A unique feature of this project is the integration of Psychological Screening to distinguish between actual physiological symptoms and anxiety-driven somatic concerns.

2. Problem Statement

Many online symptom checkers either provide too many scary possibilities (leading to "Cyberchondria") or fail to provide actionable next steps (like nearby hospitals). This system solves this by:

Using ML for "Major Diseases" only when confidence is high.

Using LLM for "Simple Diseases" or general advice.

Filtering predictions based on the user's mental state (Anxiety/Stress).

Mapping results to local hospitals.

3. The 4-Condition Logic (The "Brain" of the App)

The system evaluates ML_Confidence (threshold 70%) and Anxiety_Score.

Scenario A (High Confidence): Display predicted disease + specific hospital list.

Scenario B (Low Confidence + High Anxiety): Suppress disease output; suggest stress management and general wellness.

Scenario C (Low Confidence + Low Anxiety): Trigger LLM to provide general health precautions.

Scenario D (Uncertainty/Close Scores): Inform the user that symptoms are ambiguous and suggest clinical testing.

4. Team Division (5 Members)

Role

Responsibilities

AI/ML Lead

Train Disease Model (Random Forest/XGBoost) & LLM API Integration (Gemini).

Backend Dev

API Development (Flask/FastAPI), Logic for 4-conditions, & Database (Hospitals).

Frontend Dev

UI/UX Design, Form validation, Responsive Dashboard, & Result Visualization.

Data Engineer

Data Cleaning (Kaggle Datasets), Psychology Scoring Logic, & Hospital CSV Mapping.

Documentarian

Research Paper, Synopsis, PPT, Software Requirement Specification (SRS).

5. Tech Stack

Frontend: React.js / HTML5 / Tailwind CSS

Backend: Python (Flask/Django)

AI/ML: Scikit-learn, Google Gemini API (LLM)

Database: Firestore (for persistence) or Local JSON (for Hospitals)