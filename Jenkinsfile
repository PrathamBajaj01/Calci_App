pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'  // Set your AWS region
    }

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

        stage('Deploy Lambda') {
            steps {
                script {
                    // Deploy Lambda via SAM
                    sh '''
                    sam build --use-container
                    sam deploy --stack-name calci-stack --no-confirm-changeset --capabilities CAPABILITY_IAM
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'All tests passed and Lambda deployed ✅'
        }
        failure {
            echo 'Some tests failed or deployment failed ❌'
        }
    }
}