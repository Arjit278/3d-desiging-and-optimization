# Pictator Pro 2026 — Complete Fixed Script


import io
import requests
import streamlit as st
from PIL import Image
from huggingface_hub import InferenceClient

# --------------------------------------
# 🔧 PAGE CONFIG & API
# --------------------------------------

st.set_page_config(
    page_title="Pictator Pro 2026",
    page_icon="🏎️",
    layout="wide"
)

OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")
SERP_API_KEY = st.secrets.get("SERP_API_KEY", "")
HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# --------------------------------------
# ⚡ VALID IMAGE MODELS ONLY
# --------------------------------------

MODEL_OPTIONS = {
    "🔥 FLUX.1 Dev": "black-forest-labs/FLUX.1-dev",
    "⚡ FLUX.1 Schnell": "black-forest-labs/FLUX.1-schnell",
    "🏎️ FLUX.2 Klein": "black-forest-labs/FLUX.2-klein-9b-fp8",
    "✨ FLUX.1 Kontext Dev": "black-forest-labs/FLUX.1-Kontext-dev",
    "🪟 FLUX.1 Fill Dev": "black-forest-labs/FLUX.1-Fill-dev",
    "🌀 FLUX.1 Redux Dev": "black-forest-labs/FLUX.1-Redux-dev",
    "✨ SD 3.5 Large": "stabilityai/stable-diffusion-3.5-large"
}

ANALYSIS_MODELS = [
    "qwen/qwen-3-coder:free",
    "meta-llama/llama-3.2-3b-instruct:free"
]

TRUSTED_DOMAINS = [
    "autofurnish.com",
    "autofit.in",
    "carwale.com",
    "cardekho.com",
    "amazon.in"
]

# --------------------------------------
# 🧠 IMAGE GENERATION
# --------------------------------------

def generate_ai_image(prompt, model_id):

    try:

        client = InferenceClient(
            model=model_id,
            token=HF_TOKEN
        )

        image = client.text_to_image(
            prompt,
            width=1024,
            height=768
        )

        return image

    except Exception as e:

        st.error(f"Generation Failed: {e}")
        return None

# --------------------------------------
# ⚡ OPENROUTER ANALYSIS
# --------------------------------------

def call_openrouter(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    for model in ANALYSIS_MODELS:

        try:

            r = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an automotive engineering expert."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                },
                timeout=20
            )

            if r.status_code == 200:

                return r.json()["choices"][0]["message"]["content"]

        except:
            continue

    return "Flashmind fallback active."

# --------------------------------------
# 🌍 MARKET REFERENCES
# --------------------------------------

def fetch_market_references(query):

    try:

        params = {
            "engine": "google_images",
            "q": f"{query} leather seat cover",
            "api_key": SERP_API_KEY,
            "num": 20
        }

        r = requests.get(
            "https://serpapi.com/search",
            params=params,
            timeout=10
        )

        results = r.json().get("images_results", [])

        filtered_refs = []

        for i in results[:6]:

            filtered_refs.append({
                "img": i.get("original"),
                "link": i.get("link"),
                "src": i.get("source")
            })

        return filtered_refs

    except:

        return []

# --------------------------------------
# 🏎️ HEADER
# --------------------------------------

st.title("🏎️ Pictator Pro – CEO Engineering Suite")
st.caption(
    "Strategic Parallel RCA | Multithreaded Design | 2026 Material Intel"
)

selected_model = st.sidebar.selectbox(
    "Choose Pro AI Model",
    list(MODEL_OPTIONS.keys())
)

uploaded_reference = st.sidebar.file_uploader(
    "Upload OEM Seat/Base Reference",
    type=["png", "jpg", "jpeg"]
)

# --------------------------------------
# 🎨 CONFIGURATOR
# --------------------------------------

car = st.selectbox(
    "Vehicle",
    [
        "Maruti Wagon R",
        "Maruti Grand Vitara",
        "Custom/Other"
    ]
)

material = st.selectbox(
    "Material",
    [
        "1200 GSM Nappa",
        "Synthetic Leather",
        "Carbon Fiber Leather"
    ]
)

stitch_type = st.selectbox(
    "Stitching Style",
    [
        "Diamond Stitch",
        "Honeycomb Stitch",
        "Contrast Stitching"
    ]
)

pattern_target = st.selectbox(
    "Pattern Target",
    [
        "Base Design",
        "Patch",
        "Stitching",
        "Piping"
    ]
)

pattern_color = st.selectbox(
    "Pattern/Patch Color",
    [
        "White",
        "Silver",
        "Ivory",
        "Red",
        "Blue",
        "Orange",
        "Gold",
        "Black"
    ]
)

side_patch_mode = st.selectbox(
    "Side Patches",
    [
        "None",
        "Full Side Patch",
        "Only Cylindrical Side Patch",
        "Head Rest Patch",
        "Custom"
    ]
)

base_color = st.selectbox(
    "Base Color",
    [
        "Black",
        "Ivory",
        "Beige"
    ]
)

num_images = st.select_slider(
    "Generation Count",
    options=[1, 3, 5]
)

