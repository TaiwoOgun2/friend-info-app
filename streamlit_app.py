{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyN0R4t7qy4v0z+YhdbG5cpU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TaiwoOgun2/friend-info-app/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8pId6Ww-bCvq",
        "outputId": "67cc0f04-2159-4c95-f5a4-056e2437e23c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🎉 Welcome to the Friend Info App!\n",
            "\n",
            "👤 What's your friend's name? unique\n",
            "📅 Age: 22\n",
            "📏 Height (e.g., 5.9 ft or 180 cm): 5'9\n",
            "🎨 Hobby: basketball\n",
            "❤ What does your friend like most? snapchat\n",
            "💪 What is their biggest strength? big yansh\n",
            "💍 Relationship status (Single/Married): in btw\n",
            "\n",
            "📋 Summary about your friend:\n",
            "\n",
            "🧑 Name: unique\n",
            "📅 Age: 22\n",
            "📏 Height: 5'9\n",
            "🎨 Hobby: basketball\n",
            "❤ Loves: snapchat\n",
            "💪 Strength: big yansh\n",
            "💍 Relationship Status: in btw\n",
            "\n",
            "Thanks for sharing, you're a good friend to unique! 😊\n"
          ]
        }
      ],
      "source": [
        "def talk_to_friend():\n",
        "    print(\"🎉 Welcome to the Friend Info App!\\n\")\n",
        "\n",
        "    name = input(\"👤 What's your friend's name? \")\n",
        "    age = input(\"📅 Age: \")\n",
        "    height = input(\"📏 Height (e.g., 5.9 ft or 180 cm): \")\n",
        "    hobby = input(\"🎨 Hobby: \")\n",
        "    favourite = input(\"❤ What does your friend like most? \")\n",
        "    strength = input(\"💪 What is their biggest strength? \")\n",
        "    status = input(\"💍 Relationship status (Single/Married): \")\n",
        "\n",
        "    print(\"\\n📋 Summary about your friend:\\n\")\n",
        "    print(f\"🧑 Name: {name}\")\n",
        "    print(f\"📅 Age: {age}\")\n",
        "    print(f\"📏 Height: {height}\")\n",
        "    print(f\"🎨 Hobby: {hobby}\")\n",
        "    print(f\"❤ Loves: {favourite}\")\n",
        "    print(f\"💪 Strength: {strength}\")\n",
        "    print(f\"💍 Relationship Status: {status}\")\n",
        "\n",
        "    print(f\"\\nThanks for sharing, you're a good friend to {name}! 😊\")\n",
        "\n",
        "# Run the app\n",
        "talk_to_friend()"
      ]
    }
  ]
}