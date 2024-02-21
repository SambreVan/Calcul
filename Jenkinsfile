pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    try {
                        bat 'docker build -t flask-calculator-app .'
                    } catch (Exception e) {
                        echo "Erreur lors de la construction de l'image Docker : ${e}"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Si besoin de tests'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    try {
                        bat 'docker run -d -p 5000:5000 flask-calculator-app'
                    } catch (Exception e) {
                        echo "Erreur lors du déploiement de l'application : ${e}"
                    }
                }
            }
        }
    }
}
