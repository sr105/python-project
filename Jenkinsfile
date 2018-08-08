pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'false'
            }
        }
        stage('deploy') {
            steps {
                sh 'python --version'
            }
        }
    }
}
