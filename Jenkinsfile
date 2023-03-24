pipeline {
  agent any
  stages {
    stage('new') {
      steps {
        git(url: 'https://github.com/itsmeshabeeb/Docker-Django', branch: 'master')
      }
    }

    stage('print files') {
      parallel {
        stage('print files') {
          steps {
            sh '''ls -la



'''
            sh 'ls -la'
          }
        }

        stage('build') {
          steps {
            sh 'docker build . -t django:latest'
          }
        }

      }
    }

  }
}