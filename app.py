import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="KTG CAPTURES | Photography Portfolio",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent

PHOTOS = [   
    {"file": "15-hanging-lantern.jpeg", "title": "A Quiet Glow", "category": "Architecture", "description": "A hanging lantern framed by warm afternoon light and soft greenery."},
    {"file": "02-bird-in-flight.jpeg", "title": "A Moment in Flight", "category": "Wildlife", "description": "A fleeting silhouette framed by open sky."},
    {"file": "03-red-parrot.jpeg", "title": "A Flash of Red", "category": "Wildlife", "description": "Colour, character and a curious gaze."},
    {"file": "04-toucan.jpeg", "title": "The Toucan", "category": "Wildlife", "description": "A close study of bold colour and remarkable detail."},
    {"file": "05-butterfly-flower.jpeg", "title": "A Delicate Pause", "category": "Nature", "description": "A butterfly finding stillness on a bright bloom."},
    {"file": "06-vintage-car-night.jpeg", "title": "After Dark", "category": "Street & Details", "description": "A vintage silhouette beneath the night lights."},
    {"file": "07-warm-lanterns.jpeg", "title": "Golden Glow", "category": "Architecture", "description": "Warm woven lights beneath a textured roof."},
    {"file": "08-temple-elephant.jpeg", "title": "Tradition in Frame", "category": "Culture", "description": "A richly detailed moment of cultural tradition."},
    {"file": "09-clocktower-sky.jpeg", "title": "Time Above Us", "category": "Architecture", "description": "A clocktower set against a dramatic sky."},
    {"file": "10-crowned-crane.jpeg", "title": "Crowned Elegance", "category": "Wildlife", "description": "The graceful profile of a crowned crane."},
    {"file": "11-palace-reflection.jpeg", "title": "A Palace in Stillness", "category": "Architecture", "description": "An illuminated palace mirrored across the quiet water after dark."},
    {"file": "12-wings-above.jpeg", "title": "Wings Above", "category": "Wildlife", "description": "Birds gliding across a vast, cloud-filled sky."},
    {"file": "13-crystal-light.jpeg", "title": "Crystal Light", "category": "Architecture", "description": "A dramatic study of a grand chandelier and its intricate details."},
    {"file": "14-pink-cockatoo.jpeg", "title": "A Gentle Presence", "category": "Wildlife", "description": "A soft-pink cockatoo pausing for a quiet moment on its perch."},
    {"file": "01-seascape-boat.jpeg", "title": "Between Tides", "category": "Seascapes", "description": "A quiet boat resting on an endless blue horizon."},
]


