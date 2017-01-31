startDb:

    docker run --detach --name myDatabase1 --env="MYSQL_ROOT_PASSWORD=password" --publish 6603:3306 --volume=/root/docker/test-mysql/conf.d:/etc/mysql/conf.d --volume=/storage/    docker/mysql-datadir1:/var/lib/mysql -d mysql/mysql-server:5.7.16
    docker run --detach --name myDatabase2 --env="MYSQL_ROOT_PASSWORD=password" --publish 6604:3306 --volume=/root/docker/test-mysql/conf.d:/etc/mysql/conf.d --volume=/storage/    docker/mysql-datadir2:/var/lib/mysql -d mysql/mysql-server:5.7.16
    docker run --detach --name myDatabase3 --env="MYSQL_ROOT_PASSWORD=password" --publish 6605:3306 --volume=/root/docker/test-mysql/conf.d:/etc/mysql/conf.d --volume=/storage/    docker/mysql-datadir3:/var/lib/mysql -d mysql/mysql-server:5.7.16

build:
    docker build assignment3:v1 .
    docker build assignment3:v2 .
    docker build assignment3:v3 .

run:
    docker run -id -p 5000:5000 —name appcontainer1 --link myDatabase1:mysql -d assignment3:v1
    docker run -id -p 6000:5000 —name appcontainer2 --link myDatabase2:mysql -d assignment3:v2
    docker run -id -p 7000:5000 —name appcontainer3 --link myDatabase3:mysql -d assignment3:v3

