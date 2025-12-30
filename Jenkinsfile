pipeline {
    agent any

    stages {

        // 1️⃣ Checkout code
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/i221575-eng/FLASK.git', branch: 'main'
            }
        }

        // 2️⃣ Install dependencies from requirements.txt
        stage('Install Dependencies') {
            steps {
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requierments.txt
                '''
            }
        }

        // 3️⃣ Run unit tests using pytest
        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }

        // 4️⃣ Simulate deployment by copying files
        stage('Deploy Application') {
            steps {
                sh '''
                    mkdir -p /opt/flask_app
                    cp -r * /opt/flask_app/
                    echo "Files copied to /opt/flask_app - Deployment simulated"
                '''
            }
        }

        // 5️⃣ Simulate restart of the application
        stage('Restart Application') {
            steps {
                sh 'echo "Simulating Flask app restart..."'
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
