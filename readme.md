# BuxLLM Personalization Service

A FastAPI-based microservice that provides personalized job recommendations and career insights using LLM technology. This service integrates with Fireworks AI to provide intelligent job suggestions, resume analysis, and LinkedIn profile optimization.

## Features

- **Job Title Suggestions**: Generate relevant job titles based on user profiles
- **Resume Analysis**: Provide checklist and improvements for resumes
- **LinkedIn Profile Optimization**: Analyze and enhance LinkedIn profiles
- **Role Labeling**: Analyze professional profiles for role categorization
- **Strength Analysis**: Identify and analyze professional strengths
- **Job Translation**: Convert job requirements into actionable job search queries

## Technology Stack

- **Framework**: FastAPI
- **LLM Integration**: Fireworks AI (llama-v3-70b-instruct)
- **Logging**: Logfire
- **Type Safety**: Pydantic
- **Development**: Poetry for dependency management

## Getting Started

### Prerequisites

- Python 3.8+
- Poetry (Python package manager)
- Fireworks AI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/micah-sircularity/bux-microservice.git
   cd bux-microservice
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

   Alternatively, you can use pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Fireworks AI API key:
   ```
   FIREWORKS_API_KEY=your_api_key_here
   PORT=5000
   ```

### Running the Service

Start the service using uvicorn:
```bash
poetry run python main.py
```

Or directly with uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /`: API root endpoint
- `POST /api/job-titles`: Generate job title suggestions
- `POST /api/analyze-profile`: Analyze professional profiles
- `POST /api/create-jobs-list`: Create job search queries
- `POST /api/check-resume`: Analyze resume content
- `POST /api/check-linkedin`: Analyze LinkedIn profile
- `POST /api/strengths`: Analyze professional strengths

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Style
The project follows PEP 8 guidelines and uses type hints throughout the codebase.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is proprietary and confidential. All rights reserved.

## Contact

Micah - [@micah-sircularity](https://github.com/micah-sircularity)