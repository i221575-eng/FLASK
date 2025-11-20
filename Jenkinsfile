pipeline {
    agent any

    environment {
        // SonarQube Server Name (Must match 'Manage Jenkins -> System -> SonarQube servers')
        SONAR_SERVER_NAME = 'SonarQube Server'

        // SonarQube Project Details
        SONAR_PROJECT_KEY  = 'FLASK_i221575'
        SONAR_PROJECT_NAME = 'Lab12'

        // Version tag
        NEW_VERSION = '1.3.0'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version ${NEW_VERSION} on Windows..."
                bat 'echo Running Build Step...'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // 1. Get the path to the scanner tool configured in Jenkins
                    // The name 'sonar_scanner' must match exactly what you entered in 'Global Tool Configuration'
                    def scannerHome = tool 'sonar-scanner'
                    
                    // 2. Use the withSonarQubeEnv wrapper to inject tokens/URL
                    withSonarQubeEnv(SONAR_SERVER_NAME) {
                        echo "Starting SonarQube Analysis for project ${env.SONAR_PROJECT_NAME}..."
                        echo "Using Scanner at: ${scannerHome}"
                        
                        // 3. Run the scanner using the retrieved path
                        bat "\"${scannerHome}\\bin\\sonar-scanner\" " + 
                            "-Dsonar.projectKey=${SONAR_PROJECT_KEY} " + 
                            "-Dsonar.projectName=\"${SONAR_PROJECT_NAME}\" " + 
                            "-Dsonar.sources=." 
                    }
                }
            }
        }

        stage('Quality Gate Check') {
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    script {
                        // Wait for SonarQube to finish processing the report
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
                echo 'Testing Project...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    
    post { 
        always {
            echo 'Post build condition running'    
        }
        failure {
            echo 'Post action if build failed'    
        }
    }
}
