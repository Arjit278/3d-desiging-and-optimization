# =========================================================
# PICTATOR PRO 2026 — ULTIMATE FLASHMIND EDITION
# =========================================================

import io
import requests
import streamlit as st
from huggingface_hub import InferenceClient

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Pictator Pro 2026",
    page_icon="🏎️",
    layout="wide"
)

HF_TOKEN = st.secrets.get("HF_TOKEN", "")
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")
SERP_API_KEY = st.secrets.get("SERP_API_KEY", "")

# =========================================================
# FLASHMIND MODELS
# =========================================================

ANALYSIS_MODELS = [
    "qwen/qwen-3-coder:free",
    "meta-llama/llama-3.2-3b-instruct:free",
    "nousresearch/hermes-2-pro-llama-3-8b"
]

# =========================================================
# TRUSTED DOMAINS
# =========================================================

TRUSTED_DOMAINS = [
    "autofurnish.com",
    "autofit.in",
    "coverking.com",
    "katzkin.com",
    "cardekho.com",
    "carwale.com",
    "amazon.in"
]

# =========================================================
# MODELS
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
st.caption("Advanced OEM Seat Intelligence + Flashmind Trend Engineering")

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
    # 🎨 COLOR CONTROL + REFERENCE FEED
    # =========================================================
    
    color_control_mode = st.toggle(
        "Color Control Mode",
        value=True
    )
    
    color_choices = {
        1: ["Silver"],
        3: ["Silver", "Blue", "Red"],
        5: ["Silver", "Orange", "Blue", "Red", "Gold"]
    }
    
    manual_color = st.selectbox(
        "Select Palette",
        color_choices.get(num_images)
    )
    
    # =========================================================
    # 🌍 URL / IMAGE FEED ENGINE
    # =========================================================
    
    reference_mode = st.toggle(
        "Reference Feed Mode",
        value=True
    )
    
    reference_url = ""
    
    if reference_mode:
    
        reference_url = st.text_input(
            "Paste OEM / Market Reference URL",
            placeholder="https://..."
        )
    
        st.caption(
            "Supports marketplace links, OEM photos, Pinterest, Google Images etc."
        )
    
    # =========================================================
    # 🪑 STRICT SEAT LOCK ENGINE
    # =========================================================
    
    seat_mode = "Single Front Seat"
    
    if (
        single_seat_toggle
        and not double_seat_toggle
        and not four_seat_toggle
    ):
    
        seat_mode = "Single Front Seat"
    
    elif (
        double_seat_toggle
        and not four_seat_toggle
    ):
    
        seat_mode = "Dual Front Seats"
    
    elif four_seat_toggle:
    
        seat_mode = "Full 4 Seat Set"
    
    # =========================================================
    # 🔒 WAGONR HARD LOCK
    # =========================================================
    
    wagonr_fixed_prompt = ""
    
    if car == "Maruti Wagon R":
    
        wagonr_fixed_prompt = """
        STRICT ENFORCEMENT:
        - WagonR compact hatchback geometry
        - fixed integrated headrest mandatory
        - prohibit detachable headrests
        - prohibit luxury sofa geometry
        - compact upright OEM seating
        """
    
        if seat_mode == "Single Front Seat":
    
            wagonr_fixed_prompt += """
            Generate ONLY ONE front seat.
            """
    
        elif seat_mode == "Dual Front Seats":
    
            wagonr_fixed_prompt += """
            Generate ONLY TWO front seats.
            """
    
        elif seat_mode == "Full 4 Seat Set":
    
            wagonr_fixed_prompt += """
            Generate COMPLETE 4-seat WagonR layout.
            """
    
    # =========================================================
    # 🏔️ GRAND VITARA LOCK
    # =========================================================
    
    grand_vitara_prompt = ""
    
    if car == "Maruti Grand Vitara":
    
        grand_vitara_prompt = """
        STRICT ENFORCEMENT:
        - premium SUV seat geometry
        - integrated SUV headrests
        - wider premium shoulder contours
        - realistic Grand Vitara spacing
        """
    
    # =========================================================
    # 🎨 ADD INSIDE FINAL PROMPT
    # =========================================================
    
    final_prompt += f"""
    
    Selected Palette:
    {manual_color}
    
    Reference URL:
    {reference_url}
    
    Vehicle Lock:
    {wagonr_fixed_prompt}
    {grand_vitara_prompt}
    
    Critical Rules:
    - obey exact seat count
    - obey exact vehicle geometry
    - maintain OEM realism
    - maintain hatchback proportions
    - maintain SUV proportions
    """


