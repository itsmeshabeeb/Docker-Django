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
            sh '''git clone https://github.com/itsmeshabeeb/Docker-Django.git && cd Docker-Django && aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 014189373214.dkr.ecr.ap-south-1.amazonaws.com
  && docker tag django:latest 014189373214.dkr.ecr.ap-south-1.amazonaws.com/django:latest && docker push 014189373214.dkr.ecr.ap-south-1.amazonaws.com/django:latest'''
          }
        }

      }
    }

  }
}