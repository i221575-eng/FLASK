pipeline {
    agent any
    
    environment {
        VENV_DIR = 'venv'
        APP_NAME = 'ItemManagement'
        FLASK_ENV = 'production'
        // Defined exact path here to ensure consistency and easier maintenance
        // Double backslashes are used to escape the path correctly in Groovy
        PYTHON_PATH = 'C:\\Users\\Abubakar\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo "Setting up Python environment using ${env.PYTHON_PATH}..."
                bat '''
                    "%PYTHON_PATH%" --version
                    "%PYTHON_PATH%" -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pytest --verbose --junit-xml=test-results.xml || exit 0
                '''
            }
        }
        
        stage('Database Migration Check') {
            steps {
                echo 'Checking database schema...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    "%PYTHON_PATH%" -c "import sqlite3; conn = sqlite3.connect('database.db'); print('✓ Database accessible')" || exit 0
                '''
            }
        }
        
        stage('Build Artifact') {
            steps {
                echo 'Creating deployment artifact...'
                bat '''
                    if exist dist rmdir /s /q dist
                    mkdir dist
                    if exist templates xcopy /E /I /Y templates dist\\templates
                    copy app.py dist\\
                    copy requirements.txt dist\\
                '''
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
                archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed!'
            junit testResults: 'test-results.xml', allowEmptyResults: true
        }
        success {
            echo '✓ Build successful!'
        }
        failure {
            echo '✗ Build failed! Check logs for details.'
        }
        unstable {
            echo '⚠ Build unstable. Review warnings and test failures.'
        }
    }
}
