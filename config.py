from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

API_PREFIX = "/api"

config = Config(".env")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default=[""],
)
