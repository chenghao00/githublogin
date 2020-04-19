# githublogin
scrapy模拟登陆之自动登录


#github中是用的yield scrapy.FormRequest.from_response(response,fromdata={'login':'xx','password':'xx'},callback=self.after_login)


#github2中用的是 yield scrapy.FormRequest(‘x x x/session’,formdata=post_data,callback=self.after_login)
