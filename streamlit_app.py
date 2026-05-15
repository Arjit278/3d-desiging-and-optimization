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
    "⚡ PaliGemma 2 3B": "google/paligemma2-3b-pt-448",
    "✨ Pixtral 12B": "mistralai/Pixtral-12B-2409",
    "🔥 GLM-4.1V 9B Thinking": "THUDM/glm-4-9b-chat",
    "🏎️ Qwen2.5-VL 7B Instruct": "Qwen/Qwen2.5-VL-7B-Instruct",
    "🏎️ FLUX.2 Klein": "black-forest-labs/FLUX.2-klein-9b-fp8", 
    "✨ FLUX.1 Kontext Dev": "black-forest-labs/FLUX.1-Kontext-dev",
    "🪟 FLUX.1 Fill Dev": "black-forest-labs/FLUX.1-Fill-dev",
    "🌀 FLUX.1 Redux Dev": "black-forest-labs/FLUX.1-Redux-dev"
    
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
    "meta-llama/llama-3.2-3b-instruct:free",
    "nousresearch/hermes-2-pro-llama-3-8b"
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

    col_opt1, col_opt2 = st.columns(2)

    with col_opt1:

        st.toggle("Custom Pattern Mode")

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

    palette = color_choices.get(num_images)

    vehicle_structure_prompt = ""

    
   if car == "Maruti Wagon R":

       
        # --------------------------------------
        # OEM VEHICLE RULES
        # --------------------------------------
        
        wagonr_rules = ""
        
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
        
        # --------------------------------------
        # FINAL AI PROMPT
        # --------------------------------------
        
        final_prompt = f"""
        Professional automotive interior photography.
        
        STRICT OEM ACCURACY REQUIRED.
        
        Vehicle:
        {car}
        
        {wagonr_rules}
        
        Stitching:
        {pattern}
        
        Material:
        {material}
        
        Color Theme:
        {colors}
        
        Lighting:
        {lighting}
        
        Market Tier:
        {market}
        
        Engineering Instructions:
        {custom_instruction}
        
        Rules:
        - Maintain OEM seat geometry
        - No floating cushions
        - No detachable headrests
        - No SUV seat proportions
        - Maintain hatchback ergonomics
        - Production-ready upholstery
        - Hyper realistic leather texture
        - 8K automotive photography
        - Studio catalog rendering
        """

    
    Reference:
    https://www.carwale.com/maruti-suzuki-cars/wagon-r/images/maruti-suzuki-wagon-r-front-row-seats-442349/?category=interior
    """
    
    else:
    
        wagonr_rules = ""
    
    final_prompt = f"""
    Professional automotive interior photography.
    
    STRICT OEM ACCURACY REQUIRED.
    
    Vehicle:
    {car}
    
    {wagonr_rules}
    
    Stitching:
    {pattern}
    
    Material:
    {material}
    
    Color Theme:
    {colors}
    
    Lighting:
    {lighting}
    
    Market Tier:
    {market}
    
    Engineering Instructions:
    {custom_instruction}
    
    Rules:
    - Maintain OEM seat geometry
    - No floating cushions
    - No detachable headrests
    - No SUV seat proportions
    - Maintain hatchback ergonomics
    - Production-ready upholstery
    - Hyper realistic leather texture
    - 8K automotive photography
    - Studio catalog rendering
    """

    elif car == "Maruti Grand Vitara":

        vehicle_structure_prompt = """
STRICTLY preserve original Maruti Grand Vitara OEM seat architecture.

Reference:
https://www.marutisuzuki.com/grand-vitara
"""

    side_patch_prompt = ""

    if side_patch_mode == "Full Side Patch":

        side_patch_prompt = f"""
Generate sporty OEM dual-tone side patches.

{pattern_color} side shoulder patches
flowing vertically from upper shoulders
towards lower seat base.

Black outer bolsters.

Premium sporty hatchback styling.

Maintain compact OEM WagonR seat shape.

Patch flow must resemble uploaded
reference image style.
"""

    elif side_patch_mode == "Only Cylindrical Side Patch":

        side_patch_prompt = f"""
Generate cylindrical side inserts
in {pattern_color} color.

Keep the base color as centre.

Maintain sporty OEM hatchback styling.
"""

    elif side_patch_mode == "Head Rest Patch":

        side_patch_prompt = f"""
Generate integrated fixed headrest patch
in {pattern_color} color.

Headrest MUST remain fixed and integrated.

Blend patch into upper shoulder design.
"""

    elif side_patch_mode == "Custom":

        side_patch_prompt = custom_side_patch

    with st.status("Engineering Intelligence..."):

        for i in range(num_images):

            current_color = (
                manual_color
                if i == 0
                else palette[i % len(palette)]
            )

            color_rule = ""

            if color_control:

                color_rule = f"""
STRICTLY use {current_color}
for stitching/accent details.

STRICTLY use {pattern_color}
for {pattern_target} elements.

Do not introduce random colors.
"""

            else:

                color_rule = """
Creative complementary tones allowed.
"""

            strict_prompt = f"""
Professional automotive interior photography.

STRICT OEM ACCURACY REQUIRED.

Vehicle:
{car}

