pipeline {
    agent any

    environment {
        IMAGE_NAME = "blue-green-app"
        IMAGE_TAG = "v2"
        GREEN_PORT = "8082"
        GREEN_CONTAINER = "app-green"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Deploy Green') {
            steps {
                sh '''
                    docker rm -f ${GREEN_CONTAINER} || true

                    docker run -d \
                      --name ${GREEN_CONTAINER} \
                      -p ${GREEN_PORT}:8080 \
                      -e App_version=v2.0 \
                      -e App_en=GREEN \
                      ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Health Check Green') {
            steps {
                sh '''
                    sleep 5

                    curl -f http://localhost:${GREEN_PORT}/health
                '''
            }
        }
    }

    post {
        success {
            echo 'Green deployment and health check successful!'
        }

        failure {
            echo 'Green deployment failed!'
        }
    }
}
