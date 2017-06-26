# fuck here
写这个项目的原因是因为在微博上肖像被恶意使用，且维权无果  
于是就写了个脚本跟网上的网友对骂，我就看着他们跟我脚本骂了一个通宵。
## 使用方法

1 注册一个微博账号，并开通open.weibo.com的账号

2 关注你想fuck的用户

3 使用python3环境，安装weibo包

4 使用python3运行 fuck_mahine.py脚本

# 配置说明
## user_configs.json
配置用户信息，支持多用户，多用户可以多线程并发骂。  
fuck_rull.json

```json
{
  "users":[
      {
          "username":"",
          "password":"",
          "app_key":"",
          "api_secret":"",
          "redirect_uri":null
          //可以为单个用户配置一个app_key
      }
  ],
  "api_limit_time":60,//这是一个时间范围之
  "app_key":"",
  "api_secret":"",
  "redirect_uri":null
  //也可以使用公用的app_key，但是微博现在不允许这么用，除非先通过审核且授权。
}
```

配置骂人脚本  
```json
{
  "fuck_mode":[
      "comment",
      "status" //回复微博和微博下的评论
  ],
  "f_words":[
      {
          "text":"操你麻痹，看你麻痹看，滚！"
      }
  ],
  "skip_words":[
      "，滚你妈逼"
  ],
  // f_words和skip_words随机组合
  "fuck_you":[
      "说给网友小张"
  ]
  //时间线中的这位用户会被 fuck  
}

```
