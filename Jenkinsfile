pipeline {
    agent any

    environment {
        // Python environment (adjust if using a virtualenv)
        PYTHON = "python3"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub
                git branch: 'main', url: 'https://github.com/i221575-eng/FLASK.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh "${env.PYTHON} -m pip install --upgrade pip"
                sh "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python tests (if using pytest)
                sh "${env.PYTHON} -m pytest tests"
            }
        }

        stage('Build & Deploy') {
            steps {
                // Run the Flask app (basic example)
                sh "${env.PYTHON} app.py"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build and deployment succeeded!'
        }
        failure {
            echo 'Build or tests failed.'
        }
    }
}
