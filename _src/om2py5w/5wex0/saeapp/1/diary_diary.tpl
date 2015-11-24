<!DOCTYPE html>
<html lang="zh-CN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Web Diary</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<h1>Web Diary</h1>
<form action="/" method="post">

            <br>

            <div>
            <input type="text" name="diary_text" size="40" placeholder="请输入,回车键结束"/>
            </div>
            <div>
                TAG
                <input name = 'tags'></input>
            </div>
            
            <a href='/'>历史<a>
            <center>
            <textarea rows="10" cols="50" readonly>{{diary_textarea}}
            </textarea>
            <center>
</form>
    %import time
    %for row in diary_textarea:
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          <em class=tags>tags: {{' '.join(row['tags'])}}</em><br>
          <pre class=content>{{row['content']}}</pre>
        </div>
    %end
    <h5>本站共被访问{{traffic}}次, 共有{{note}}条笔记</h5>
</body>
</html>
