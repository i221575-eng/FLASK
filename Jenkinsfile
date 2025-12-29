pipeline {
    agent any

    environment {
        // SonarQube server name from "Manage Jenkins → System → SonarQube Servers"
        SONAR_SERVER_NAME = 'SonarQube'
        // SonarQube Project Info
        SONAR_PROJECT_KEY  = 'FLASK_i221575'
        SONAR_PROJECT_NAME = 'Lab12'
        // Version tag
        NEW_VERSION = '1.3.0'
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
                    // Must match the name defined in Global Tool Configuration
                    def scannerHome = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    
                    withSonarQubeEnv(SONAR_SERVER_NAME) {
                        echo "Starting SonarQube Analysis for ${SONAR_PROJECT_NAME}..."
                        bat """
                            "${scannerHome}\\bin\\sonar-scanner.bat" ^
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} ^
                            -Dsonar.projectName=${SONAR_PROJECT_NAME} ^
                            -Dsonar.sources=.
                        """
                    }
                }
            }
        }

        stage('Quality Gate Check') {
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline failed due to SonarQube Quality Gate failure: ${qg.status}"
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
