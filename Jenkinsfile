pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/i221575-eng/FLASK.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requierments.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                    mkdir C:\\flask_app
                    xcopy /E /I * C:\\flask_app\\
                    echo "Files copied to C:\\flask_app - Deployment simulated"
                '''
            }
        }

        stage('Restart Application') {
            steps {
                bat 'echo Simulating Flask app restart...'
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
