# Production CI/CD Pipeline

An end-to-end CI/CD project for a Flask application. GitHub Actions runs continuous integration on every push, while Jenkins builds the Docker image, runs automated tests, scans code with SonarQube, and deploys the container after the quality gate passes.

## Tools Used

- **GitHub Actions** — continuous integration
- **Jenkins** — continuous delivery pipeline
- **Docker** — application packaging and deployment
- **SonarQube** — code-quality analysis and quality gates
- **Pytest** — automated application testing
- **Git & GitHub** — source control and pipeline trigger

## Pipeline Flow

```text
GitHub Push → GitHub Actions (test + Docker build)
           → Jenkins (build → test → SonarQube scan → deploy)
```

```text
Checkout → Build → Test → Sonar Scan → Deploy
```

## Project Structure

```text
.
├── .github/workflows/ci.yml    # GitHub Actions CI workflow
├── jenkins/Dockerfile          # Jenkins image with Docker CLI
├── app.py                      # Flask application
├── test_app.py                 # Pytest test suite
├── Dockerfile                  # Application container image
├── Jenkinsfile                 # Jenkins pipeline definition
├── docker-compose.yml          # Local Jenkins + SonarQube services
└── requirements.txt            # Python dependencies
```

## Prerequisites

- Docker Desktop running in Linux-container mode
- A GitHub repository whose default branch is `main`

## Run the application locally

```powershell
docker build -t flask-app:local .
docker run --rm -p 5000:5000 flask-app:local
```

Open `http://localhost:5000`.

Expected response:

```text
CI/CD Project Running
```

## Run Tests

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected result: `1 passed`.

## Start Jenkins and SonarQube

```powershell
docker compose up --build -d
```

- Jenkins: `http://localhost:8080`
- SonarQube: `http://localhost:9000`

> Your existing Jenkins container is mapped to `http://localhost:8081`. The Compose setup maps Jenkins to port 8080.

In SonarQube, create a project with key `flask-app`, then generate a user token. In Jenkins, add that value as a **Secret text** credential with ID `sonar-token`.

Create a Jenkins Pipeline job that points at this repository and uses the included `Jenkinsfile`. Install the Docker Pipeline and Pipeline plugins in Jenkins. A successful run builds the image, runs `pytest`, sends the scan to SonarQube, and serves the app on port 5000.

## GitHub Actions

Every push to `main` installs dependencies, executes the test suite, and builds the Docker image. The workflow is in `.github/workflows/ci.yml`.

## Proof of Execution


### Application Running

<img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/2d9c2e90-ebca-429d-9de1-8bcd12884dd4" />


### GitHub Actions CI Success

<img width="1248" height="874" alt="image" src="https://github.com/user-attachments/assets/dd57018d-ac71-4f76-af83-5864aaf18ec1" />

### Jenkins Dashboard

<img width="1256" height="857" alt="image" src="https://github.com/user-attachments/assets/600d62e2-3d23-4208-9f42-e9a8820f1609" />


### Jenkins Pipeline Success

<img width="1264" height="862" alt="image" src="https://github.com/user-attachments/assets/4dbef58f-ee72-4579-9eed-352d6e3480ec" />


### SonarQube Quality Dashboard

<img width="1260" height="862" alt="image" src="https://github.com/user-attachments/assets/ad76de91-7827-42a1-b59b-f9060e7d1b5f" />


### SonarQube Analysis Activity

<img width="1259" height="857" alt="image" src="https://github.com/user-attachments/assets/a26f5a94-7e0d-4019-9c58-a69e86ae9b93" />


## Stop local services

```powershell
docker compose down
```

## Author

TriptiP-Code
