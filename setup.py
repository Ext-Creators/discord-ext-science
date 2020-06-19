from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.2.0'

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

# basically install databases if they want it.
extras_require = {
    'databases': 'databases',
}

setup(
    name='discord-ext-science',
    author='NCPlayz',
    python_requires='>=3.7.0',
    url='https://github.com/NCPlayz/discord-ext-science',
    version=version,
    packages=[
        'discord/ext/science',
        'discord/ext/science/recorders',
        ],
    license='MIT',
    description='A simple event logger for discord.py.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
