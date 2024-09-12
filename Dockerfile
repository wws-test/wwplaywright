# 使用指定的Playwright镜像作为基础镜像
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 设定工作目录
WORKDIR /app

# 将本地代码复制到工作目录
COPY . /app

# 配置 pip 使用自定义的 PyPI 镜像源
#RUN pip install --upgrade pip && \
#    pip config set global.index-url http://10.10.20.115:8081/repository/pypi-proxy/simple/ && \
#    pip config set global.trusted-host 10.10.20.115
# 安装 Allure 命令行工具

RUN apt-get update && apt-get install -y default-jre && \
    apt-get install -y curl && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz
# 安装项目中需要的依赖
RUN pip install -r requirements.txt

# 给予pytest运行权限，并设为入口点
ENTRYPOINT ["pytest"]