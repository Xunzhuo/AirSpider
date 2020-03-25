# Git 常用命令

+ 初始化：git init

+ 看见隐藏文件：ls -ah

+ 把文件添加到仓库：git add 文件名字

+ 把文件提交到仓库：git commit -m “注释”

+ 查看当前仓库状态：git status

+ 查看仓库变化：git diff

+ 查看之前提交的记录：git log --graph（--pretty=oneline）--abbrev-commit

+ 返回前一个文件版本：git reset --hard HEAD^ (或者HEAD^^返回前两个版本 或者HEAD~100返回前100个版本)

+ 查看之前版本和现在版本的区别：git diff HEAD --      文件名

+ 回到任意版本：git reset --hard 版本号（可残缺）

+ 查看文件内容：cat 文件名字

+ 查看你之前的命令：git reflog

+ 丢弃工作区的修改，返回上一个版本：git checkout --       文件名

+ 撤销暂存区的文件：git reset HEAD 文件名

+ 删除文件：git rm 文件名

+ 建立远程仓库：git remote add 仓库名 网页仓库链接

+ 产看远程仓库名字：git remote

+ 删除远程仓库：git remote rm 仓库名

+ 第一次将本地提交：git push -u 仓库名 master

+ 之后将本地提交：git push 仓库名 master

+ 将远程仓库下载到本地仓库：git clone 网页仓库链接

+ 创建一个分支然后切换到该分支：git switch -c 分支名字

+ 创建一个分支：git branch 分支名字

+ 删除一个认知：git branch -d 分支名字

+ 切换到指定分支：git switch 分支名字

+ 查看分支：git branch

+ 将主指针合并到当前分支：git merge 希望切换到的分支名字

+ 将主干和分支合并并且保留分支：git merge --no-ff -m    “注释”    希望合并的分支

+ 保存工作现场：git stash

+ 查看保存情况：git stash list

+ 恢复保存的现场：git stash apply   现场名字

+ 删除保存的现场：git stash drop

+ 回复并且删除保存的现场：git stash pop

+ 复制一个分支并且提交：git cherry-pick 版本号