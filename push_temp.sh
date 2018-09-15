#git add *.md
git add .
git commit -m 'updated .md files'
git push origin master
open $(git remote get-url origin)
