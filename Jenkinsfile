node {
    stage('Clear workspace') {
        deleteDir()
    }
    stage('Preparation') { 
        git branch: 'main', url: "https://github.com/AralAskarov/modern-techniques-sis1.git"
    }
    stage('Preparation') { 
        sh "python3 namesprint.py"
    }
    stage('Post clear workspace') {
        deleteDir()
    }
}
