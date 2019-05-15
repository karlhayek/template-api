# API Template

Template project for writing API's that run inference on machine learning models in Python. [FastAPI](https://fastapi.tiangolo.com) is the used web framework, and [Cookiecutter](https://github.com/audreyr/cookiecutter) is used to define the template and create projects from it.

The boilerplate project runs a web server API inside a Docker container that listens to HTTP requests and provides documentation for requests to the available endpoints. 

## Quick Start

Install Cookiecutter:

```sh
$ pip install cookiecutter
```

To create a new boilerplate project from the template:

```sh
$ cookiecutter https://github.com/karlhayek/template-api.git
```


#### Short description of what Cookiecutter does.

Cookiecutter is a tool for creating project templates. You can define project-specific names and content of files and folders as placeholders with the {{cookiecutter.variable_name}} syntax, and define all of these variables along with their default values in [cookiecutter.json](cookiecutter.json). When Cookiecutter is run to create a new project from a template, it asks the user to specify the template's variables and then replaces all instances of the variable placeholders with the specified values.

Here the actual API boilerplate project is in the `{{cookiecutter.project_slug}}` directory, and is what Cookiecutter installs when you create a new project from the template.