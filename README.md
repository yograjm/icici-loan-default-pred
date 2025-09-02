# icici-loan-default-pred

Install training requirements:

`pip install -r requirements/requirements.txt`

Run training script: 

`python train_model.py`

Install Test requirements

`pip install -r requirements/test_requirements.txt`

Run test cases

`pytest`

Install API requirements

`pip install -r requirements/api_requirements.txt`

Run Gradio OR FastAPI 

`python app.py`

`python app2.py`  (Swagger Documentation will be avaiable on this endpoint ->   /docs )

Build Docker image

`docker build -t loan_default_pred .`

Start Docker Container

`docker run -d -it -p 7860:7860 --name=myapp loan_default_pred:latest`

`docker logs -f myapp`   (to check container logs)

## To push docker image on DockerHub

Tag Docker Iamge with your Docker Username

`docker tag loan_default_pred <YOUR-DOCKER-USERNAME>/loan_default_pred`

Login to DockerHub

`docker login -u <YOUR-DOCKER-USERNAME>`  (Paste YOUR Docker Access Token when prompted)

`docker push <YOUR-DOCKER-USERNAME>/loan_default_pred`


