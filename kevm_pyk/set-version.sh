#!/usr/bin/env bash

set -euxo pipefail

cd deps/k
git fetch origin 'refs/tags/*:refs/tags/*'
K_COMMIT="$(git tag --points-at HEAD | cut --characters=2-)"
cd ../..

cat kevm_pyk/setup.cfg.tmpl | sed 's/\${K_COMMIT}/'"${K_COMMIT}"'/' > kevm_pyk/setup.cfg
git add kevm_pyk/setup.cfg
! git commit -m "kevm_pyk/setup.cfg: update version to ${K_COMMIT}" || git push
