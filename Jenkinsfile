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
        stage('Run WoG app') {
            agent {
                docker { 
                    image 'ofirdassa/wog:wog'
                    args '-p 5000:5000'
                    reuseNode true
                    ''
                }
            }
            // steps {
            //     script {
            //         sh '''
            //             psql -h redshift-cluster-prod.cbqaieorrxk9.us-east-1.redshift.amazonaws.com -p 5439 -U centrical -d datacentric -f /tmp/t.sql -AF, > t.csv
            //         '''
            //     }
            // }
        }
        stage ('Run Tests') {
            agent {
                docker { 
                    image 'ofirdassa/wog:wog_tests'
                    args '-e HOSTIP=host.docker.internal'
                    reuseNode true
                    ''
                }
            }
        }
    }
}