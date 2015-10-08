# Win 下安装NPM和Node

## 下载node 

linux可以直接下载msi安装包来安装，也可以直接下载单个的exe文件来直接运行，根据你的系统选择32位或64位的node。现在对node感兴趣的人应该没几个用32位的了吧。

http://nodejs.org/dist/v0.10.15/node.exe

http://nodejs.org/dist/v0.10.15/x64/node.exe

## 下载npm 
下载地址： http://nodejs.org/dist/npm/npm-1.3.7.zip 
你可以到http://nodejs.org/dist/npm找到最新的版本。 
解压npm，我解压到 D:\dev\node\npm 
将 node.exe 挪到 D:\dev\node\npm，这样npm就可以调用到node了，当然也可以把node.exe所在目录加入到path中

检查是否能正常运行 
cd D:\dev\node\npm 
D: 
node -v 
npm -v

## 编写一个简单的服务器体验一下

var http = require('http');
 
http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
}).listen(8000);
 
console.log('Server running at http://localhost:8000/');
1、保存代码到 d:\test\test1.js 
2、命令行下执行命令： 
D:\dev\node\node d:\test\test1.js

通过浏览器访问 http://localhost:8000/

看到结果了吗？