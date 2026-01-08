pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        VENV = ".venv"
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
                "%PYTHON%" -m venv %VENV%
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                %VENV%\\Scripts\\python.exe -m pip install --upgrade pip
                %VENV%\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Basic Validation') {
            steps {
                bat '''
                %VENV%\\Scripts\\python.exe --version
                %VENV%\\Scripts\\pip.exe list
                '''
            }
        }

    stage('Alembic Migration (Optional)') {
    steps {
        bat '''
        if exist alembic (
            .venv\\Scripts\\alembic.exe upgrade head || echo "Alembic skipped"
        ) else (
            echo "Alembic not configured"
        )
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


