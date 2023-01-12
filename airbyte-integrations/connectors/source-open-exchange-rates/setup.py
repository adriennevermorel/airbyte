#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk~=0.2",
    "pytest~=6.1",
    "pytest-mock~=3.6.1",
    "pendulum==2.1.2",
]

TEST_REQUIREMENTS = [
    "source-acceptance-test",
]

setup(
    name="source_open_exchange_rates",
    description="Source implementation for Open Exchange Rates.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "*.yaml", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
