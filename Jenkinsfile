pipeline {
    agent any

    environment {
        // Définir les variables d'environnement nécessaires
        FLASK_APP = 'app.py'
        DOCKER_HOST = '\\.\\pipe\\docker_engine'
    }

    stages {
        stage('Build') {
            steps {
                // Construire l'image Docker
                bat 'sudo docker build -t flask-calculator-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Si besoin de tests'
            }
        }
        stage('Deploy') {
            steps {
                // Déployer l'application en utilisant Docker avec un utilisateur non privilégié (-u option)
                bat 'sudo docker run -d -p 5000:5000 --user "$(id -u):$(id -g)" flask-calculator-app'
            }
        }
    }
}
