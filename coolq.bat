
			 
docker run -ti --rm --name cqhttp-test  -p 9000:9000 -p 5700:5700 -e COOLQ_ACCOUNT=1978003202 -e CQHTTP_SERVE_DATA_FILES=yes richardchien/cqhttp:latest