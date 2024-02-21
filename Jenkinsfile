pipeline {
    agent any

    environment {
        // Définir les variables d'environnement nécessaires
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Build') {
            steps {
                // Construire l'image Docker
                sh 'docker build -t flask-calculator-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Si besoin de tests'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-calculator-app'
            }
        }
    }
}
