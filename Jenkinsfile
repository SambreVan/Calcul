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
                bat 'docker build -t flask-calculator-app .'
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest --junitxml=test-reports/report.xml'
                    // Liste le contenu du répertoire pour vérification
                    sh 'ls -la test-reports'
                }
            }
            post {
                always {
                    // Collecter les résultats des tests pour Jenkins
                    junit '**/test-reports/*.xml'
                    // Nettoyer le répertoire des rapports après la collecte
                    sh 'rm -rf test-reports'
                }
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5001:5000 flask-calculator-app'
            }
        }
    }
}