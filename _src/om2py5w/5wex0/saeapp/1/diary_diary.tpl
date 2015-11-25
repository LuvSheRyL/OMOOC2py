<!DOCTYPE html>
<html lang="zh-CN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Web Diary</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style>
      h1, h5, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
     margin: 10px 20%;}
      em.date { color: #999;}
      em.tags { color: #999;}
    </style>
</head>
<body>
<h1>Web Diary</h1>
<form action="/" method="post">


            <div>
            <textarea type="text" id="diary_text" name="diary_text"  placeholder="请输入,回车键结束"></textarea>
            </div>
            <div>
                <input name = 'tags' placeholder="TAG"></input>
            <div><button id="go" type="submit">保存</button></div>
            </div>

</form>
    %import time
    %for row in diary_text:
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          <em class=tags>tags: {{' '.join(row['tags'])}}</em><br>
          <pre class=content>{{row['content']}}</pre>
        </div>
    %end
    <h5>本站共被访问{{traffic}}次, 共有{{note}}条笔记</h5>
</body>
</html>
