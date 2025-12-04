#!/usr/bin/env python
# coding: utf-8
"""Product data analysis and category translation using Ollama."""

import json
import subprocess

import pandas as pd
import requests

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3:8b"


def list_models() -> list:
    """List all available models installed locally."""
    response = requests.get(f"{OLLAMA_URL}/api/tags")
    return [model["name"] for model in response.json()["models"]]


def simple_chat(prompt: str) -> str:
    """Send a simple prompt and get a response."""
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def ollama_run(prompt, model="llama3"):
    """Send a prompt to Ollama and return the text output."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()


def explore_data(df):
    """Print basic data exploration info."""
    print("First 10 rows:")
    print(df.head(10))
    
    print(f"\nFirst product category: {df.loc[0, 'product_category_name']}")
    
    print("\nLast 10 rows:")
    print(df.tail(10))
    
    print("\nDataFrame info:")
    df.info()
    
    print(f"\nShape: {df.shape}")
    
    print("\nNull values per column:")
    print(df.isnull().sum())
    
    print(f"\nDuplicate rows: {df.duplicated().sum()}")
    
    num_unique = df['product_id'].nunique()
    print(f"Number of unique product_id: {num_unique}")


def translate_categories(df):
    """Translate Portuguese category names to English using Ollama."""
    categories_pt = (
        df['product_category_name']
        .dropna()
        .unique()
        .tolist()
    )

    prompt = f"""
Translate the following Portuguese product category names into English.
Return ONLY a JSON list of translations, in the exact same order.
Do NOT include explanations. Only output valid JSON.

Portuguese list:
{json.dumps(categories_pt, ensure_ascii=False)}
"""

    response = ollama_run(prompt)
    categories_en = json.loads(response)
    translation_map = dict(zip(categories_pt, categories_en))
    
    df['product_category_name_english'] = df['product_category_name'].map(translation_map)
    return df


def main():
    # Load dataset
    df_products = pd.read_csv('./data/brazilian_e-commerce/olist_products_dataset.csv')
    
    # Explore data
    explore_data(df_products)
    
    # Check Ollama connection
    print("\n" + "=" * 50)
    print("OLLAMA INTERACTION EXAMPLES")
    print("=" * 50)
    
    try:
        models = list_models()
        print(f"\n✅ Ollama is running!")
        print(f"📦 Available models: {models}\n")
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to Ollama. Start it with: ollama serve")
        return
    
    # Simple translation example
    print("\n--- Example 1: Simple Chat ---")
    response = simple_chat(f"translate {df_products.loc[0, 'product_category_name']} into english")
    print(f"Response: {response}\n")
    
    # Batch translate all categories
    df_products = translate_categories(df_products)
    print("\nTranslated categories:")
    print(df_products.head())
    
    # Save translated data to CSV
    output_path = './data/brazilian_e-commerce/products_translated.csv'
    df_products.to_csv(output_path, index=False)
    print(f"\n✅ Translated data saved to: {output_path}")


if __name__ == "__main__":
    main()
