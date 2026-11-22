import streamlit as st
from pathlib import Path

st.set_page_config(page_title="KTG CAPTURES | Photography Portfolio", page_icon="📷", layout="wide")
BASE = Path(__file__).parent

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
:root { --ink:#171a1c; --muted:#72787b; --paper:#f7f7f4; --line:#e5e5df; }
.stApp { background:var(--paper); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1240px; padding-top:1.4rem; padding-bottom:4rem; }
header[data-testid="stHeader"] { background:transparent; }
.brand { letter-spacing:.28em; font-size:.83rem; font-weight:700; }
.navline { border-bottom:1px solid var(--line); padding: .55rem 0 1.1rem; margin-bottom:2.8rem; display:flex; justify-content:space-between; align-items:center; }
.hero { padding:3.6rem 0 3.2rem; border-bottom:1px solid var(--line); }
.eyebrow { text-transform:uppercase; letter-spacing:.25em; color:var(--muted); font-size:.72rem; font-weight:600; }
.hero h1 { font-family:'Playfair Display',serif; font-size:clamp(3.5rem,8vw,7.5rem); line-height:.98; letter-spacing:-.055em; margin:.8rem 0 1.1rem; color:var(--ink); }
.hero p { max-width:570px; color:#5d6467; font-size:1.05rem; line-height:1.8; }
.section-title { font-family:'Playfair Display',serif; font-size:2.5rem; margin:0; }
.small-note { color:var(--muted); font-size:.88rem; }
.photo-card { background:white; padding:0 0 .8rem; }
.caption { padding:.7rem .2rem 0; color:#313638; font-size:.92rem; }
.tag { color:var(--muted); text-transform:uppercase; letter-spacing:.15em; font-size:.65rem; padding-top:.25rem; }
.about { background:#eceeea; padding:2.4rem; border-radius:3px; }
.about h2 { font-family:'Playfair Display',serif; font-size:2.2rem; margin-top:0; }
.footer { border-top:1px solid var(--line); margin-top:4rem; padding-top:1.5rem; color:var(--muted); font-size:.8rem; }
div[data-testid="stImage"] img { border-radius:2px; }
.stButton button { border-radius:2px; border:1px solid #222; background:#222; color:white; padding:.55rem 1.1rem; }
</style>
""", unsafe_allow_html=True)

photos = [
    {"file":"01-seascape-boat.jpeg", "title":"Between Tides", "category":"Seascapes", "desc":"A quiet boat on an endless blue horizon."},
    {"file":"02-bird-in-flight.jpeg", "title":"A Moment in Flight", "category":"Wildlife", "desc":"A small silhouette against an open sky."},
    {"file":"03-red-parrot.jpeg", "title":"A Flash of Red", "category":"Wildlife", "desc":"Colour, character and a curious gaze."},
    {"file":"04-toucan.jpeg", "title":"The Toucan", "category":"Wildlife", "desc":"A close-up study of a striking beak and bold details."},
    {"file":"05-butterfly-flower.jpeg", "title":"A Delicate Pause", "category":"Nature", "desc":"A butterfly resting on a bright bloom."},
    {"file":"06-vintage-car-night.jpeg", "title":"After Dark", "category":"Street & Details", "desc":"A vintage silhouette under the streetlights."},
    {"file":"07-warm-lanterns.jpeg", "title":"Golden Glow", "category":"Architecture & Details", "desc":"Warm woven lights beneath a textured roof."},
    {"file":"08-temple-elephant.jpeg", "title":"Tradition in Frame", "category":"Culture", "desc":"A decorated elephant in a temple setting."},
    {"file":"09-clocktower-sky.jpeg", "title":"Time Above Us", "category":"Architecture & Details", "desc":"A clocktower framed by a dramatic sky."},
    {"file":"10-crowned-crane.jpeg", "title":"Crowned Elegance", "category":"Wildlife", "desc":"The graceful profile of a crowned crane."},
]

st.markdown('<div class="navline"><div class="brand">KTG&nbsp; CAPTURES</div><div class="small-note">PHOTOGRAPHY · PORTFOLIO</div></div>', unsafe_allow_html=True)
st.markdown('''<section class="hero"><div class="eyebrow">A personal photography journal</div><h1>Finding beauty<br>in the in-between.</h1><p>Stories told through light, colour and quiet details. A collection of moments from nature, wildlife, coastlines and the world around me.</p></section>''', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="eyebrow">Selected photographs</div><div style="display:flex;justify-content:space-between;align-items:end;gap:1rem;flex-wrap:wrap"><div class="section-title">The Gallery</div><div class="small-note">10 photographs · KTG CAPTURES</div></div>', unsafe_allow_html=True)
choices = ["All work"] + sorted({p["category"] for p in photos})
selected = st.selectbox("Explore by collection", choices, label_visibility="collapsed")
visible = photos if selected == "All work" else [p for p in photos if p["category"] == selected]

for start in range(0, len(visible), 2):
    cols = st.columns(2, gap="large")
    for col, photo in zip(cols, visible[start:start+2]):
        with col:
            st.image(str(BASE / photo["file"]), use_container_width=True)
            st.markdown(f'<div class="caption"><strong>{photo["title"]}</strong><div class="tag">{photo["category"]}</div><div class="small-note">{photo["desc"]}</div></div>', unsafe_allow_html=True)
            st.write("")

st.write("")
st.markdown('''<div class="about"><div class="eyebrow">Behind the lens</div><h2>Hey, I’m the eye behind KTG CAPTURES.</h2><p>Photography is my way of slowing down and noticing the details that are easy to miss — a bird in motion, changing skies, a quiet shoreline or the character of a place. This portfolio brings together a few frames I’m proud to share.</p><p class="small-note">Every photograph is a moment collected, not just an image captured.</p></div>''', unsafe_allow_html=True)

st.write("")
left, right = st.columns([2,1], vertical_alignment="center")
with left:
    st.markdown('<div class="eyebrow">Let’s connect</div><div class="section-title">See more moments.</div><p class="small-note">Follow the photography journey on Instagram.</p>', unsafe_allow_html=True)
with right:
    st.link_button("Follow @KTG_CAPTURES on Instagram", "https://www.instagram.com/ktg_captures/", use_container_width=True)

st.markdown('<div class="footer">© KTG CAPTURES · A personal photography portfolio<br>Made with a love for light, moments and storytelling.</div>', unsafe_allow_html=True)
