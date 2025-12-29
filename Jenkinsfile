pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the latest code from GitHub or your source control
                git url: 'https://github.com/i221575-eng/FLASK.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Compile the application or build the Docker image
                sh 'mvn clean install' // or docker build
            }
        }


        stage('Dependency Check') {
            steps {
                // Run OWASP Dependency-Check to scan for vulnerabilities in third-party libraries
                script {
                    sh 'dependency-check --project MyProject --scan ./ --format HTML --out dependency-check-report.html'
                }
            }
        }


        stage('Unit Tests') {
            steps {
                // Run unit tests to ensure functionality
                sh 'mvn test'
            }
        }

        stage('Deploy to Staging') {
            steps {
                // Deploy the application to the staging environment
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }

        stage('Security Gate') {
            steps {
                // If security checks fail, abort the pipeline
                script {
                    def hasVulnerabilities = readFile('dependency-check-report.html').contains('High')
                    if (hasVulnerabilities) {
                        error "Security vulnerabilities found. Aborting the pipeline!"
                    }
                }
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                // Deploy to production if the branch is 'main' and security checks passed
                sh 'kubectl apply -f k8s-prod-deployment.yaml'
            }
        }
    }

    post {
        always {
            // Archive the security reports regardless of the pipeline result
            archiveArtifacts artifacts: 'dependency-check-report.html, sonar-report.html', allowEmptyArchive: true
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
