# texas_holdem_record_sanic
德州扑克术语表

## api开发流程
### 1.添加测试
  
  1.根据设计好的api添加相应的测试，测试中验证返回数据是否符合api期望
  
### 2.添加api
   1.在`models.db_scheme`中添加需要的 Model


# 启动步骤

```
cd docker
docker-compose up -d
docker-compose exec backend bash

```
# 进入容器后
```
python manage.py sync_db --config=configs.docker_compose

python manage.py runserver --config=configs.docker_compose

```
