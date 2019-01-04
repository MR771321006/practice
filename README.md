# texas_holdem_record_sanic
#
德州扑克术语表

## 数据来源
<http://thepokerlogic.com/glossary>

<https://www.pokerstars.com/zhs/poker/terms/>

<https://zh.pokerstrategy.com/glossary/>

<https://www.pk.cn/portal-glossary>

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
