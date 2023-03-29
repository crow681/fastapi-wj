# FastApi-wj
FastApi框架练习
高效快速的web框架，基于python3.6


## 安装部署
### 依赖
- python3.6及以上版本
- Starlette:负责web部分
- Pydantic:负责数据部分

### 安装
> pip install fastapi 
### 部署
可以使用Uvicorn或者Hypercorn
> pip install uvicorn[standard]
### 运行
> uvicorn main:app --reload
### 自动生成的接口文档
http://127.0.0.1:8000/docs或者http://127.0.0.1:8000/redoc