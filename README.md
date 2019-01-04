# texas_holdem_record_sanic

## api开发流程
### 1. 添加测试
  
  1. 根据设计好的api添加相应的测试，测试中验证返回数据是否符合api期望
  
### 2. 添加api
  1. 在 `models.db_scheme` 中添加需要的 Model
  2. 在 `views.serializers` 中添加用于验证 api 数据数据的 serializer
  3. 在 `views.views` 中添加 api 处理视图类
  4. 在 `views.routers` 中添加 url 路由
### 3.添加文档
  1.文档中需要详细描述 `api` 的 `url path`, `url params`, `header`, `body`
### 4.测试
  1. 完善 `.drone.yml`
  2. 本地使用时, 添加本地配置 `configs/local_settings.py`, 运行 `python manage.py test --
    config=local_settings` 进行测试
  3. 本地同步数据库: `python manage.py sync_db --config=local_settings`
  4. 本地启动服务器: `python manage.py runserver --config=local_settings`
### 5. 部署
  1. 申请 sentry dsn, 配置到 `configs/__init__.py` 中
    后续部署流程等待 k8s 使用流程确定好后完善
# 如何使用

```
> cd docker
> docker-compose up -d
> docker-compose exec backend bash
```
## 进入 docker 以后, 运行 runserver.sh
> ./runserver.sh
