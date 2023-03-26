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
          }
        }

        stage('build') {
          steps {
            sh 'git pull https://github.com/itsmeshabeeb/Docker-Django.git && cd Docker-Django && ls -la'
            sh 'docker ps -a'
          }
        }

      }
    }

    stage('error') {
      steps {
        sh '  sudo docker build . -t docker-jenkins-test'
      }
    }

  }
}