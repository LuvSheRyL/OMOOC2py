# SSH 配置


## 检查SSH keys的设置

1、 首先我们需要检查你电脑上现有的ssh key：

    $ cd ~/.ssh

如果显示`“No such file or directory”`，跳到第三步，否则继续。


2、备份和移除原来的ssh key设置：

因为已经存在key文件，所以需要备份旧的数据并删除：

    $ ls
    config  id_rsa  id_rsa.pub  known_hosts
    $ mkdir key_backup
    $ cp id_rsa* key_backup
    $ rm id_rsa*
    

3、生成新的SSH Key：

输入下面的代码，就可以生成新的key文件，我们只需要默认设置就好，所以当需要输入文件名的时候，回车就好。
    
    $ ssh-keygen -t rsa -C "邮件地址@youremail.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/your_user_directory/.ssh/id_rsa):
<回车就好>

然后系统会要你输入加密串（Passphrase）：
    
    Enter passphrase (empty for no passphrase):<输入加密串>
    Enter same passphrase again:<再次输入加密串>
    

4、添加SSH Key到GitHub：

在本机设置SSH Key之后，需要添加到GitHub上，以完成SSH链接的设置。

用文本编辑工具打开id_rsa.pub文件，如果看不到这个文件，你需要设置显示隐藏文件。准确的复制这个文件的内容，才能保证设置的成功。

在GitHub的主页上点击设置(`settings-accountsetting→SSH keys`
)按钮：


> PS：如果需要配置多个GitHub账号，可以参看这个多个github帐号的SSH key切换，不过需要提醒一下的是，如果你只是通过这篇文章中所述配置了Host，那么你多个账号下面的提交用户会是一个人，所以需要通过命令git config --global --unset user.email删除用户账户设置，在每一个repo下面使用git config --local user.email '你的github邮箱@mail.com' 命令单独设置用户账户信息

5、测试一下

可以输入下面的命令，看看设置是否成功，git@github.com的部分不要修改：

    $ ssh -T git@github.com
如果是下面的反应：

    The authenticity of host 'github.com (207.97.227.239)' can't be established.
    RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    Are you sure you want to continue connecting (yes/no)?

不要紧张，输入`yes`就好，然后会看到：

    Hi <em>username</em>! You've successfully authenticated, but GitHub does not provide shell access.

6、设置你的账号信息

现在你已经可以通过SSH链接到GitHub了，还有一些个人信息需要完善的。

Git会根据用户的名字和邮箱来记录提交。GitHub也是用这些信息来做权限的处理，输入下面的代码进行个人信息的设置，把名称和邮箱替换成你自己的，名字必须是你的真名，而不是GitHub的昵称。


    $ git config --global user.name "你的名字"
    $ git config --global user.email "your_email@youremail.com"



