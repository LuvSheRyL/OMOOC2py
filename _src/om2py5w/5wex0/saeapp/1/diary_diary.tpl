<!DOCTYPE html>
<html lang="zh-CN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>My Diary</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<form action="/" method="post">

            <br>
            <center>
            <textarea rows="10" cols="50" readonly>{{diary_textarea}}
            </textarea>
            <center>
            <input type="text" name="diary_text" size="40" placeholder="请输入,回车键结束"/>
            <a href='/diary'>历史<a>
</form>

%import time
%for row in diary:
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          <em class=tags>tags: {{' '.join(row['tags'])}}</em><br>
          <pre class=content>{{!row['diary_textarea'].replace('\n','<br/>')}}</pre>
        </div>
%end
</body>
</html>