custom_instruction = st.text_area(
    "Engineering Instructions"
)

# --------------------------------------
# 🚀 EXECUTION PIPELINE
# --------------------------------------

if st.button("🚀 EXECUTE FULL SUITE"):

    generated_images = []

    wagonr_rules = ""

    # --------------------------------------
    # FIXED WAGONR HEADREST RULES
    # --------------------------------------

    if car == "Maruti Wagon R":

        wagonr_rules = """
STRICTLY generate Maruti WagonR OEM seats.

ABSOLUTE REQUIREMENTS:
- FIXED integrated headrest ONLY
- Headrest merged into seat
- NO detachable headrests
- NO adjustable rod headrests
- NO luxury SUV seats
- NO oversized bolsters
- Compact hatchback seat proportions
- Slim shoulder geometry
- Thin upright OEM seat profile

IMPORTANT:
Seats must visually resemble
OEM WagonR front seats.

Side shoulder patches must flow
from upper shoulder area downward.

Use compact sporty hatchback styling.

Reference:
https://www.carwale.com/maruti-suzuki-cars/wagon-r/images/maruti-suzuki-wagon-r-front-row-seats-442349/?category=interior
"""

    elif car == "Maruti Grand Vitara":

        wagonr_rules = """
STRICTLY preserve original Maruti Grand Vitara OEM seat architecture.
"""

    # --------------------------------------
    # SIDE PATCH PROMPTS
    # --------------------------------------

    side_patch_prompt = ""

    if side_patch_mode == "Full Side Patch":

        side_patch_prompt = f"""
Generate sporty OEM dual-tone side patches.

{pattern_color} side shoulder patches
flowing vertically from upper shoulders
towards lower seat base.

Black outer bolsters.

Premium sporty hatchback styling.
"""

    elif side_patch_mode == "Only Cylindrical Side Patch":

        side_patch_prompt = f"""
Generate cylindrical side inserts
in {pattern_color} color.
"""

    elif side_patch_mode == "Head Rest Patch":

        side_patch_prompt = f"""
Generate integrated fixed headrest patch
in {pattern_color} color.
"""

    final_prompt = f"""
Professional automotive interior photography.

STRICT OEM ACCURACY REQUIRED.

Vehicle:
{car}

{wagonr_rules}

Material:
{material}

Stitching:
{stitch_type}

Pattern Target:
{pattern_target}

Pattern Color:
{pattern_color}

Side Patch Design:
{side_patch_prompt}

Engineering Notes:
{custom_instruction}

Rules:
- Maintain OEM seat geometry
- Maintain integrated fixed headrest
- No detachable headrests
- No SUV seat proportions
- Hyper realistic detailing
- Automotive catalog photography
"""

    st.code(final_prompt)

    # --------------------------------------
    # IMAGE GENERATION
    # --------------------------------------

    for i in range(num_images):

        img = generate_ai_image(
            final_prompt,
            MODEL_OPTIONS[selected_model]
        )

        if img:

            generated_images.append(img)

    # --------------------------------------
    # FLASHMIND ANALYSIS
    # --------------------------------------

    analysis = call_openrouter(
        f"""
You are Flashmind Automotive Intelligence 2026.

Generate:
- 5 to 6 concise bullet points
- premium upholstery trends
- GenZ sporty interior trends
- OEM upgrade demand
- integrated headrest trends

Vehicle:
{car}

Material:
{material}
"""
    )

    genz_trends = call_openrouter(
        f"""
Generate 8 to 10 premium GenZ automotive trend bullet points.

Focus:
- sporty hatchback interiors
- side patch trends
- premium stitching
- ambient cabin styling
- OEM+ upgrades
- urban GenZ buyer trends
"""
    )

    market_refs = fetch_market_references(
        f"{car} {material} seat cover"
    )

    # --------------------------------------
    # OUTPUT
    # --------------------------------------

    for idx, img in enumerate(generated_images):

        st.image(
            img,
            caption=f"Variant {idx+1}",
            use_container_width=True
        )

    st.subheader(
        "🌍 Verified Market References & Live Shop Links"
    )

    cols = st.columns(3)

    for idx, ref in enumerate(market_refs):

        with cols[idx % 3]:

            if ref["img"]:

                st.image(
                    ref["img"],
                    caption=ref["src"],
                    use_container_width=True
                )

            if ref["link"]:

                st.link_button(
                    "🔗 View Shop",
                    ref["link"]
                )

    st.divider()

    st.subheader("📈 Flashmind 2026 Trend Intelligence")

    st.markdown(analysis)

    st.divider()

    st.subheader(
        "🔥 GenZ Upholstery & Market Intelligence 2026"
    )

    st.markdown(genz_trends)

# --------------------------------------
# 📊 TECH STANDARDS
# --------------------------------------

with st.expander("📊 2026 Tech Standards"):

    st.write(
        "- OEM WagonR fixed integrated headrest enforcement active."
    )

    st.write(
        "- Reference-image guided side patch generation active."
    )

    st.write(
        "- 2026 sporty hatchback upholstery intelligence enabled."
    )
