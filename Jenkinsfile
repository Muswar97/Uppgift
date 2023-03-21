pipeline {
    agent any
    stages {
        stage('Clone repository from GitHub'){
            steps {
                checkout scmGit(branches: [[name: '']], extensions: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/Muswar97/Uppgift.git']])
                }
            }
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
