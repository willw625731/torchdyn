import setuptools

setuptools.setup(
    name="torchdyn",
    version="0.2.0",
    author="DiffEqML",
    author_email="polimic03@gmail.com, massaroli@robot.t.u-tokyo.ac.jp",
    description="PyTorch package for all things neural differential equations",
    url="https://github.com/DiffEqML/torchdyn",
    packages=setuptools.find_packages(),
    install_requires=['torch',
                      'pytorch-lightning>=0.8.4',
                      'dgl>=0.4.1',
                      'torchdiffeq',
                      'torchsde',
                      'matplotlib',
                      'torchvision',
                      'scikit-learn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
