import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InsightsGG",
    version="0.9.2",
    author="Aud",
    author_email="audaciousxth@gmail.com",
    description="The unofficial api for Insights.gg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thoward02/InsightsGG",
    packages= ["insightsGG", "insightsGG.Errors", "insightsGG.Objects", "insightsGG.Objects.OverwatchAnalytics"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
