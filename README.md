# Datarails Examples

This repo contains examples of how you can use Datarails to structure your ETL jobs. It also provides examples of how to build documentaiton
for your ETL jobs using mkdocs and the material theme. Figuring out how to host your documentation is up to you.

## Official Documentation
The official documentation is hosted on github pages at [jesse.maitland.github.io](https://jessemaitland.github.io/datarails/)

## Makefile
There is a makefile in this repo to help with getting started. Just run `make help` to see the available commands.

```bash
help:                   Show help messages and exit.
venv:                   Create local python venv for development
install:                Install project requirements
serve-mkdocs:           Serve mkdocs documentation
jupyter-lab:            Start Jupiter Labs
```

## Using This Project

1. Clone the project
2. Create a virtual environment `make venv`
3. Install the project requirements `make install`
4. Start the jupyter lab server `make jupyter-lab`
5. Start the mkdocs server `make serve-mkdocs`
6. Running examples `cd examples && python example.py`