# =========================================================
# THREAD / PIPING
# =========================================================

st.markdown("### 🧵 Piping / Threading / Custom Tuning")

thread_cols = st.columns(4)

with thread_cols[0]:

    piping_toggle = st.toggle(
        "Piping",
        value=True
    )

with thread_cols[1]:

    threading_toggle = st.toggle(
        "Threading",
        value=True
    )

with thread_cols[2]:

    custom_color_toggle = st.toggle(
        "Custom Color Tune",
        value=True
    )

with thread_cols[3]:

    sporty_finish_toggle = st.toggle(
        "Sport Finish"
    )

thread_colors = st.multiselect(
    "Thread / Piping Colors",
    [
        "Red",
        "Silver",
        "Gold",
        "Blue",
        "Peach",
        "Sky Blue",
        "Black",
        "White",
        "Cream",
        "Orange",
        "Magenta"
    ],
    default=["Red", "Silver"]
)

thread_pattern = st.selectbox(
    "Thread Pattern",
    [
        "Contrast OEM",
        "Luxury Flow",
        "GT Sport",
        "Diamond Highlight",
        "Premium Executive"
    ]
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
# HEADREST LOGIC
# =========================================================

if car == "Maruti Wagon R":

    st.toggle(
        "🔒 WagonR Fixed Headrest",
        value=True,
        disabled=True
    )

else:

    st.toggle(
        "🏔️ Grand Vitara SUV Seats",
        value=True,
        disabled=True
    )

# =========================================================
# PATCH ENGINEERING
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
    default=["Silver"]
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
        "Smooth Leather",
        "Carbon Texture",
        "Alcantara Style"
    ]
)

# =========================================================
# FLASHMIND BOX
# =========================================================

st.markdown("## 📈 Flashmind Trend Intelligence")

trend_toggle = st.toggle(
    "Enable Flashmind Analysis",
    value=True
)

engineering_notes = st.text_area(
    "✍️ Engineering Instructions",
    value="Share good designs as per above settings with fixed seat head rests",
    height=140
)

# =========================================================
# OPENROUTER
# =========================================================

def call_openrouter(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    for model in ANALYSIS_MODELS:

        try:

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an automotive upholstery market intelligence expert."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                },
                timeout=20
            )

            if response.status_code == 200:

                data = response.json()

                return data["choices"][0]["message"]["content"]

        except:
            continue

    return "Flashmind fallback active."

# =========================================================
# SERP MARKET REFERENCES
# =========================================================

