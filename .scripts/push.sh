# This script is used to push all the changes to the github repository.
# Before pushing the changes it removes all the cache options as well 
# as the C object options.
#
# To run this script use:
#   sh push.sh <commit-flag> <commit-msg>
#
if ! [ -x "$(command -v git)" ]; then
  echo 'Error: git is not installed.' >&2
  exit 1
fi

git pull
rm -rf client/trojan/*.o
git add .
git commit -m "$1: $2"
git push