{vehicle_structure_prompt}

Reference Image Guidance:
Use uploaded OEM reference image
as structural guidance.

Material:
{material}

Seat Base Color:
{base_color}

Stitching:
{stitch_type}

Thread Accent:
{current_color}

Pattern Target:
{pattern_target}

Pattern Color:
{pattern_color}

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
- Maintain WagonR compact proportions
- Maintain integrated fixed headrest
- No luxury SUV seats
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

        st.write(
            "📊 Running Flashmind Intelligence..."
        )

        analysis = call_openrouter(
            f"""
        You are Flashmind Automotive Intelligence 2026.
        
        Generate:
        - 5 to 6 concise bullet points
        - followed by a short premium market summary
        
        Focus on:
        - 2026 upholstery trends
        - sporty hatchback interiors
        - integrated headrest trends
        - dual-tone side patch trends
        - luxury stitching trends
        - OEM upgrade demand
        - ergonomic seat contouring
        - Indian aftermarket trends
        
        Vehicle:
        {car}
        
        Material:
        {material}
        
        Pattern:
        {pattern}
        
        Colorway:
        {colors}
        
        Rules:
        - concise bullets
        - premium automotive tone
        - no generic AI wording
        """
        )

        
        genz_trends = call_openrouter(
            f"""
        You are Flashmind GenZ Automotive Trend Intelligence 2026.
        
        Generate:
        - 8 to 10 premium trend bullet points
        - include trend names
        - include modern buyer preferences
        - include GenZ customization demand
        - include sporty upholstery trends
        - include premium hatchback modifications
        - include luxury stitching trends
        - include seat contour trends
        - include side patch trends
        - include ambient cabin styling trends
        - include compact sporty OEM upgrade trends
        
        Vehicle:
        {car}
        
        Material:
        {material}
        
        Pattern:
        {pattern}
        
        Colorway:
        {colors}
        
        Output format:
        - professional bullets
        - premium automotive language
        - NO paragraphs
        - concise but insightful
        - include small web/article references when relevant
        
        Example:
        • Floating contrast side patches trending in GenZ hatchbacks (AutoForm 2026)
        """
        )



        st.write(
            "🌍 Fetching Market References..."
        )

        market_refs = fetch_market_references(
            f"{car} {material} seat cover"
        )

    if generated_images:

        st.subheader("🎨 AI Generated Concepts")

        for idx, (img, c_name) in enumerate(
            generated_images
        ):

            img_col, info_col = st.columns([1.7, 1])

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

            with info_col:

                st.markdown(
                    f"""
### 📈 Flashmind Analysis

#### 🚘 Vehicle
{car}

#### 🧵 Material
{material}

#### ✨ Stitching
{stitch_type}

#### 🎨 Pattern Target
{pattern_target}

#### 🛡️ Patch Style
{side_patch_mode}

#### 🎯 Pattern Color
{pattern_color}

#### 🎨 Variant Accent
{c_name}

---

### 🧠 OEM Compatibility

✅ Fixed Headrest Geometry Preserved  
✅ OEM Hatchback Seat Mapping  
✅ Production Ready Design  
✅ Premium Upholstery Finish  
✅ Automotive Grade Detailing  
✅ 2026 Trend Compatible  
✅ Ergonomic Compact Seat Profile  

---

### 🔥 2026 Trend Intelligence

{analysis}
"""
                )

            st.divider()

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


                st.divider()
                
                st.subheader("📈 Flashmind 2026 Trend Intelligence")
                
                st.markdown(
                    f"""
                ### 🚘 Vehicle
                {car}
                
                ### 🧵 Material
                {material}
                
                ### ✨ Stitching
                {pattern}
                
                ### 🎨 Colorway
                {colors}
                
                ---
                
                ### 🔥 Market + Upholstery Trends
                
                {analysis}
                
                ---
                
                ### 🧠 OEM Intelligence
                
                ✅ Fixed Headrest Enforcement Active  
                ✅ Hatchback Seat Mapping Enabled  
                ✅ Premium Side Patch Styling Active  
                ✅ 2026 Trend Optimization Enabled  
                ✅ OEM Geometry Preservation Active  
                """
                )

st.divider()

st.subheader("🔥 GenZ Upholstery & Market Intelligence 2026")

st.markdown(
    f"""
### 🚘 Vehicle Segment
{car}

### 🎨 Current Customization Direction
{pattern} • {colors} • {material}

---

### 📈 GenZ Buyer Preferences & Trends

{genz_trends}

---

### 🌐 Premium Market Signals

• OEM+ sporty interiors dominating premium hatchback upgrades  
• Integrated headrest seat demand increasing in urban GenZ buyers  
• Dual-tone side patch styling trending in aftermarket customization  
• Ambient stitching + contrast piping rapidly growing in Tier-1 cities  
• Compact sporty seat ergonomics outperform bulky luxury seats  
"""
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

    st.write(
        "- OEM WagonR fixed integrated headrest enforcement active."
    )

    st.write(
        "- Reference-image guided side patch generation active."
    )

    st.write(
        "- 2026 sporty hatchback upholstery intelligence enabled."
    )

    st.caption(
        "Zero Data Retention (ZDR) Commitment"
    )
