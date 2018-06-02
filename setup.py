from setuptools import setup
from setuptools import find_packages


setup(name='cleverhans',
      version='2.0.0',
      url='https://github.com/tensorflow/cleverhans',
      license='MIT',
      install_requires=[
          'nose',
          'pycodestyle',
          'scipy',
          'matplotlib'],
      # Explicit dependence on TensorFlow is not supported.
      # See https://github.com/tensorflow/tensorflow/issues/7166
      extras_require={
        "tf": ["tensorflow>=1.4.1"],
        "tf_gpu": ["tensorflow-gpu>=1.4.1"],
      },
      packages=find_packages())
