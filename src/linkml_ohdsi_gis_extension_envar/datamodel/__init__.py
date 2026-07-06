"""Data model package for linkml-ohdsi-gis-extension-envar."""

from pathlib import Path
from .linkml_ohdsi_gis_extension_envar import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "linkml_ohdsi_gis_extension_envar.yaml"
