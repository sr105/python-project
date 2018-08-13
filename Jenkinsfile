node {

    def customImage

    stage('Checkout Latest Source') {
        def scmVars = checkout scm
        // env.GIT_COMMIT = scmVars.GIT_COMMIT
        // env.GIT_BRANCH = scmVars.GIT_BRANCH
    }

    // stage('Setup Environment') {
    //     env.PROJECT_ID = env.GIT_BRANCH
    //     env.RANDOM_HASH = sh(returnStdout: true, script: "sha256sum").trim()
    //     if (env.GIT_BRANCH == 'master') {
    //         env.MARATHON_FILE = 'prod'
    //         env.PROJECT_ID = 'prod'
    //     }
    //     else if(env.GIT_BRANCH == 'staging'){ env.MARATHON_FILE = env.GIT_BRANCH }
    //     else if(env.GIT_BRANCH == 'dev') { env.MARATHON_FILE = env.GIT_BRANCH }
    //     else { env.MARATHON_FILE = 'feature' }
    // }

    stage('Build Container and Register') {
        customImage = docker.build()
    }

    stage ('Run Tests') {
        customImage.inside {
            sh "pytest --junit-xml=test_results.xml /app || exit 0"
            junit keepLongStdio: true, allowEmptyResults: true, testResults: 'test_results.xml'
        }
    }
}
