pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
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
                        docker run --rm \
                            --network jenkins \
                            -e SONAR_HOST_URL=http://sonarqube:9000 \
                            -e SONAR_TOKEN=$SONAR_TOKEN \
                            -v "$WORKSPACE:/usr/src" \
                            sonarsource/sonar-scanner-cli
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true

                    docker run -d \
                        --name flask-app \
                        -p 5000:5000 \
                        flask-app
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
    }
}