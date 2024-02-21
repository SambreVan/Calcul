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
                    // Activez un environnement virtuel si nécessaire
                    // sh 'source venv/bin/activate'
                    sh 'pytest --junitxml=test-reports/report.xml'
                }
            }
            post {
                always {
                    // Collecter les résultats des tests pour Jenkins
                    junit '**/test-reports/*.xml'
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