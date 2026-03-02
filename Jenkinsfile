pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Mohan1521/NewPlaywrightProjects.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install pytest playwright'
                sh 'playwright install'
            }
        }
        stage('Run Playwright Tests') {
            steps {
                sh 'pytest Mytest/tes_looooo.py'
            }
        }
    }
}

