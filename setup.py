from setuptools import setup

setup(
    name='bark_voice_clone',
    version='0.0.1',
    # description='Your package description',
    # author='Your Name',
    # author_email='your@email.com',
    packages=['hubert'],
    install_requires=[
        # 'audiolm-pytorch',
        # 'fairseq',
        'huggingface-hub',
        'sentencepiece',
        'transformers',
        'encodec',
        'soundfile; platform_system == "Windows"',
        'sox; platform_system != "Windows"'
    ],
)