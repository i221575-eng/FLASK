pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY  = 'FLASK_i221575'
        SONAR_PROJECT_NAME = 'Lab12'
        NEW_VERSION        = '1.3.0'
        SONAR_HOST_URL     = 'http://192.168.10.1:9005'
    }

    stages {

        stage('Build') {
            steps {
                echo "Building version ${NEW_VERSION}..."
                bat "echo Running Build Step..."
            }
        }

        stage('SonarQube Analysis (Docker)') {
            steps {
                script {
                    echo "Running SonarQube analysis using Dockerized SonarScanner..."

                    // Docker command for SonarScanner
                    bat """
                    docker run --rm ^
                        -e SONAR_HOST_URL=${SONAR_HOST_URL} ^
                        -v "%cd%:/usr/src" ^
                        sonarsource/sonar-scanner-cli ^
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} ^
                        -Dsonar.projectName=${SONAR_PROJECT_NAME} ^
                        -Dsonar.sources=.
                    """
                }
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."
            }
        }
    }

    post {
        always {
            echo "Post build actions..."
        }
        failure {
            echo "Build failed."
        }
    }
}
