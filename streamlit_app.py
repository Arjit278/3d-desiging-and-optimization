import io
import requests
import streamlit as st
from huggingface_hub import InferenceClient

# =========================================================
# PICTATOR PRO 2026 — FINAL INTEGRATED VERSION
# =========================================================

st.set_page_config(
    page_title="Pictator Pro 2026",
    page_icon="🏎️",
    layout="wide"
)

HF_TOKEN = st.secrets.get("HF_TOKEN", "")
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")

# =========================================================
# SAFE WORKING MODELS
# =========================================================

MODEL_OPTIONS = {
    "⚡ FLUX Schnell": "black-forest-labs/FLUX.1-schnell",
    "🔥 FLUX Dev": "black-forest-labs/FLUX.1-dev",
    "✨ SDXL Base": "stabilityai/stable-diffusion-xl-base-1.0",
    "🌀 SD 1.5": "runwayml/stable-diffusion-v1-5"
}

# =========================================================
# HEADER
# =========================================================

st.title("🏎️ Pictator Pro – CEO Engineering Suite")
st.caption("Advanced OEM Seat Intelligence + 2026 Trend Engineering")

# =========================================================
# SIDEBAR
# =========================================================

selected_model = st.sidebar.selectbox(
    "Choose AI Model",
    list(MODEL_OPTIONS.keys())
)

uploaded_reference = st.sidebar.file_uploader(
    "Upload OEM Seat Reference",
    type=["png", "jpg", "jpeg"]
)

# =========================================================
# MAIN CONFIG
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    car = st.selectbox(
        "Vehicle",
        [
            "Maruti Wagon R",
            "Maruti Grand Vitara"
        ]
    )

    stitching = st.selectbox(
        "Stitching",
        [
            "Diamond Stitch",
            "Honeycomb Stitch",
            "Contrast Stitching",
            "Tuck and Roll",
            "Double Decorative"
        ]
    )

with col2:

    material = st.selectbox(
        "Material",
        [
            "Synthetic Leather",
            "1200 GSM Nappa",
            "Carbon Fiber Leather"
        ]
    )

    base_color = st.selectbox(
        "Base Color",
        [
            "Black",
            "Beige",
            "Cream",
            "Ivory",
            "Tan",
            "Charcoal"
        ]
    )

with col3:

    num_images = st.select_slider(
        "Generation Count",
        options=[1, 3, 5]
    )

# =========================================================
# SEAT TOGGLES
# =========================================================

st.markdown("## 🪑 Seat Generation Layout")

seat_cols = st.columns(3)

with seat_cols[0]:

    single_seat_toggle = st.toggle(
        "Single Seat",
        value=True
    )

with seat_cols[1]:

    double_seat_toggle = st.toggle(
        "Double Seat"
    )

with seat_cols[2]:

    four_seat_toggle = st.toggle(
        "4 Seats"
    )

seat_mode = "Single Front Seat"

if double_seat_toggle:
    seat_mode = "Dual Front Seats"

if four_seat_toggle:
    seat_mode = "Full 4 Seat Set"

# =========================================================
# VEHICLE HEADREST LOCKS
# =========================================================

vehicle_cols = st.columns(2)

with vehicle_cols[0]:

    if car == "Maruti Wagon R":

        st.toggle(
            "🔒 WagonR Fixed Headrest",
            value=True,
            disabled=True
        )

with vehicle_cols[1]:

    if car == "Maruti Grand Vitara":

        st.toggle(
            "🏔️ Grand Vitara SUV Seats",
            value=True,
            disabled=True
        )

# =========================================================
# PATCH TOGGLES
# =========================================================

st.markdown("## 🎨 Side Patch Engineering")

patch_cols = st.columns(4)

with patch_cols[0]:

    seat_back_patch = st.toggle(
        "Seat Back Patch",
        value=True
    )

with patch_cols[1]:

    full_side_patch = st.toggle(
        "Full Side Patch"
    )

with patch_cols[2]:

    shoulder_patch = st.toggle(
        "Shoulder Patch"
    )

with patch_cols[3]:

    headrest_patch = st.toggle(
        "Headrest Patch"
    )

patch_colors = st.multiselect(
    "Patch Colors",
    [
        "Silver",
        "White",
        "Beige",
        "Cream",
        "Sky Blue",
        "Magenta",
        "Red",
        "Blue",
        "Black",
        "Orange",
        "Gold"
    ],
    default=["Silver", "Sky Blue"]
)

patch_style = st.selectbox(
    "Patch Style",
    [
        "OEM Sport",
        "Luxury Flow",
        "Floating Accent",
        "Dual Tone OEM+",
        "Performance GT",
        "Urban GenZ"
    ]
)

patch_texture = st.selectbox(
    "Patch Texture",
    [
        "Alcantara Style",
        "Smooth Leather",
        "Carbon Texture"
    ]
)

# =========================================================
# OPENROUTER ANALYSIS
# =========================================================

st.markdown("## 📈 OpenRouter Trend Intelligence")

trend_toggle = st.toggle(
    "Enable Trend Analysis",
    value=True
)

