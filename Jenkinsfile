pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                // 1. Pull code from GitHub
                git url: 'https://github.com/i221575-eng/FLASK.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // 2. Install Python dependencies for Flask
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // 3. Run unit tests using pytest
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
