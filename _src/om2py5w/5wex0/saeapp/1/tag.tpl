<!DOCTYPE html>
<html>
  <head>
    <title>Alan's Diary</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
     margin: 10px 20%;}
      em.date { color: #999;}
      em.tags { color: #999;}
    </style>
  </head>
  <body>
    <h1><a href='/'>返回<a></h1>
    <h1>标签{{tag}}的历史记录</h1>
    %import time
    %for row in diary:
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          <em class=tags>tags: {{' '.join(row['tags'])}}</em><br>
          <p class=content>{{!row['content'].replace('\n','<br/>')}}</p>
        </div>
    %end
  </body>
</html>
