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
            sh 'git clone https://github.com/itsmeshabeeb/Docker-Django.git && cd Docker-Django && ls -la'
            sh 'docker ps -a'
          }
        }

      }
    }

    stage('error') {
      steps {
        sh '  docker build . -t docker-jenkins-test && docker tag docker-jenkins-test:latest 014189373214.dkr.ecr.ap-south-1.amazonaws.com/docker-jenkins-test:latest && docker push 014189373214.dkr.ecr.ap-south-1.amazonaws.com/docker-jenkins-test:latest'
      }
    }

  }
}