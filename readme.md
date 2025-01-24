# Activate the virtual environment
source env/bin/activate

# Run the app
uvicorn main:app --reload
 # AI-Powered Career Development API

A FastAPI-based application that provides various career development tools and assessments.
This microservice is designed to be easily integrated with:
- Bubble.io
- Xano
- Supabase

## Features

- LinkedIn Profile Analysis
- Resume Checklist
- Job Suggestions
- Role Labeling
- Strengths Assessment
- Job Description Translation

## Prerequisites

- Python 3.10+
- Poetry or pip for dependency management

## Installation

1. Clone the repository:

## Running the Application

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
