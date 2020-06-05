pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./Script/*'
            }
        }
        
        stage('Run application') {
            steps {
                sh './Script/environment.sh'
                
            }
        }
    }
}
