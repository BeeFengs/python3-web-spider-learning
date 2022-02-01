#!/usr/bin/env python
# encoding: utf-8

import os
import time
import random
import logging

# 安装好playwright后，安装驱动：playwright install 命令
from playwright.sync_api import sync_playwright

def new_cookie(url):
    cookie = None
    def set_cookie(req):
        nonlocal cookie
        if "cookie" in req.headers:
            cookie = req.headers["cookie"]

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
        # Open new page
        page = context.new_page()
        page.on("request", set_cookie)
        print(cookie,"old cookie")
        page.goto(url)
        page.click("[placeholder=\" 笔名/已验证手机\"]")
        # Fill [placeholder=" 笔名/已验证手机"]
        page.fill("[placeholder=\" 笔名/已验证手机\"]", "xxxxx")
        # Click [placeholder=" 请输入密码"]
        page.click("[placeholder=\" 请输入密码\"]")
        # Fill [placeholder=" 请输入密码"]
        page.fill("[placeholder=\" 请输入密码\"]", "xxxx")
        # Click text=登 录
        # with page.expect_navigation(url="https://shuo.taoguba.com.cn/shuo/shuoindex"):
        time.sleep(random.randrange(5, 8,0.1))
        page.click("text=登 录")
        try:
            # page.on("request", set_cookie)
            page.wait_for_timeout(10000)
            page.close()
        except Exception as e:
            print("Error in playwright script.")
            print(e)
            page.close()
        browser.close()

    return cookie




if __name__ == '__main__':
    url = "https://sso.taoguba.com.cn/web/login/index?url=https://shuo.taoguba.com.cn/shuo/shuoindex"
    cookies = new_cookie(url)

    # 同步模式

    # 异步模式
    # asyncio.run(async_demo())