pipeline {
    agent any
    stages {
        stage('Clone repository from GitHub'){
            steps {
                checkout scmGit(branches: [[name: '*Muswar*']], extensions: [], userRemoteConfigs: [[credentialsId: 'fe67cc87-9e1e-46d3-aaff-540e34650d4f', url: 'https://github.com/Muswar97/Uppgift.git']])
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
