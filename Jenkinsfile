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
                python -m venv %VENV%
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
`
