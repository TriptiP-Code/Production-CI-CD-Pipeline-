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

Add your screenshot files to the `screenshots` folder with these names.

### Application Running

<img width="1248" height="874" alt="image" src="https://github.com/user-attachments/assets/dd57018d-ac71-4f76-af83-5864aaf18ec1" />


### GitHub Actions CI Success

<img width="1243" height="853" alt="image" src="https://github.com/user-attachments/assets/d6e9c7be-d033-46c0-9149-548db44d1cdd" />


### Jenkins Dashboard

![Uploading image.png…]()


### Jenkins Pipeline Success

![Jenkins pipeline success](screenshots/jenkins-pipeline-success.png)

### SonarQube Quality Dashboard

![SonarQube overview](screenshots/sonarqube-overview.png)

### SonarQube Analysis Activity

![SonarQube analysis activity](screenshots/sonarqube-activity.png)

## Stop local services

```powershell
docker compose down
```

## Author

TriptiP-Code
