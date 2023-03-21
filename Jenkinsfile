pipeline {
    agent any
    stages {
        stage('Testing GitHub-tests locally') {
            steps {
                dir('C:\Users\Musta\OneDrive\Skrivbord\Uppgift'){ 
                    bat 'python -m unittest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
        }
    }
