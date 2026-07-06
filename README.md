<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# linkml-ohdsi-gis-extension-envar

A LinkML model of the OHDSI GIS extension

## Documentation Website

[https://monarch-initiative.github.io/linkml-ohdsi-gis-extension-envar](https://monarch-initiative.github.io/linkml-ohdsi-gis-extension-envar)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [linkml_ohdsi_gis_extension_envar](src/linkml_ohdsi_gis_extension_envar)
    * [schema/](src/linkml_ohdsi_gis_extension_envar/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/linkml_ohdsi_gis_extension_envar/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
