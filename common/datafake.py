from faker import Faker
import functools
from log import logger

fake = Faker('zh_CN')


def capture_responses(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        page = kwargs.get('page')
        if not page:
            raise ValueError("必须提供 'page' 参数")

        responses = []

        def log_response(response):
            try:
                if response.status == 200:
                    try:
                        body = response.json()
                    except ValueError:
                        body = response.body()  # 获取原始的二进制内容
                    responses.append({
                        'url': response.url,
                        'status': response.status,
                        'body': body
                    })
            except Exception as e:
                logger.error(f"处理响应时发生错误: {e}")

        page.on("response", log_response)

        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"执行 {func.__name__} 时发生错误: {e}")
            for response in responses:
                logger.error(f"接口返回: URL={response['url']}, 状态={response['status']}, 内容={response['body']}")
            raise
 
    return wrapper