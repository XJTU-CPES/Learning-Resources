# Git笔记


## Git仓库搭建操作命令

配置名字和邮箱：

```bash
$ git config --global user.name "puzhenyu"

$ git config --global user.email zhenyupu@foxmail.com
```

在项目所在文件夹输入：$ git init，就变成git仓库

克隆别人的项目：`git clone URL`

文件四个状态：未跟踪，未修改，已修改，暂存

跟踪文件或者目录： `$ git add <name>`

不想被跟踪——删除： `$ git rm <name>`

保留在目录但不被跟踪：`$ git rm --cache <name>`

缓存状态： `git add <file-name>`

取消缓存：`git reset HEAD <name>`

提交修改：`git commit -m '修改内容'`

取消提交： `git reset head~ --soft`，但不能撤回第一次提交

查看状态：`git status`

查看文件哪里被修改：`git diff`

查看提交历史：`git log`，美化输出：`git log --pretty`

e.g. `git log--pretty=oneline`, `git log --graph`

连接远程仓库：`git remote add filename URL`

修改名字： `git remote rename oldname newname`

推送分支：`git push filename branch`

ssh协议去健全：

```bash
ssh_test cd ~/.ssh
.ssh ssh-keygen -t rsa -b 4096 -C "zhenyupu@foxmail.com" #生成密钥
```

同步问题：

```
git init
git add .      #缓存所有文件
git status     #查看状态
git commit -m "`date +\"%Y-%m-%d\"`"  #提交所有修改
git push origin master    #更新远程仓库
```


为了实现本地代码和github上默认main分支关联,步骤如下进行修复 :
- git checkout -b main
#switched to a new branch 'main'
- git branch




第一次提交到github上：
```
ssh-keygen -t rsa -C "*@*.com"
# 本机命令，查看公钥，或者去文件地址用vscode打开查看：
cat ~/.ssh/id_rsa.pub
# 之后再github线上添加公钥：项目仓库 => settings => SSH and GPG keys => New SSH key 
```



![1693843024189](https://cdn.jsdelivr.net/gh/ZhenyuPU/picx-images-hosting@master/20241012/1693843024189.3hj0t5icjjc0.webp)


create a new repository on the command line:
```bash
echo "# ZhenyuPU.github.io" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ZhenyuPU/ZhenyuPU.github.io.git
git push -u origin main
```



## 分支合并

- git merge master
#将master分支合并 到main上
#Already up to date
- git pull origin main --allow-unrelated-histories
- git push origin main



```
git fetch
git stash
git merge '@{u}'
git stash pop
```
When you can't integrate both storage, you need to look up the following website.

[Stackoverflow融合branch问题](https://stackoverflow.com/questions/39399804/updates-were-rejected-because-the-tip-of-your-current-branch-is-behind-its-remot)



## 大文件上传

需要使用LFS，首先需要安装Git LFS:
- Wins
通过官网下载

- Mac OS
```bash
brew install git-lfs
```
- Linux
```bash
sudo apt-get install git-lfs
```

1. 初始化Git LFS:
```bash
git lfs install
```

2. 跟踪大文件
```bash
git lfs track "*.npz" 
```
其中，`"*.npz"`为文件路径


3. 添加和提交大文件
```bash
git add .gitattributes
git add fold/*.npz
git commit -m "Add large files with LFS"
```


4. 推送到仓库
```bash
git push origin main
```

5. 检查状态
```bash
git lfs ls-files
```

6. 克隆和拉取

拉取时LFS会自动下载