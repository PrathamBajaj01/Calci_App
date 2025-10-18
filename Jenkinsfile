pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/PrathamBajaj01/Calci_App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('calci-app')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('calci-app').inside {
                        sh 'pytest -v'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'All tests passed ✅'
        }
        failure {
            echo 'Some tests failed ❌'
        }
    }
}
