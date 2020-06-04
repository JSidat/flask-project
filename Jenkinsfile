pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./Script/*'
            }
        }
        stage('Get the envinronment ready') {
            steps {
                sh './Script/before-installation.sh'
                sh './Script/installation.sh'
            }
        }
        stage('Run the application') {
            steps {
                sh 'sudo systemctl restart flask.service'
            }
        }
    }
}
