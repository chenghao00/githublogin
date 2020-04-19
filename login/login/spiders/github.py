# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动的从response中寻找from表单
            formdata={"login":"xxx","password":"xxx"},
            callback = self.after_login
        )

    def after_login(self,response):
        print(re.findall("noobpythoner|NoobPythoner",response.body.decode()))

