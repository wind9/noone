from test_celery import send_mail


def register():
    print("开始注册")
    print("开始发邮件")
    import time
    start = time.time()
    send_mail.delay("lek@gmail.com")
    print("耗时:",(time.time()-start))
    print("注册完成")


if __name__ == "__main__":
    register()
