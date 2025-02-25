import sys

from setuptools import find_packages, setup  # noqa

# from flytekit.tools.lazy_loader import LazyLoadPlugin  # noqa
# extras_require = LazyLoadPlugin.get_extras_require()

MIN_PYTHON_VERSION = (3, 7)
CURRENT_PYTHON = sys.version_info[:2]
if CURRENT_PYTHON == (3, 6):
    print(
        f"Flytekit native typed API is supported for python versions {MIN_PYTHON_VERSION}+, Python 3.6 is supported"
        f" only for legacy Flytekit API. This will be deprecated when Python 3.6 reaches end of life (Dec 23rd, 2021),"
        f" we recommend migrating to the new API"
    )
elif CURRENT_PYTHON < MIN_PYTHON_VERSION:
    print(
        f"Flytekit API is only supported for Python version is {MIN_PYTHON_VERSION}+. Detected you are on"
        f" version {CURRENT_PYTHON}, installation will not proceed!"
    )
    sys.exit(-1)

spark = ["pyspark>=2.4.0,<3.0.0"]
spark3 = ["pyspark>=3.0.0"]
sidecar = ["k8s-proto>=0.0.3,<1.0.0"]
schema = ["numpy>=1.14.0,<2.0.0", "pandas>=0.22.0,<2.0.0", "pyarrow>2.0.0,<4.0.0"]
hive_sensor = ["hmsclient>=0.0.1,<1.0.0"]
notebook = ["papermill>=1.2.0", "nbconvert>=6.0.7", "ipykernel>=5.0.0,<6.0.0"]
sagemaker = ["sagemaker-training>=3.6.2,<4.0.0"]

all_but_spark = sidecar + schema + hive_sensor + notebook + sagemaker

extras_require = {
    "spark": spark,
    "spark3": spark3,
    "sidecar": sidecar,
    "schema": schema,
    "hive_sensor": hive_sensor,
    "notebook": notebook,
    "sagemaker": sagemaker,
    "all-spark2.4": spark + all_but_spark,
    "all": spark3 + all_but_spark,
}

__version__ = "0.0.0+develop"

setup(
    name="flytekit",
    version=__version__,
    maintainer="Flyte Contributors",
    maintainer_email="admin@flyte.org",
    packages=find_packages(exclude=["tests*"]),
    url="https://github.com/flyteorg/flytekit",
    description="Flyte SDK for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "pyflyte-execute=flytekit.bin.entrypoint:execute_task_cmd",
            "pyflyte-fast-execute=flytekit.bin.entrypoint:fast_execute_task_cmd",
            "pyflyte-map-execute=flytekit.bin.entrypoint:map_execute_task_cmd",
            "pyflyte=flytekit.clis.sdk_in_container.pyflyte:main",
            "flyte-cli=flytekit.clis.flyte_cli.main:_flyte_cli",
        ]
    },
    install_requires=[
        "flyteidl>=0.21.0,<0.22.0",
        "wheel>=0.30.0,<1.0.0",
        "pandas>=1.0.0,<2.0.0",
        "pyarrow>=2.0.0,<4.0.0",
        "click>=6.6,<8.0",
        "croniter>=0.3.20,<4.0.0",
        "deprecated>=1.0,<2.0",
        "python-dateutil<=2.8.1,>=2.1",
        "grpcio>=1.3.0,<2.0",
        "protobuf>=3.6.1,<4",
        "python-json-logger>=2.0.0",
        "pytimeparse>=1.1.8,<2.0.0",
        "pytz>=2017.2,<2018.5",
        "keyring>=18.0.1",
        "requests>=2.18.4,<3.0.0",
        "responses>=0.10.7",
        "six>=1.9.0,<2.0.0",
        "sortedcontainers>=1.5.9<3.0.0",
        "statsd>=3.0.0,<4.0.0",
        "urllib3>=1.22,<2.0.0",
        "wrapt>=1.0.0,<2.0.0",
        "retry==0.9.2",
        "dataclasses-json>=0.5.2",
        "marshmallow-jsonschema>=0.12.0",
        "natsort>=7.0.1",
        "dirhash>=0.2.1",
        "docker-image-py>=0.1.10",
        "singledispatchmethod; python_version < '3.8.0'",
        "docstring-parser>=0.9.0",
        "diskcache>=5.2.1",
    ],
    extras_require=extras_require,
    scripts=[
        "flytekit_scripts/flytekit_build_image.sh",
        "flytekit_scripts/flytekit_venv",
        "flytekit_scripts/flytekit_sagemaker_runner.py",
        "flytekit/bin/entrypoint.py",
    ],
    license="apache2",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
