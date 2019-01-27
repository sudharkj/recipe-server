# Bowl2Recipe
Application server for Bowl2Recipe App. 

###### Project set-up

Create an ini file similar to 
[resources/app_config.ini](https://github.com/BOWL2RECIPE/recipe-server/blob/master/resources/app_config.ini) 
outside the project and add the following content.
```text
[EDAMAM_API]
app-id = 1a1a1a1a
app-key = aaaa1111aaaa1111aaaa1111aaaa1111
```
Replace the values (i.e., string to the left side of =) with the actual values.

Create sensitive.ini file similar to 
[resources/app_config.ini](https://github.com/BOWL2RECIPE/recipe-server/blob/master/resources/app_config.ini) 
in resources folder and add the following content.
```text
[SECRET]
keys-file-location = /my_folder_path/bowl-2-recipe.ini
google-keys-file-location = /my_folder_path/google-keys-file-name.json
```

Replace the value of `google-keys-file-location` with the absolute path of the file containing google keys. 
Refer to [Using a service account](https://cloud.google.com/vision/docs/auth#using_a_service_account) 
to download the key file.

Also, replace the value of `keys-file-location` under `[SECRET]` section in 
[resources/config.ini](https://github.com/sudharkj/recipe-server/blob/master/config/config.ini) 
with the absolute path of this file.

###### Install Dependencies
Make sure that the conda channel is conda-forge.
```text
conda config --add channels conda-forge
```
Run the following command to install the dependencies.
```text
conda install requirements.txt
```

###### Starting Server
Run the following command to start the server in default mode
```text
$ flask run
```

Application environment and debug mode can be set using `FLASK_ENV` and `FLASK_DEBUG` variables respectively.
```text
$ FLASK_ENV=development FLASK_DEBUG=1 flask run
```
The above command start the server in development environment with debug mode on.