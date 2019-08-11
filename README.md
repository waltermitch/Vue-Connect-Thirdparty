# BriteCore Engineering Application

## Steps Taken to auto lint my code

## Python :

- I installed Python extension  for visual studio code.
- Then installed Linter extension.
- Then installed Pep8 extension and made it the default configuration for linter.
- In my custom settings JSON file, i set the key `editor.formatOnSave` to `True`. 

## JavaScript :

- I used Vue CLI 3 to create the project.
- I manually selected features.
- I choose Linter / Formatter.
- For Linter i choose `Prettier`.
- I selected the configuration file should be placed inside my package.json.
- I added the following code to my package.json file :

```
    "prettier": {
    "tabwidth": 4,
    "singleQuote": true
  }
```

- Then i run `npm run lint`.

## Approach

My approach was basic. I hand coded the functionalities that were unique to this project and made use of third party packages for requirements that weren't unique (CORS & Audit Log).

In the project i started with the  backend (Django & PostgreSql) and then went ahead to implement the frontend using VueJS.



## Deployment Method

For my deployment, i made use of 2 Digital Ocean droplets; one for the backend (Django & PostgreSql) and another for the frontend of the app (VueJS).
Both droplets are linux based (Ubuntu 18.0.4) 

The frontend app connects to the backend and pulls all the resources it needs from the backend.
