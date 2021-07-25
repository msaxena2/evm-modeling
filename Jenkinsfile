pipeline {
  agent { label 'docker && !smol' }
  environment {
    GITHUB_TOKEN     = credentials('rv-jenkins')
    VERSION          = '1.0.1'
    LONG_REV         = """${sh(returnStdout: true, script: 'git rev-parse HEAD').trim()}"""
    SHORT_REV        = """${sh(returnStdout: true, script: 'git rev-parse --short=7 HEAD').trim()}"""
    KEVM_RELEASE_TAG = "v${env.VERSION}-${env.SHORT_REV}"
    K_VERSION        = """${sh(returnStdout: true, script: 'cd deps/k && git tag --points-at HEAD | cut --characters=2-').trim()}"""
  }
  options { ansiColor('xterm') }
  stages {
    stage('Init title') {
      when { changeRequest() }
      steps { script { currentBuild.displayName = "PR ${env.CHANGE_ID}: ${env.CHANGE_TITLE}" } }
    }
    stage('Build and Test') {
      agent {
        dockerfile {
          additionalBuildArgs '--build-arg K_COMMIT="${K_VERSION}" --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)'
          reuseNode true
        }
      }
      stages {
        stage('Build') { steps { sh 'make build RELEASE=true -j6' } }
        stage('Test') {
          failFast true
          options {
            lock("proofs-${env.NODE_NAME}")
            timeout(time: 150, unit: 'MINUTES')
          }
          parallel {
            stage('Conformance (LLVM)')         { steps { sh 'make test-conformance -j8 TEST_CONCRETE_BACKEND=llvm' } }
            stage('Proofs (Java)')              { steps { sh 'make test-prove -j5 TEST_SYMBOLIC_BACKEND=java'       } }
            stage('Proofs (Haskell)')           { steps { sh 'make test-prove -j4 TEST_SYMBOLIC_BACKEND=haskell'    } }
          }
        }
        stage('Test Interactive') {
          failFast true
          options { timeout(time: 35, unit: 'MINUTES') }
          parallel {
            stage('LLVM krun')      { steps { sh 'make test-interactive-run TEST_CONCRETE_BACKEND=llvm'           } }
            stage('Java krun')      { steps { sh 'make test-interactive-run TEST_CONCRETE_BACKEND=java'           } }
            stage('Haskell krun')   { steps { sh 'make test-interactive-run TEST_CONCRETE_BACKEND=haskell'        } }
            stage('LLVM Kast')      { steps { sh 'make test-parse TEST_CONCRETE_BACKEND=llvm'                     } }
            stage('Failing tests')  { steps { sh 'make test-failure TEST_CONCRETE_BACKEND=llvm'                   } }
            stage('Java KLab')      { steps { sh 'make test-klab-prove TEST_SYMBOLIC_BACKEND=java'                } }
            stage('Haskell Search') { steps { sh 'make test-interactive-search TEST_SYMBOLIC_BACKEND=haskell -j4' } }
            stage('KEVM help')      { steps { sh './kevm help'                                                    } }
          }
        }
      }
    }
    stage('Package') {
      when {
        branch 'master'
        beforeAgent true
      }
      post { failure { slackSend color: '#cb2431' , channel: '#kevm' , message: "Packaging Phase Failed: ${env.BUILD_URL}" } }
      stages {
        stage('Ubuntu Focal') {
          stages {
            stage('Build Ubuntu Focal') {
              agent {
                dockerfile {
                  additionalBuildArgs '--build-arg K_COMMIT="${K_VERSION}" --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)'
                  reuseNode true
                }
              }
              steps {
                dir('focal-build') {
                  checkout scm
                  sh './package/debian/package focal'
                }
                stash name: 'focal', includes: "kevm_${env.VERSION}_amd64.deb"
              }
            }
            stage('Test Ubuntu Focal') {
              agent {
                dockerfile {
                  filename 'package/debian/Dockerfile.test'
                  additionalBuildArgs '--build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) --build-arg BASE_IMAGE=ubuntu:focal'
                  reuseNode true
                }
              }
              options {
                skipDefaultCheckout()
                timeout(time: 25, unit: 'MINUTES')
              }
              steps {
                dir('focal-test') {
                  checkout scm
                  unstash 'focal'
                  sh '''
                    export KLAB_OUT=$(pwd)
                    sudo DEBIAN_FRONTEND=noninteractive apt-get update
                    sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade --yes
                    sudo DEBIAN_FRONTEND=noninteractive apt-get install --yes ./kevm_${VERSION}_amd64.deb
                    which kevm
                    kevm help
                    kevm version
                    make -j4 test-interactive-run    TEST_CONCRETE_BACKEND=llvm
                    make -j4 test-interactive-run    TEST_CONCRETE_BACKEND=java
                    make -j4 test-interactive-run    TEST_CONCRETE_BACKEND=haskell
                    make -j4 test-parse              TEST_CONCRETE_BACKEND=llvm
                    make -j4 test-failure            TEST_CONCRETE_BACKEND=llvm
                    make -j4 test-klab-prove         TEST_SYMBOLIC_BACKEND=java
                    make -j4 test-interactive-search TEST_SYMBOLIC_BACKEND=haskell
                  '''
                }
              }
            }
          }
        }
        stage('DockerHub') {
          environment {
            DOCKERHUB_TOKEN   = credentials('rvdockerhub')
            FOCAL_VERSION_TAG = "ubuntu-focal-${env.SHORT_REV}"
            FOCAL_BRANCH_TAG  = "ubuntu-focal-${env.BRANCH_NAME}"
            DOCKERHUB_REPO    = "runtimeverificationinc/kframework-evm-semantics"
          }
          stages {
            stage('Build Image') {
              agent { label 'docker' }
              steps {
                dir('focal') { unstash 'focal' }
                sh '''
                    mv focal/kevm_${VERSION}_amd64.deb kevm_amd64_focal.deb
                    docker login --username "${DOCKERHUB_TOKEN_USR}" --password "${DOCKERHUB_TOKEN_PSW}"
                    docker image build . --file package/docker/Dockerfile.ubuntu --tag "${DOCKERHUB_REPO}:${FOCAL_VERSION_TAG}" --build-arg BASE_IMAGE=focal
                    docker image push "${DOCKERHUB_REPO}:${FOCAL_VERSION_TAG}"
                    docker tag "${DOCKERHUB_REPO}:${FOCAL_VERSION_TAG}" "${DOCKERHUB_REPO}:${FOCAL_BRANCH_TAG}"
                    docker push "${DOCKERHUB_REPO}:${FOCAL_BRANCH_TAG}"
                '''
              }
            }
            stage('Test Focal Image') {
              agent {
                docker {
                  image "${DOCKERHUB_REPO}:${FOCAL_VERSION_TAG}"
                  args '-u 0'
                  reuseNode true
                }
              }
              steps { sh 'which kevm ; kevm help ; kevm version ;' }
            }
          }
        }
      }
    }
    stage('Deploy') {
      when {
        branch 'master'
        beforeAgent true
      }
      agent {
        dockerfile {
          additionalBuildArgs '--build-arg K_COMMIT="${K_VERSION}" --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)'
          reuseNode true
        }
      }
      post { failure { slackSend color: '#cb2431' , channel: '#kevm' , message: "Deploy Phase Failed: ${env.BUILD_URL}" } }
      stages {
        stage('GitHub Release') {
          steps {
            dir('focal')  { unstash 'focal'  }
            sshagent(['2b3d8d6b-0855-4b59-864a-6b3ddf9c9d1a']) {
              sh '''
                git clone 'ssh://github.com/kframework/evm-semantics.git' kevm-release
                cd kevm-release
                git fetch --all

                git tag -d "${KEVM_RELEASE_TAG}"         || true
                git push -d origin "${KEVM_RELEASE_TAG}" || true
                hub release delete "${KEVM_RELEASE_TAG}" || true

                git tag "${KEVM_RELEASE_TAG}" "${LONG_REV}"
                git push origin "${KEVM_RELEASE_TAG}"

                focal_name=kevm_${VERSION}_amd64_focal.deb
                mv ../focal/kevm_${VERSION}_amd64.deb  ${focal_name}

                echo "KEVM Release ${KEVM_RELEASE_TAG}"  > release.md
                echo ''                                 >> release.md
                cat INSTALL.md                          >> release.md
                hub release create                                          \
                    --attach ${focal_name}'#Ubuntu Focal (20.04) Package'   \
                    --file release.md "${KEVM_RELEASE_TAG}"
              '''
            }
          }
        }
        stage('Update Dependents') {
          steps {
            build job: 'rv-devops/master', propagate: false, wait: false                                         \
                , parameters: [ booleanParam ( name: 'UPDATE_DEPS'         , value: true                       ) \
                              , string       ( name: 'UPDATE_DEPS_REPO'    , value: 'kframework/evm-semantics' ) \
                              , string       ( name: 'UPDATE_DEPS_VERSION' , value: "${env.LONG_REV}")           \
                              ]
          }
        }
        stage('Jello Paper') {
          steps {
            sshagent(['2b3d8d6b-0855-4b59-864a-6b3ddf9c9d1a']) {
              dir("kevm-${env.VERSION}-jello-paper") {
                sh '''
                  git clone 'ssh://github.com/kframework/evm-semantics.git'
                  cd evm-semantics
                  git checkout -B gh-pages origin/master
                  git submodule update --init --recursive -- ./web
                  cd web
                  npm install
                  npm run build
                  npm run build-sitemap
                  cd -
                  mv web/public_content ./
                  rm -rf $(find . -maxdepth 1 -not -name public_content -a -not -name .git -a -not -path . -a -not -path .. -a -not -name CNAME)
                  mv public_content/* ./
                  rm -rf public_content
                  git add ./
                  git commit -m 'gh-pages: Updated the website'
                  git merge --strategy ours origin/gh-pages --allow-unrelated-histories
                  git push origin gh-pages
                '''
              }
            }
          }
        }
      }
    }
  }
}
