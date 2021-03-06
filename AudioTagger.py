{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "AudioTagger",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/QColeman97/AudioTagger/blob/master/AudioTagger.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1r-IRKqSNCF8",
        "colab_type": "code",
        "outputId": "5cfb11c8-f5b2-4f38-c619-af8f6c7bbe7b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BntxWSSKakG2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np \n",
        "import pandas as pd \n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns # for data visualization \n",
        "\n",
        "\n",
        "import IPython.display as ipd #To play sound in notebook\n",
        "import scipy as sci\n",
        "import wave \n",
        "from scipy.io import wavfile \n",
        "\n",
        "import librosa "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OFEZe0wzpLdP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WUp-xuxBUHie",
        "colab_type": "code",
        "outputId": "2b5e59ed-7804-4f6a-8a00-4fa62000876e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "import os \n",
        "print(os.listdir(\"drive/My Drive/CSC490Final-AudioTagger\"))"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['FSDKaggle2018.audio_test']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K7_TeQythJZs",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "audio_test_file = (\"drive/My Drive/CSC490Final-AudioTagger/FSDKaggle2018.audio_test\")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tOT2j9MfiSxD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}