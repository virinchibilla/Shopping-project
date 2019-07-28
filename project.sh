function build-stack {
    docker-compose -p shop build $@
}

function start-stack {
    docker-compose -p shop up -d
}

function stop-stack {
    docker-compose -p shop kill
}

function restart-stack {
    stop-stack && start-stack
}

function logs {
    docker-compose -p shop logs -f $@
}

function db-make-migrations {
    docker exec shop_backend_1 python manage.py makemigrations
}

function db-migrate {
    docker exec shop_backend_1 python manage.py migrate
}

function create-su {
    docker exec -it shop_backend_1 python manage.py createsuperuser
}

function fix-sass {
    docker exec -it shop_frontend_1 npm rebuild node-sass --force
}

function create-database {
    docker exec -i $(docker ps -qf "name=shop_db_1") psql  -U postgres  -c 'CREATE DATABASE postgres WITH OWNER "postgres" ENCODING UTF8 LC_COLLATE = "en_US.UTF-8" LC_CTYPE = "en_US.UTF-8" TEMPLATE template0;'
}

function database-generate-migrate {
    create-database ; db-make-migrations && db-migrate
}


function fix-start-stack {
    start-stack
    id=$(docker ps -qf "name=shop_backend_1")
    docker stop "$id"
    docker start "$id"
}

function fix-sass-stack {
    fix-sass && restart-stack && fix-start-stack 
}


function build-production {
    docker exec shop_frontend_1 npm run build
    rm -rf nginx/static
    mkdir nginx/static
    cp -r frontend/dist/ nginx/
    mv nginx/index.html nginx/static/
    cp -r backend/static/ nginx/static/
    rm -rf frontend/dist
}


echo -e "

Available commands:

\tbuild-stack
\tstart-stack
\tstop-stack
\trestart-stack
\tlogs
\tdb-make-migrations
\tdb-migrate
\tcreate-su
\tbuild-production
\tfix-sass
\tfix-start-stack
\tcreate-database
\tdatabase-generate-migrate
\tfix-sass-stack



"
