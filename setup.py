from distutils.core import setup

setup(
    name="pywordcloud",
    version="0.1",
    author="Shivam Bansal",
    author_email="shivam5992@gmail.com",
    packages=["pywordcloud"],
    include_package_data=True,
    url="https://github.com/shivam5992/pywordcloud",
    license='MIT',
    description="Generate Word Clouds in Python.",
    long_description=open("README.md").read(),
    keywords = ['wordcloud','wordtagcloud','word','tagcloud']
)