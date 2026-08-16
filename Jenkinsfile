pipeline {

    agent any

    environment {
        IMAGE_NAME = "flask-app"
        CONTAINER_NAME = "flask-app"

        SONAR_HOST_URL = "http://sonarqube:9000"
        SONAR_PROJECT_KEY = "flask-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Building Docker image..."

                    docker build \
                        -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                        -t ${IMAGE_NAME}:latest \
                        .

                    echo "Docker image built successfully"
                    docker images ${IMAGE_NAME}
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Running automated tests..."
                    docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} pytest -q
                '''
            }
        }

        stage('Sonar Scan') {
            steps {

                withCredentials([
                    string(
                        credentialsId: 'sonar-token',
                        variable: 'SONAR_TOKEN'
                    )
                ]) {

                    sh '''
                        echo "Starting SonarQube scan..."

                        docker run --rm \
                            --network host \
                            -e SONAR_HOST_URL=${SONAR_HOST_URL} \
                            -e SONAR_TOKEN=${SONAR_TOKEN} \
                            -v "${WORKSPACE}:/usr/src" \
                            sonarsource/sonar-scanner-cli:latest \
                            sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.sources=/usr/src \
                            -Dsonar.host.url=${SONAR_HOST_URL} \
                            -Dsonar.token=${SONAR_TOKEN} \
                            -Dsonar.qualitygate.wait=true

                        echo "SonarQube scan completed"
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploying application..."

                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 5000:5000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}

                    echo "Container started"

                    for attempt in 1 2 3 4 5; do
                        if docker inspect --format='{{.State.Health.Status}}' ${CONTAINER_NAME} | grep -q healthy; then
                            echo "Application is healthy"
                            exit 0
                        fi
                        sleep 3
                    done

                    docker logs ${CONTAINER_NAME} --tail 50
                    echo "Application did not become healthy"
                    exit 1
                '''
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
