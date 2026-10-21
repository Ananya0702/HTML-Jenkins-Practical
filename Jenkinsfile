
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist test.py exit /b 1'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat '"C:\\Users\\pakash chandra shukl\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" test.py'
            }
        }
    }

    post {
        success {
            echo 'All HTML form tests passed!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
