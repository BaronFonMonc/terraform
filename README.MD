Go to backend dir and run following comands:

docker image build -t flask_docker .
docker run -p 5000:5000 -d flask_docker
docker tag flask_docker timachanep/flask-docker
docker push timachanep/flask-docker

Then go back to terraform to dir with main.tf and run terraform apply.
