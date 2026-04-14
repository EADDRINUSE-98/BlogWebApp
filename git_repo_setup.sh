#!/bin/bash

REMOTE_GITHUB_REPO_SSH_URL="$1"
if [[ -z "${REMOTE_GITHUB_REPO_SSH_URL}" ]]; then
	echo "Usage: ./git_repo_setup.sh [REMOTE_GITHUB_REPO_SSH_URL]"
	exit 1
fi

DEFAULT_GIT_BRANCH="$(git config --global --get init.defaultBranch)"
echo "Defaul branch: ${DEFAULT_GIT_BRANCH}"
echo ""

if [[ ${DEFAULT_GIT_BRANCH} != "main" ]]; then
	git config --global init.defaultBranch main && echo "Changing default branch to: main"
	echo ""
fi

if [[ -d ".git" ]]; then
	echo "Git repo is already initialized here."
	echo ""
else
	git init && echo "Git repo initialized."
	echo ""
fi

SSH_GITHHUB_AUTH_STATUS=$(ssh -T git@github.com 2>&1)
echo "${SSH_GITHHUB_AUTH_STATUS}" | grep -iq ' successfully' && echo "${SSH_GITHHUB_AUTH_STATUS}" | grep -iq 'authenticated'
if [[ $? ]]; then
	echo "Ssh authentication successful."
	echo ""
else
	echo "Either ssh agent is not running or ssh key is not added."
	exit 1
fi

(git remote set-url origin "${REMOTE_GITHUB_REPO_SSH_URL}" || git remote add origin "${REMOTE_GITHUB_REPO_SSH_URL}") && echo "origin set to: ${REMOTE_GITHUB_REPO_SSH_URL}, successfully."
echo ""
