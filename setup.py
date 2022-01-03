from setuptools import setup, find_packages

package_name = 'lanenet_model'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    py_modules=[],
    zip_safe=True,
    install_requires=[
        'glog',
        'loguru',
        'tensorflow_gpu==2.7.0',
        'tqdm',
        'matplotlib',
        'opencv_contrib_python',
        'numpy',
        'scikit_learn',
        'tensorflow',
        'PyYAML'
    ],
    author='Giovanni Santos',
    maintainer='Giovanni Santos',
    description='MaybeShewill-CV Lanenet implementation',
    license='Apache License, Version 2.0',
    test_suite='pytest'
)
