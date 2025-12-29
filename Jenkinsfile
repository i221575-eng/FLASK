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
                echo "Building version ${NEW_VERSION} on Windows..."
                bat "echo Running Build Step..."
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    echo "Running SonarQube analysis using Docker scanner..."
                    
                    // Use Docker SonarScanner image
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

        stage('Quality Gate Check') {
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    script {
                        // Wait for Quality Gate via SonarQube plugin
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline failed due to SonarQube Quality Gate: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo "Testing Project..."
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
            echo "Post build action running..."
        }
        failure {
            echo "Build failed."
        }
    }
}
