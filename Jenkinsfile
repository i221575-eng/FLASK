pipeline {
    agent any

    stages {
        // The 'Checkout' stage is usually automatic, but kept here if you prefer manual control
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/i221575-eng/FLASK.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python --version
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Ensure pytest is installed in your requirements.txt
                bat 'pytest'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                    if not exist "C:\\flask_app" mkdir "C:\\flask_app"
                    xcopy /E /I /Y * "C:\\flask_app\\"
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
            echo 'Pipeline failed! Check the console output for errors.'
        }
    }
}
