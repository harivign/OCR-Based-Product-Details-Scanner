
import streamlit as st
from PIL import Image
import easyocr
import requests
import numpy as np

st.title("🧾 OCR-Based Product Details Scanner")

uploaded_file = st.file_uploader("Upload an image of a product", type=["jpg", "jpeg", "png"])

# Extract text from image
def extract_text_from_image(uploaded_image):
    reader = easyocr.Reader(['en'], gpu=False)
    image = Image.open(uploaded_file).convert('RGB')
    image_np = np.array(image)
    result = reader.readtext(image_np)
    filtered_text = [
        text for (_, text, confidence) in result
        if confidence > 0.5 and text.isalpha() and len(text) > 2
    ]
    return " ".join(filtered_text)

# Fetch product details without timeout restriction
def fetch_product_details(query):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.text.strip() == "":
            st.warning("⚠️ API returned empty response.")
            return None
        data = response.json()

        if data.get("count", 0) > 0:
            product = data["products"][0]
            ingredients = product.get("ingredients_text_en") or "N/A"
            raw_categories = product.get("categories_tags", [])
            english_categories = [
                cat.split(":")[-1].replace("-", " ").title()
                for cat in raw_categories if cat.startswith("en:")
            ]
            return {
                "Product Name": product.get("product_name", "N/A"),
                "Ingredients": ingredients,
                "Nutrition Facts": product.get("nutriments", {}),
                "Brand": product.get("brands", "N/A"),
                "Categories": english_categories
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Network/API Error: {e}")
        return None
    except ValueError:
        st.error("⚠️ API did not return valid JSON.")
        return None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_from_image(uploaded_file)
        st.write("**Extracted Text:**", extracted_text)

    with st.spinner("🔎 Searching Open Food Facts..."):
        details = fetch_product_details(extracted_text)
        if details:
            st.subheader("📦 Product Details")
            st.write(f"**Product Name:** {details['Product Name']}")
            st.write(f"**Brand:** {details['Brand']}")
            if details['Categories']:
                st.write("**Categories:**", ", ".join(details['Categories']))
            else:
                st.write("**Categories:** Not available")
            st.write("**Ingredients (English Only):**")
            st.write(details["Ingredients"])

            # Nutrition Facts
            st.write("### 📊 Nutrition Facts (per 100g):")
            nutrients = details["Nutrition Facts"]
            important_keys = {
                "energy-kcal_100g": "Calories (kcal)",
                "fat_100g": "Fat (g)",
                "saturated-fat_100g": "Saturated Fat (g)",
                "carbohydrates_100g": "Carbohydrates (g)",
                "sugars_100g": "Sugars (g)",
                "proteins_100g": "Protein (g)",
                "salt_100g": "Salt (g)",
                "sodium_100g": "Sodium (g)"
            }
            for key, label in important_keys.items():
                if key in nutrients and isinstance(nutrients[key], (int, float)):
                    st.write(f"**{label}:** {nutrients[key]}")
        else:
            st.warning("No matching product found.")



# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #d4f4dd;  /* light green shade */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
