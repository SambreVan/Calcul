pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                echo 'Exécution des tests...'
                bat 'docker-compose up -d'
                bat 'docker-compose run web pytest'
                bat 'docker-compose down'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }
    post {
        always {
            bat 'docker-compose down'
        }
    }
}
