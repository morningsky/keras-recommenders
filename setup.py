from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(name='keras-recommenders',  # 包名
      version='0.0.3',  # 版本号
      description='A recommendation system models based Keras',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Mincai lai',
      author_email='757387961@qq.com',
      url='https://github.com/morningsky/keras-recommenders',
      install_requires=['deepctr>=0.8.6', 'tensorflow>=2.3.0'],
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: Apache Software License',
      ],
      license="Apache-2.0",
      keywords=['ctr', 'click through rate', 'deep learning', 'keras', 'tensorflow', 'recommendation', 'deepctr'],
      )