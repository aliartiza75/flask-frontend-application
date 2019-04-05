pipeline {
    agent {
        docker { 
            image 'python:3.5.1' 
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'pwd'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
