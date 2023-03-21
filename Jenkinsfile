pipeline {
    agent any
    stages {
        stage('Testing GitHub-tests locally') {
            steps {
                dir('C:/Users/Musta/Skrivbord/Uppgift'){ 
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
