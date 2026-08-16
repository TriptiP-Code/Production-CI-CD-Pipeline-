# Production CI/CD Pipeline

This project runs a small Flask application through GitHub Actions for CI and Jenkins for build, test, SonarQube analysis, and deployment.

## Prerequisites

- Docker Desktop running in Linux-container mode
- A GitHub repository whose default branch is `main`

## Run the application locally

```powershell
docker build -t flask-app:local .
docker run --rm -p 5000:5000 flask-app:local
```

Open `http://localhost:5000`.

## Start Jenkins and SonarQube

```powershell
docker compose up --build -d
```

- Jenkins: `http://localhost:8080`
- SonarQube: `http://localhost:9000`

In SonarQube, create a project with key `flask-app`, then generate a user token. In Jenkins, add that value as a **Secret text** credential with ID `sonar-token`.

Create a Jenkins Pipeline job that points at this repository and uses the included `Jenkinsfile`. Install the Docker Pipeline and Pipeline plugins in Jenkins. A successful run builds the image, runs `pytest`, sends the scan to SonarQube, and serves the app on port 5000.

## GitHub Actions

Every push to `main` installs dependencies, executes the test suite, and builds the Docker image. The workflow is in `.github/workflows/ci.yml`.

## Stop local services

```powershell
docker compose down
```
