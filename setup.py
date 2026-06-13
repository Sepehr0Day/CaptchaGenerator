from setuptools import find_packages, setup


setup(
    name="CaptchaGenerator",
    version="2.0.0",
    description="A modular and customizable CAPTCHA generation library.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sepehr0Day",
    url="https://github.com/Sepehr0Day/CaptchaGenerator",
    project_urls={
        "Documentation": "https://github.com/Sepehr0Day/CaptchaGenerator/wiki",
        "Issues": "https://github.com/Sepehr0Day/CaptchaGenerator/issues",
    },
    packages=find_packages(include=("CaptchaGenerator", "CaptchaGenerator.*")),
    python_requires=">=3.11",
    install_requires=["Pillow>=10.0.0"],
    extras_require={
        "audio": ["gTTS>=2.3.2"],
        "telegram": ["telethon>=1.30.0"],
        "dev": ["build", "pytest", "ruff", "mypy"],
    },
    license="MIT",
    keywords=["captcha", "security", "pillow", "accessibility", "image"],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Typing :: Typed",
    ],
)