def fetch_market_references(query):

    try:

        params = {
            "engine": "google_images",
            "q": f"{query} leather seat cover",
            "api_key": SERP_API_KEY,
            "num": 20
        }

        response = requests.get(
            "https://serpapi.com/search",
            params=params,
            timeout=15
        )

        data = response.json()

        results = data.get("images_results", [])

        final_refs = []

        for item in results:

            link = item.get("link", "").lower()

            if any(td in link for td in TRUSTED_DOMAINS):

                final_refs.append({
                    "img": item["original"],
                    "link": item["link"],
                    "src": item.get("source", "Market")
                })

            if len(final_refs) >= 6:
                break

        return final_refs

    except Exception as e:

        st.error(f"SERP Error: {e}")

        return []

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
    # THREAD ENGINE
    # =====================================================

    thread_prompt = ""

    if piping_toggle:

        thread_prompt += f"""
        Premium piping enabled.
        Piping Colors:
        {", ".join(thread_colors)}
        """

    if threading_toggle:

        thread_prompt += f"""
        Decorative threading enabled.
        Thread Pattern:
        {thread_pattern}
        """

    if custom_color_toggle:

        thread_prompt += """
        Custom dual-tone color tuning enabled.
        """

    if sporty_finish_toggle:

        thread_prompt += """
        Sport finish styling enabled.
        """

    # =====================================================
    # SEAT LOGIC
    # =====================================================

    if car == "Maruti Wagon R":

        if seat_mode == "Single Front Seat":

            seat_prompt = """
            STRICT WagonR single seat generation.
            ONLY ONE seat.
            Fixed integrated headrest mandatory.
            Compact hatchback geometry.
            """

        elif seat_mode == "Dual Front Seats":

            seat_prompt = """
            STRICT WagonR dual seat generation.
            ONLY TWO seats.
            Fixed integrated headrests mandatory.
            """

        else:

            seat_prompt = """
            STRICT WagonR 4-seat layout.
            Front seats fixed integrated headrests.
            Rear compact hatchback bench.
            """

    else:

        if seat_mode == "Single Front Seat":

            seat_prompt = """
            STRICT Grand Vitara SUV single seat.
            Premium SUV seat geometry.
            Integrated SUV headrest.
            """

        elif seat_mode == "Dual Front Seats":

            seat_prompt = """
            STRICT Grand Vitara dual seat generation.
            Premium SUV contours.
            Integrated SUV headrests.
            """

        else:

            seat_prompt = """
            STRICT Grand Vitara full seat layout.
            Premium SUV front & rear seats.
            Integrated SUV headrests.
            """

    # =====================================================
    # FINAL PROMPT
    # =====================================================

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

    Thread / Piping:
    {thread_prompt}

    Instructions:
    {engineering_notes}

    Selected Palette: {manual_color} 
    
    Reference URL: {reference_url} 
    
    Vehicle Lock: 
    {wagonr_fixed_prompt} 
    {grand_vitara_prompt} 
    
    Critical Rules: 
    - obey exact seat count 
    - obey exact vehicle geometry 
    - maintain OEM realism 
    - maintain hatchback proportions 
    - maintain SUV proportions 
    """

    Rules:
    - hyper realistic upholstery
    - premium piping
    - premium threading
    - OEM seat geometry
    - no floating cushions
    - no detachable headrests
    - realistic hatchback ergonomics
    - realistic SUV ergonomics
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
    # FLASHMIND ANALYSIS
    # =====================================================

    if trend_toggle:

        st.write("📊 Running Flashmind Analysis...")

        trend_result = call_openrouter(
            f"""
            Analyze latest 2026 automotive upholstery trends.

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

            Patch Texture:
            {patch_texture}

            Patch Colors:
            {", ".join(patch_colors)}

            Thread Colors:
            {", ".join(thread_colors)}

            Engineering Notes:
            {engineering_notes}

            Generate:
            - concise bullet points
            - latest market trends
            - GenZ trends
            - luxury trends
            - sporty hatchback trends
            - premium SUV trends
            - recommended color combinations
            - premium piping recommendations
            """
        )

        st.subheader("📈 Flashmind Market Intelligence")

        st.text_area(
            "Flashmind Analysis",
            value=trend_result,
            height=320
        )

    # =====================================================
    # MARKET REFERENCES
    # =====================================================

    market_refs = fetch_market_references(
        f"{car} {material} seat cover"
    )

    st.subheader("🌍 Live Market Trends & Web References")

    if market_refs:

        ref_cols = st.columns(3)

        for idx, ref in enumerate(market_refs):

            with ref_cols[idx % 3]:

                st.image(
                    ref["img"],
                    caption=f"Trend: {ref['src']}",
                    use_container_width=True
                )

                st.link_button(
                    f"🔗 Open {ref['src']}",
                    ref["link"]
                )

# =========================================================
# TECH STANDARDS
# =========================================================

with st.expander("📊 2026 Tech Standards"):

    st.write("- WagonR fixed headrest logic enabled.")
    st.write("- Grand Vitara SUV seat logic enabled.")
    st.write("- Single / Double / 4-seat generation enabled.")
    st.write("- Threading & piping intelligence enabled.")
    st.write("- Flashmind trend analysis enabled.")
    st.write("- SERP market references enabled.")
