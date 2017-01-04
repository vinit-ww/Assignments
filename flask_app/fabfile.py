from fabistrano import deploy
env.hosts = ["HOST"] # Replace with your host name or IP
env.base_dir = '/www' # Set to your apps directory
env.app_name = 'app_name.com' # This will deploy the app to /www/app_name.com/
env.git_clone = 'GIT_PATH' # Your git url
env.restart_cmd = 'kill -HUP `supervisorctl pid gunicorn`' # Restart command

