pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/TriptiP-Code/Production-CI-CD-Pipeline-'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Sonar Scan') {
            steps {
                sh '''
                sonar-scanner \
                -Dsonar.projectKey=flask-app \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://localhost:9000 \
                -Dsonar.login=squ_fdef76eff0c0eeec6d54020803c88489d93da954
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true

                docker run -d \
                --name flask-container \
                -p 5000:5000 \
                flask-app
                '''
            }
        }
    }
}