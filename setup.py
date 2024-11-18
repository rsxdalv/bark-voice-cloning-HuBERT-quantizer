from setuptools import setup

setup(
    name='bark_hubert_quantizer',
    version='0.0.4',
    packages=['bark_hubert_quantizer'],
    install_requires=[
        'audiolm-pytorch>=1.1.4,<1.2.29',
        'fairseq',
        'huggingface-hub',
        'sentencepiece',
        'transformers',
        'encodec',
        'soundfile; platform_system == "Windows"',
        'sox; platform_system != "Windows"'
    ],
)