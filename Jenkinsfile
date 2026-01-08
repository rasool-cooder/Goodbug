pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv .venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Basic Validation') {
            steps {
                bat '''
                %VENV%\\Scripts\\activate
                python --version
                pip list
                '''
            }
        }

        stage('Alembic Migration (Optional)') {
            when {
                expression { fileExists('alembic.ini') }
            }
            steps {
                bat '''
                %VENV%\\Scripts\\activate
                alembic upgrade head || echo Alembic skipped
                '''
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo 'Deployment step will be added later'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}

