pipeline {
    agent any
    stages{
        stage ('Gather parameters') {
            steps{
                timeout(time: 60, unit: 'SECONDS') {
                    script {
                        try {
                            def INPUT_PARAMS = input message: 'Please Provide Parameters', ok: 'Next',
                                parameters: [
                                choice(name: 'BUILD', choices: ['Yes','No'].join('\n'), description: 'Build images'),
                                choice(name: 'PUSH', choices: ['Yes','No'].join('\n'), description: 'Push images to docker-hub')] 
                                env.BUILD = INPUT_PARAMS.BUILD
                                env.PUSH = INPUT_PARAMS.PUSH
                        }
                        catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException ex) {
                            env.BUILD = "Yes"
                            env.PUSH = "Yes"
                        }
                        catch (Exception ex) {
                            println("Unable to run command: ${ex}")
                        }
                    }
                }
            }
        }
        stage ('Build & Push images') {
            steps{
                script{
                    try {
                        if ("${BUILD}" == "Yes") {
                            sh '''
                                docker-compose build
                            '''
                        }
                        else {
                            println("Not building")
                        }
                        if ("${PUSH}" == "Yes") {
                            sh '''
                                docker-compose push
                            '''
                        }
                        else {
                            println("Not pushing")
                        }
                    }
                    catch (Exception ex) {
                        println("Unable to run command: ${ex}")
                    }
                }
            }
        }
        stage ('Run & Test WoG app') {
            steps {
                script {
                    try {
                        sh '''
                        docker run -d -v ${WORKSPACE}/Scores.txt:/usr/src/app/Scores.txt -p 5000:5000 wog
                        docker run -d -e HOSTIP=host.docker.internal ofirdassa/wog:wog_tests
                        sleep 3
                        export CONTAINER_ID=$(docker ps -a | grep wog:wog_tests | cut -d " " -f1)
                        export EXIT_CODE=$(docker inspect $CONTAINER_ID --format='{{.State.ExitCode}}')
                        docker logs $CONTAINER_ID
                        curl localhost:5000/index.html
                        '''
                        if ("${EXIT_CODE}" == "1") {
                            currentBuild.result = 'ABORTED'
                            error("Aborting the build.")
                        }
                    }
                    catch (Exception ex) {
                        println("Unable to run command: ${ex}")
                    }
                }
            }
        }
        stage ('Delete old containers') {
            steps {
                script {
                    sh '''
                    docker kill $(docker ps -q)
                    '''
                }
            }
        }
        // stage('Run & Test WoG app') {
        //     agent {
        //         docker { 
        //             image 'ofirdassa/wog:wog'
        //             args '-p 5000:5000'
        //             reuseNode true
        //         }
        //     }
        //     steps {
        //         script {
        //             sh '''
        //                 docker run ofirdassa/wog:wog_test
        //             '''
        //         }
        //     }
        // }
        // stage ('Run Tests') {
        //     agent {
        //         docker { 
        //             image 'ofirdassa/wog:wog_tests'
        //             args '-e HOSTIP=host.docker.internal'
        //             reuseNode true
        //         }
        //     }
        //     steps {
        //         script {
        //             sh '''
        //                 python --version
        //             '''
        //         }
        //     }
        // }
    }
}