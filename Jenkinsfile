pipeline {
    agent {
        // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
        dockerfile {
            filename 'Dockerfile'
            dir '.'
            // label 'my-defined-label'
            // additionalBuildArgs  '--build-arg version=1.0.2'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'pwd'
                sh 'find . -type d'
                sh 'pytest --junit-xml=/app/python-project.xml /app'
            }
        }
        stage('deploy') {
            steps {
                sh 'python --version'
            }
        }
    }
    post {
        always {
            junit '/app/*.xml'
        }
    }
}
