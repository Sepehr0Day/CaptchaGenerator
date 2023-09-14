from setuptools import setup

setup(
    name='CaptchaGenerator',
    version='1.1.6',
    license='MIT',
    description='A library for captcha generator for Telegram bots',
    author='Sepehr0Day',
    author_email='sphrz2324@gmail.com',
    packages=['CaptchaGenerator'],
    install_requires=[
        'Pillow',
        'colorama',
        'gTTS'
    ],
)