def photo_path(filename: str) -> Path:
    """Support both the current GitHub root layout and an images/ subfolder."""
    candidates = [BASE / filename, BASE / "images" / filename]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        f"Couldn't find {filename}. Place it beside app.py or inside an images folder."
    )


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');
:root { --bg:#101110; --panel:#191b19; --ink:#f2f0e9; --muted:#a4a49b; --gold:#c6a875; --line:#34352f; }
.stApp { background:var(--bg); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1320px; padding:1.5rem 3rem 4rem; }
header[data-testid="stHeader"] { background:transparent; }
footer { visibility:hidden; }
#MainMenu { visibility:hidden; }
.brand { font-size:.85rem; font-weight:700; letter-spacing:.34em; color:var(--ink); }
.brand span { color:var(--gold); }
.nav-meta { color:var(--muted); font-size:.68rem; letter-spacing:.16em; text-transform:uppercase; text-align:right; padding-top:.2rem; }\n.nav-meta a { color:var(--muted); text-decoration:none; transition:color .2s ease; }\n.nav-meta a:hover { color:var(--gold); }
.rule { border-top:1px solid var(--line); margin:1rem 0 3rem; }
.eyebrow { color:var(--gold); font-size:.68rem; font-weight:600; letter-spacing:.25em; text-transform:uppercase; }
.hero-title { font-family:'Playfair Display',serif; font-size:clamp(3.2rem,7vw,6.6rem); line-height:.98; letter-spacing:-.045em; color:var(--ink); margin:.9rem 0 1.3rem; }
.hero-title em { color:var(--gold); font-weight:400; }
.hero-copy { color:#b9b9b0; font-size:1rem; line-height:1.9; max-width:540px; }
.hero-note { color:var(--muted); font-size:.68rem; letter-spacing:.18em; text-transform:uppercase; margin-top:1.3rem; }
.section-kicker { color:var(--gold); text-transform:uppercase; letter-spacing:.24em; font-size:.68rem; font-weight:600; }
.section-heading { color:var(--ink); font-family:'Playfair Display',serif; font-size:clamp(2.1rem,4vw,3.4rem); line-height:1.1; margin:.35rem 0 .6rem; }
.section-copy { color:var(--muted); font-size:.9rem; line-height:1.8; }
.photo-title { color:var(--ink); font-family:'Playfair Display',serif; font-size:1.35rem; margin:.65rem 0 .15rem; }
.photo-category { color:var(--gold); font-size:.64rem; letter-spacing:.18em; text-transform:uppercase; }
.photo-description { color:var(--muted); font-size:.82rem; line-height:1.7; margin-top:.4rem; }
.stat-number { color:var(--ink); font-family:'Playfair Display',serif; font-size:2rem; }
.stat-label { color:var(--muted); font-size:.65rem; letter-spacing:.16em; text-transform:uppercase; }
.about-panel { background:#1a1c19; border:1px solid var(--line); padding:2rem; }
.about-heading { font-family:'Playfair Display',serif; color:var(--ink); font-size:2.2rem; line-height:1.15; }
.footer-line { border-top:1px solid var(--line); margin-top:4rem; padding-top:1.5rem; color:var(--muted); font-size:.75rem; letter-spacing:.08em; }
div[data-testid="stImage"] img { border-radius:2px; }
.stSelectbox label { color:var(--muted) !important; }
.stSelectbox div[data-baseweb="select"] > div { background:#1a1c19; border-color:var(--line); color:var(--ink); }
.stButton button, .stLinkButton a { border-radius:2px; border:1px solid var(--gold); background:var(--gold); color:#171713; font-weight:600; }
.stButton button:hover, .stLinkButton a:hover { border-color:#e0c18c; background:#e0c18c; color:#171713; }
@media (max-width: 700px) { .block-container { padding:1rem 1.1rem 3rem; } .hero-title { font-size:3.35rem; } }
</style>
""", unsafe_allow_html=True)

# Header
head_left, head_right = st.columns([1.25, 1])
with head_left:
    st.markdown('<div class="brand">KTG <span>CAPTURES</span></div>', unsafe_allow_html=True)
with head_right:
    st.markdown(
        '<div class="nav-meta"><a href="#portfolio">PORTFOLIO</a>&nbsp;&nbsp;&nbsp; '
        '<a href="#about">ABOUT</a>&nbsp;&nbsp;&nbsp; '
        '<a href="#contact">CONTACT</a></div>',
        unsafe_allow_html=True,
    )
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# Hero
hero_text, hero_image = st.columns([1.08, 0.92], gap="large")
with hero_text:
    st.markdown('<div class="eyebrow">Independent photography · Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Finding beauty<br>in the <em>little things.</em></div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-copy">Finding beauty in the little things. Stories told through light, colour and quiet details — from wildlife and nature to coastlines, architecture, culture and the world around us.</p>', unsafe_allow_html=True)
    st.markdown('<div class="hero-note">Observe slowly&nbsp;&nbsp; · &nbsp;&nbsp;Feel deeply&nbsp;&nbsp; · &nbsp;&nbsp;Capture honestly</div>', unsafe_allow_html=True)
with hero_image:
    st.image(str(photo_path("01-seascape-boat.jpeg")), use_container_width=True)

st.write("")
stat1, stat2, stat3 = st.columns(3)
for col, number, label in [
    (stat1, str(len(PHOTOS)), "Selected frames"),
    (stat2, "06", "Visual collections"),
    (stat3, "01", "Point of view"),
]:
    with col:
        st.markdown(f'<div class="stat-number">{number}</div><div class="stat-label">{label}</div>', unsafe_allow_html=True)
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# Gallery heading and filter
st.markdown('<div id="portfolio"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-kicker">The visual archive</div><div class="section-heading">Selected photographs</div><div class="section-copy">A few frames, each with a story of its own.</div>', unsafe_allow_html=True)
all_categories = ["All photographs"] + sorted({p["category"] for p in PHOTOS})
selected_category = st.selectbox("Browse collection", all_categories, label_visibility="collapsed")
visible_photos = PHOTOS if selected_category == "All photographs" else [p for p in PHOTOS if p["category"] == selected_category]

for start in range(0, len(visible_photos), 2):
    left, right = st.columns(2, gap="large")
    for col, photo in zip((left, right), visible_photos[start:start + 2]):
        with col:
            st.image(str(photo_path(photo["file"])), use_container_width=True)
            st.markdown(
                f'<div class="photo-title">{photo["title"]}</div>'
                f'<div class="photo-category">{photo["category"]}</div>'
                f'<div class="photo-description">{photo["description"]}</div>',
                unsafe_allow_html=True,
            )
            st.write("")

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# About
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
about_left, about_right = st.columns([1.15, 0.85], gap="large")
with about_left:
    st.markdown('<div class="section-kicker">Behind the lens</div><div class="about-heading">A little patience.<br>A different perspective.</div>', unsafe_allow_html=True)
    st.markdown('<p class="section-copy">I’m the eye behind KTG CAPTURES. Photography is my way of slowing down and noticing the details that are easy to miss — a bird in motion, changing skies, a quiet shoreline or the character of a place.</p><p class="section-copy">This portfolio brings together moments I have enjoyed discovering and capturing. Every frame is a reminder to look a little closer.</p>', unsafe_allow_html=True)
with about_right:
    st.markdown('<div class="about-panel"><div class="eyebrow">The philosophy</div><div class="about-heading">“Every photograph begins with noticing.”</div><p class="section-copy">Light changes. Moments pass. The feeling of a frame is what stays.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
contact_left, contact_right = st.columns([1.4, 1])
with contact_left:
    st.markdown('<div class="section-kicker">Stay connected</div><div class="section-heading">More moments. More stories.</div><div class="section-copy">Follow the journey, discover new frames and get in touch through Instagram.</div>', unsafe_allow_html=True)
with contact_right:
    st.link_button("FOLLOW @KTG_CAPTURES  ↗", "https://www.instagram.com/ktg_captures/", use_container_width=True)

st.markdown('<div class="footer-line">© 2026 KTG CAPTURES &nbsp; · &nbsp; A PERSONAL PHOTOGRAPHY PORTFOLIO<br><br>MADE WITH CURIOSITY, LIGHT AND A LOVE FOR THE DETAILS.</div>', unsafe_allow_html=True)