engineering_notes = st.text_area(
    "✍️ Engineering Instructions",
    value="Share good designs as per above settings with fixed seat head rests",
    height=120
)

# =========================================================
# OPENROUTER FUNCTION
# =========================================================

def call_openrouter(prompt):

    if not OPENROUTER_API_KEY:
        return "Missing OPENROUTER_API_KEY"

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.2-3b-instruct",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            },
            timeout=30
        )

        if response.status_code == 200:

            data = response.json()

            return data["choices"][0]["message"]["content"]

        return f"OpenRouter Error: {response.status_code}"

    except Exception as e:

        return str(e)

# =========================================================
# IMAGE GENERATION
# =========================================================

def generate_image(prompt, model_id):

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

# =========================================================
# EXECUTE
# =========================================================

if st.button("🚀 EXECUTE FULL SUITE"):

    active_patches = []

    if seat_back_patch:
        active_patches.append("Seat Back Patch")

    if full_side_patch:
        active_patches.append("Full Side Patch")

    if shoulder_patch:
        active_patches.append("Shoulder Patch")

    if headrest_patch:
        active_patches.append("Headrest Patch")

    # =====================================================
    # VEHICLE PROMPT LOGIC
    # =====================================================

    if car == "Maruti Wagon R":

        if seat_mode == "Single Front Seat":

            seat_prompt = """
            Generate ONE OEM WagonR front seat.
            Fixed integrated headrest mandatory.
            Compact hatchback geometry.
            """

        elif seat_mode == "Dual Front Seats":

            seat_prompt = """
            Generate TWO WagonR front seats.
            Fixed integrated headrests mandatory.
            Compact hatchback layout.
            """

        else:

            seat_prompt = """
            Generate FULL 4-seat WagonR layout.
            Front seats fixed integrated headrests.
            Compact realistic WagonR cabin spacing.
            """

    else:

        if seat_mode == "Single Front Seat":

            seat_prompt = """
            Generate ONE premium Grand Vitara SUV front seat.
            Integrated SUV headrest.
            Wide premium contours.
            """

        elif seat_mode == "Dual Front Seats":

            seat_prompt = """
            Generate TWO premium Grand Vitara front seats.
            Integrated SUV headrests.
            Premium SUV geometry.
            """

        else:

            seat_prompt = """
            Generate FULL Grand Vitara SUV seat layout.
            Premium front and rear seats.
            Integrated SUV headrests.
            """

    final_prompt = f"""
    Professional automotive seat cover design.

    Vehicle:
    {car}

    Seat Mode:
    {seat_mode}

    {seat_prompt}

    Material:
    {material}

    Stitching:
    {stitching}

    Base Color:
    {base_color}

    Patch Style:
    {patch_style}

    Patch Texture:
    {patch_texture}

    Patch Colors:
    {", ".join(patch_colors)}

    Active Patches:
    {", ".join(active_patches)}

    Instructions:
    {engineering_notes}

    Rules:
    - realistic OEM geometry
    - integrated headrests
    - sporty hatchback realism
    - premium SUV realism
    - hyper realistic texture
    - automotive studio lighting
    - 8k rendering
    """

    st.write(f"⚡ Generating {seat_mode} Designs...")

    generated = []

    for i in range(num_images):

        image = generate_image(
            final_prompt,
            MODEL_OPTIONS[selected_model]
        )

        if image:

            generated.append(image)

    # =====================================================
    # IMAGE OUTPUT
    # =====================================================

    if generated:

        st.subheader(f"🎨 Generated Output — {seat_mode}")

        for idx, img in enumerate(generated):

            st.image(
                img,
                caption=f"{seat_mode} Variant {idx+1}",
                use_container_width=True
            )

            buf = io.BytesIO()
            img.save(buf, format="PNG")

            st.download_button(
                f"💾 Download Variant {idx+1}",
                buf.getvalue(),
                f"variant_{idx+1}.png",
                key=f"download_{idx}"
            )

    # =====================================================
    # TREND ANALYSIS
    # =====================================================

    if trend_toggle:

        st.write("📊 Running OpenRouter Trend Analysis...")

        trend_result = call_openrouter(
            f"""
            Generate concise bullet points for:

            Vehicle:
            {car}

            Seat Mode:
            {seat_mode}

            Material:
            {material}

            Stitching:
            {stitching}

            Patch Style:
            {patch_style}

            Focus:
            - GenZ upholstery trends
            - sporty hatchback interiors
            - integrated headrest styling
            - OEM+ modifications
            - premium side patch trends
            """
        )

        st.subheader("📈 2026 Upholstery Trend Intelligence")

        st.text_area(
            "Trend Analysis",
            value=trend_result,
            height=300
        )

# =========================================================
# TECH STANDARDS
# =========================================================

with st.expander("📊 2026 Tech Standards"):

    st.write("- WagonR fixed headrest logic enabled.")
    st.write("- Grand Vitara SUV seat logic enabled.")
    st.write("- Single / Double / 4-seat generation enabled.")
    st.write("- Horizontal patch toggles enabled.")
    st.write("- OpenRouter trend analysis enabled.")
    st.write("- OEM geometry preservation enabled.")
