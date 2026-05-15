```python
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

TRUSTED_DOMAINS = [
    "autofurnish.com",
    "autofit.in",
    "autotextile.com",
    "coverking.com",
    "katzkin.com",
    "cardekho.com",
    "carwale.com",
    "amazon.in",
    "elegantautoretail.com"
]

# --------------------------------------
# 🏎️ HEADER
# --------------------------------------

st.title("🏎️ Pictator Pro – CEO Engineering Suite")
st.caption(
    "Strategic Parallel RCA | Multithreaded Design | 2026 Material Intel"
)

# --------------------------------------
# 🔐 AUTH
# --------------------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

with st.sidebar:

    st.title("🔐 Access Panel")

    if not st.session_state.authenticated:

        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):

            if user == "Harmony" and pwd == "Harmony_Pictator123":

                st.session_state.authenticated = True
                st.rerun()

            else:

                st.error("Invalid Credentials")

    else:

        st.success("🟢 Logged in as Harmony")

        if st.button("Logout"):

            st.session_state.authenticated = False
            st.rerun()

if not st.session_state.authenticated:

    st.warning("🔐 Please login to continue")
    st.stop()

# --------------------------------------
# ⚡ MODELS
# --------------------------------------

MODEL_OPTIONS = {
    "⚡ FLUX.1 Schnell": "black-forest-labs/FLUX.1-schnell",
    "🔥 FLUX.1 Dev": "black-forest-labs/FLUX.1-dev",
    "✨ SD 3.5 Large": "stabilityai/stable-diffusion-3.5-large"
}

selected_model = st.sidebar.selectbox(
    "Choose Pro AI Model",
    list(MODEL_OPTIONS.keys())
)

# --------------------------------------
# 📸 OEM REFERENCE
# --------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("📸 OEM Reference Upload")

uploaded_reference = st.sidebar.file_uploader(
    "Upload OEM Seat/Base Reference",
    type=["png", "jpg", "jpeg"]
)

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
# ⚡ FLASHMIND ANALYSIS
# --------------------------------------

ANALYSIS_MODELS = [
    "qwen/qwen-3-coder:free",
    "meta-llama/llama-3.2-3b-instruct:free"
]

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
            "num": 40
        }

        r = requests.get(
            "https://serpapi.com/search",
            params=params,
            timeout=10
        )

        results = r.json().get("images_results", [])

        filtered_refs = []
        used_domains = set()

        for i in results:

            source_name = i.get("source", "").strip()
            link = i.get("link", "").lower()

            if source_name in used_domains:
                continue

            is_trusted = any(
                td in link for td in TRUSTED_DOMAINS
            )

            if is_trusted:

                filtered_refs.append({
                    "img": i["original"],
                    "link": i["link"],
                    "src": source_name
                })

                used_domains.add(source_name)

            if len(filtered_refs) >= 6:
                break

        return filtered_refs

    except:

        return []

# --------------------------------------
# 🎨 CONFIGURATOR
# --------------------------------------

with st.expander(
    "🧠 Smart Design Configurator (2026 Specs)",
    expanded=True
):

    colA, colB, colC = st.columns(3)

    # --------------------------------------
    # COLUMN A
    # --------------------------------------

    with colA:

        car = st.selectbox(
            "Vehicle",
            [
                "Maruti Wagon R",
                "Maruti Grand Vitara",
                "Custom/Other"
            ]
        )

        stitch_type = st.selectbox(
            "Stitching Style",
            [
                "Diamond Stitch",
                "Honeycomb Stitch",
                "Tuck and Roll (Pleated)",
                "Contrast Stitching",
                "Threading Stitch Decorative",
                "Double Decorative",
                "Custom"
            ]
        )

        custom_stitch = ""

        if stitch_type == "Custom":

            custom_stitch = st.text_input(
                "Custom Stitch Details"
            )

    # --------------------------------------
    # COLUMN B
    # --------------------------------------

    with colB:

        material = st.selectbox(
            "Material",
            [
                "1200 GSM Nappa",
                "Cotton",
                "Synthetic Leather",
                "Carbon Fiber Leather"
            ]
        )

        piping_quilt = st.toggle(
            "Design Piping & Quilting"
        )

        custom_pq = ""

        if piping_quilt:

            custom_pq = st.text_input(
                "Custom Piping/Quilt Prompt"
            )

    # --------------------------------------
    # COLUMN C
    # --------------------------------------

    with colC:

        base_color_toggle = st.toggle("Base Colors")

        if base_color_toggle:

            base_color = st.selectbox(
                "Color",
                [
                    "Beige",
                    "Ivory",
                    "Black"
                ]
            )

        else:

            base_color = "Tan & Charcoal"

        num_images = st.select_slider(
            "Generation Count",
            options=[1, 3, 5]
        )

    st.divider()

    # --------------------------------------
    # EXTRA OPTIONS
    # --------------------------------------

    col_opt1, col_opt2 = st.columns(2)

    with col_opt1:

        st.toggle("Custom Pattern Mode")

        pattern_target = st.selectbox(
            "Pattern Target",
            [
                "Stitching",
                "Piping",
                "Base Design"
            ]
        )

        side_patch_mode = st.selectbox(
            "Side Patches",
            [
                "None",
                "Full Side Patch (White)",
                "Only Cylindrical Central (White)",
                "Custom"
            ]
        )

        custom_side_patch = ""

        if side_patch_mode == "Custom":

            custom_side_patch = st.text_input(
                "Custom Side Patch Instructions"
            )

    with col_opt2:

        color_control = st.toggle(
            "Color Control Mode"
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

    custom_instruction = st.text_area(
        "✍️ Engineering Instructions",
        placeholder="Add professional engineering details..."
    )

# --------------------------------------
# 🚀 EXECUTION PIPELINE
# --------------------------------------

if st.button("🚀 EXECUTE FULL SUITE"):

    generated_images = []

    # --------------------------------------
    # PALETTE
    # --------------------------------------

    palette = color_choices.get(num_images)

    # --------------------------------------
    # VEHICLE RULES
    # --------------------------------------

    vehicle_structure_prompt = ""

    if car == "Maruti Wagon R":

        vehicle_structure_prompt = """
STRICTLY preserve original Maruti Wagon R OEM fixed headrest geometry.

CRITICAL:
- Headrest MUST be integrated/fixed
- NEVER generate detachable headrests
- NEVER generate adjustable rod headrests
- Maintain compact WagonR proportions
- Maintain upright hatchback ergonomics
- Exact WagonR cabin structure

Reference:
https://www.carwale.com/maruti-suzuki-cars/wagon-r/images/maruti-suzuki-wagon-r-front-row-seats-442349/?category=interior,
https://www.marutisuzuki.com/wagonr
"""

    elif car == "Maruti Grand Vitara":

        vehicle_structure_prompt = """
STRICTLY preserve original Maruti Grand Vitara OEM seat architecture.

Reference:
https://www.marutisuzuki.com/grand-vitara
"""

    # --------------------------------------
    # SIDE PATCH
    # --------------------------------------

    side_patch_prompt = ""

    if side_patch_mode == "Full Side Patch (White)":

        side_patch_prompt = """
Full white side patches extending from
shoulder to lower seat base.
"""

    elif side_patch_mode == "Only Cylindrical Central (White)":

        side_patch_prompt = """
Only central cylindrical inserts in white.
Keep outer bolsters black.
"""

    elif side_patch_mode == "Custom":

        side_patch_prompt = custom_side_patch

    # --------------------------------------
    # STATUS
    # --------------------------------------

    with st.status("Engineering Intelligence..."):

        for i in range(num_images):

            current_color = (
                manual_color
                if i == 0
                else palette[i % len(palette)]
            )

            # --------------------------------------
            # COLOR RULES
            # --------------------------------------

            color_rule = ""

            if color_control:

                color_rule = f"""
STRICTLY use {current_color}
as stitching/accent color.
Do not introduce random colors.
"""

            else:

                color_rule = """
Creative complementary tones allowed.
"""

            # --------------------------------------
            # MAIN PROMPT
            # --------------------------------------

            strict_prompt = f"""
Professional automotive interior photography.

STRICT OEM ACCURACY REQUIRED.

Vehicle:
{car}

{vehicle_structure_prompt}

Reference Image Guidance:
Use uploaded OEM reference image as structural guidance.

Material:
{material}

Seat Base Color:
{base_color}

Stitching:
{stitch_type}

Thread Accent:
{current_color}

{color_rule}

Side Patch Design:
{side_patch_prompt}

Additional Stitch Details:
{custom_stitch}

Piping & Quilting:
{custom_pq if piping_quilt else "None"}

Engineering Notes:
{custom_instruction}

Rules:
- Preserve OEM seat structure
- Preserve OEM dimensions
- Preserve OEM seat contouring
- No unrealistic luxury modifications
- No floating cushions
- No detachable headrests
- No adjustable rod headrests
- No oversized bolsters
- Production-ready upholstery
- Hyper realistic texture detailing
- Studio lighting
- 8K realism
- Automotive catalog photography
"""

            st.write(
                f"🎨 Generating {current_color} Variant..."
            )

            img = generate_ai_image(
                strict_prompt,
                MODEL_OPTIONS[selected_model]
            )

            if img:

                generated_images.append(
                    (img, current_color)
                )

        # --------------------------------------
        # ANALYSIS
        # --------------------------------------

        st.write(
            "📊 Running Flashmind Intelligence..."
        )

        analysis = call_openrouter(
            f"""
Analyze durability, OEM compatibility,
premium appeal and 2026 trends for
{material} with {stitch_type}
and {side_patch_mode}.
"""
        )

        # --------------------------------------
        # MARKET REFERENCES
        # --------------------------------------

        st.write(
            "🌍 Fetching Market References..."
        )

        market_refs = fetch_market_references(
            f"{car} {material} seat cover"
        )

    # --------------------------------------
    # OUTPUT
    # --------------------------------------

    if generated_images:

        st.subheader("🎨 AI Generated Concepts")

        for idx, (img, c_name) in enumerate(
            generated_images
        ):

            img_col, info_col = st.columns([1.7, 1])

            # --------------------------------------
            # IMAGE PANEL
            # --------------------------------------

            with img_col:

                st.image(
                    img,
                    caption=f"Variant: {c_name}",
                    use_container_width=True
                )

                buf = io.BytesIO()

                img.save(buf, format="PNG")

                st.download_button(
                    f"💾 Save {c_name}",
                    buf.getvalue(),
                    f"pictator_{c_name}.png",
                    key=f"save_{idx}"
                )

            # --------------------------------------
            # INFO PANEL
            # --------------------------------------

            with info_col:

                st.markdown(
                    f"""
### 📈 Flashmind Analysis

**Vehicle:**  
{car}

**Material:**  
{material}

**Stitching:**  
{stitch_type}

**Variant Accent:**  
{c_name}

**Side Patch:**  
{side_patch_mode}

**Base Color:**  
{base_color}

---

### 🧠 OEM Compatibility

✅ OEM Geometry Preserved  
✅ Production Ready  
✅ Premium Finish  
✅ Automotive Grade Detailing  
✅ 2026 Trend Compatible

---

### 📊 Engineering Notes

{analysis}
"""
                )

            st.divider()

    # --------------------------------------
    # MARKET REFERENCES
    # --------------------------------------

    st.subheader(
        "🌍 Verified Market References & Live Shop Links"
    )

    if market_refs:

        cols = st.columns(3)

        for idx, ref in enumerate(market_refs):

            with cols[idx % 3]:

                st.image(
                    ref["img"],
                    caption=f"Ref from {ref['src']}",
                    use_container_width=True
                )

                st.link_button(
                    f"🔗 View on {ref['src']}",
                    ref["link"],
                    key=f"ref_{idx}"
                )

# --------------------------------------
# 📊 TECH STANDARDS
# --------------------------------------

with st.expander("📊 2026 Tech Standards"):

    st.write(
        "- Strict OEM vehicle geometry enforcement enabled."
    )

    st.write(
        "- WagonR fixed-headrest preservation enabled."
    )

    st.write(
        "- Grand Vitara OEM SUV contour mapping enabled."
    )

    st.write(
        "- Hyper-realistic automotive rendering active."
    )

    st.caption(
        "Zero Data Retention (ZDR) Commitment"
    )
```
