"""
Karussell-Builder für Theresa Ross Instagram Posts
Rendert Slides als 1080x1350 PNG mit korrekter Typografie.

Nutzung:
    python3 build_carousel.py --post 01

Voraussetzung:
    pip3 install Pillow
"""

import os
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps

# ==========================================
# DESIGN TOKENS
# ==========================================
COLORS = {
    'bg_creme': (245, 239, 232),
    'bg_beige': (232, 220, 200),
    'text_dark': (58, 46, 42),
    'accent_graurot': (176, 130, 116),
    'accent_zart': (201, 169, 154),
    'white': (255, 253, 248),
}

SLIDE_W = 1080
SLIDE_H = 1350
SAFE_X = 80
SAFE_Y = 100
CONTENT_W = SLIDE_W - 2 * SAFE_X  # 920
CONTENT_H = SLIDE_H - 2 * SAFE_Y  # 1150

# Font paths (macOS system fonts als Fallback)
FONT_PATHS = {
    'headline': None,  # Wird beim Start gesucht
    'body': None,
}

def find_fonts():
    """Sucht verfügbare Fonts auf dem System."""
    candidates_headline = [
        '/System/Library/Fonts/Supplemental/Times New Roman.ttf',
        '/System/Library/Fonts/Times.ttc',
        '/System/Library/Fonts/Georgia.ttf',
    ]
    candidates_body = [
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/SFNSText.ttf',
        '/System/Library/Fonts/Supplemental/Arial.ttf',
    ]

    for path in candidates_headline:
        if os.path.exists(path):
            FONT_PATHS['headline'] = path
            break

    for path in candidates_body:
        if os.path.exists(path):
            FONT_PATHS['body'] = path
            break

    if not FONT_PATHS['headline']:
        print("WARNUNG: Kein Headline-Font gefunden, nutze Default")
    if not FONT_PATHS['body']:
        print("WARNUNG: Kein Body-Font gefunden, nutze Default")

def get_font(role, size):
    """Lädt Font mit Fallback."""
    path = FONT_PATHS.get(role)
    try:
        if path:
            return ImageFont.truetype(path, size)
    except:
        pass
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        return ImageFont.load_default()

# ==========================================
# TYPOGRAFIE-CHECKS
# ==========================================
def fix_german_typography(text):
    """Deutsche Typografie-Regeln anwenden."""
    # Gerade Anführungszeichen → deutsche
    text = text.replace('"', '„').replace('"', '"')
    # Drei Punkte → Auslassungszeichen
    text = text.replace('...', '…')
    # Gerade Apostrophe → typografisch
    text = text.replace("'", "\u2019")
    return text

def smart_wrap(text, max_chars):
    """Intelligenter Zeilenumbruch ohne Schusterjungen."""
    if '\n' in text:
        return text  # Manuelle Umbrüche respektieren

    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if len(test_line) <= max_chars:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        # Schusterjungen vermeiden: wenn letzte Zeile nur 1 Wort hat
        if len(current_line) == 1 and len(lines) > 0:
            last_line_words = lines[-1].split()
            if len(last_line_words) > 2:
                # Letztes Wort der vorletzten Zeile nach unten ziehen
                move_word = last_line_words[-1]
                lines[-1] = ' '.join(last_line_words[:-1])
                current_line = [move_word] + current_line
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

# ==========================================
# SLIDE RENDERING
# ==========================================
def create_slide(bg_color='bg_creme'):
    """Erstellt leere Slide mit Hintergrundfarbe."""
    img = Image.new('RGB', (SLIDE_W, SLIDE_H), COLORS[bg_color])
    draw = ImageDraw.Draw(img)
    return img, draw

def draw_text_centered(draw, text, y, font, color='text_dark', max_width=CONTENT_W):
    """Zeichnet Text zentriert auf der Slide."""
    text = fix_german_typography(text)

    # Text-Bounding-Box berechnen
    bbox = draw.textbbox((0, 0), text, font=font, anchor='lt')
    text_w = bbox[2] - bbox[0]

    x = (SLIDE_W - text_w) // 2
    draw.text((x, y), text, font=font, fill=COLORS[color])

    return bbox[3] - bbox[1]  # Höhe zurückgeben

def draw_multiline_centered(draw, text, y, font, color='text_dark',
                             line_height_factor=1.4, max_chars=35):
    """Zeichnet mehrzeiligen Text zentriert."""
    text = fix_german_typography(text)
    wrapped = smart_wrap(text, max_chars)
    lines = wrapped.split('\n')

    # Zeilenhöhe berechnen
    sample_bbox = draw.textbbox((0, 0), "Ag", font=font)
    single_height = sample_bbox[3] - sample_bbox[1]
    line_h = int(single_height * line_height_factor)

    # Gesamthöhe
    total_h = line_h * len(lines)

    for i, line in enumerate(lines):
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_w = line_bbox[2] - line_bbox[0]
        x = (SLIDE_W - line_w) // 2
        draw.text((x, y + i * line_h), line, font=font, fill=COLORS[color])

    return total_h

def draw_line(draw, y, width=60, color='accent_graurot'):
    """Zeichnet eine dezente horizontale Linie."""
    x_start = (SLIDE_W - width) // 2
    draw.line([(x_start, y), (x_start + width, y)], fill=COLORS[color], width=1)

def draw_signature(draw, text="theresa-ross.de"):
    """Zeichnet Signatur unten auf der Slide."""
    font = get_font('body', 22)
    text = fix_german_typography(text)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = (SLIDE_W - text_w) // 2
    y = SLIDE_H - SAFE_Y - 20
    draw.text((x, y), text, font=font, fill=COLORS['accent_zart'])

# ==========================================
# SLIDE TEMPLATES
# ==========================================
def render_hook_slide(headline, eyebrow=None, bg='bg_creme'):
    """Slide 1: Hook mit großer Headline."""
    img, draw = create_slide(bg)

    y = SAFE_Y + 200

    if eyebrow:
        font_eyebrow = get_font('body', 20)
        draw_text_centered(draw, eyebrow.upper(), y, font_eyebrow, 'accent_graurot')
        y += 60

    font_headline = get_font('headline', 76)
    h = draw_multiline_centered(draw, headline, y, font_headline, 'text_dark',
                                 line_height_factor=1.15, max_chars=20)

    draw_line(draw, y + h + 40)
    draw_signature(draw, "— Theresa")

    return img

def render_text_slide(headline, body=None, bg='bg_creme'):
    """Mittlere Slide: Headline + optionaler Body."""
    img, draw = create_slide(bg)

    y = SAFE_Y + 250

    font_headline = get_font('headline', 60)
    h = draw_multiline_centered(draw, headline, y, font_headline, 'text_dark',
                                 line_height_factor=1.15, max_chars=22)

    if body:
        y_body = y + h + 50
        font_body = get_font('body', 34)
        draw_multiline_centered(draw, body, y_body, font_body, 'accent_graurot',
                                line_height_factor=1.4, max_chars=35)

    return img

def render_quote_slide(quote, author="Theresa", bg='bg_beige'):
    """Zitat-Slide."""
    img, draw = create_slide(bg)

    # Große Anführungszeichen
    font_marks = get_font('headline', 120)
    draw_text_centered(draw, '\u201e', SAFE_Y + 180, font_marks, 'accent_zart')

    y = SAFE_Y + 320
    font_quote = get_font('headline', 44)
    h = draw_multiline_centered(draw, quote, y, font_quote, 'text_dark',
                                 line_height_factor=1.3, max_chars=28)

    # Author
    font_author = get_font('body', 24)
    draw_text_centered(draw, f"— {author}", y + h + 40, font_author, 'accent_graurot')

    return img

def render_cta_slide(cta_text, sub_text=None, bg='bg_creme'):
    """Letzte Slide: CTA + Signatur."""
    img, draw = create_slide(bg)

    y = SAFE_Y + 400

    font_cta = get_font('headline', 52)
    h = draw_multiline_centered(draw, cta_text, y, font_cta, 'text_dark',
                                 line_height_factor=1.2, max_chars=25)

    if sub_text:
        y_sub = y + h + 40
        font_sub = get_font('body', 28)
        draw_multiline_centered(draw, sub_text, y_sub, font_sub, 'accent_graurot',
                                line_height_factor=1.4, max_chars=35)

    draw_signature(draw, "theresa-ross.de")

    return img

# ==========================================
# QUALITÄTSPRÜFUNG
# ==========================================
def quality_check(slides, post_number):
    """Prüft alle Slides vor Export."""
    issues = []
    for i, slide in enumerate(slides):
        # Grundlegende Checks
        if slide.size != (SLIDE_W, SLIDE_H):
            issues.append(f"Slide {i+1}: Falsche Größe {slide.size}")

    if issues:
        print(f"\nQUALITÄTSPRÜFUNG Post {post_number:02d}:")
        for issue in issues:
            print(f"  PRÜFEN: {issue}")
    else:
        print(f"\nQualitätsprüfung Post {post_number:02d}: OK")

    return issues

# ==========================================
# EXPORT
# ==========================================
def export_slides(slides, post_number):
    """Exportiert Slides als PNG."""
    output_dir = os.path.join(
        os.path.dirname(__file__),
        f"../posts/post_{post_number:02d}/output"
    )
    os.makedirs(output_dir, exist_ok=True)

    quality_check(slides, post_number)

    for i, slide in enumerate(slides):
        path = os.path.join(output_dir, f"slide_{i+1:02d}.png")
        slide.save(path, 'PNG', optimize=False)
        print(f"  Exportiert: slide_{i+1:02d}.png")

    print(f"\n{len(slides)} Slides exportiert nach posts/post_{post_number:02d}/output/")

# ==========================================
# DEMO: Post 01 — Was ist der Vagusnerv?
# ==========================================
def build_demo_post():
    """Baut einen Demo-Post zum Testen."""
    find_fonts()

    slides = [
        render_hook_slide(
            "Der längste Nerv\ndeines Körpers.",
            eyebrow="Nervensystem"
        ),
        render_text_slide(
            "Der Vagusnerv verbindet\nGehirn, Herz, Lunge\nund Darm.",
        ),
        render_text_slide(
            "Wenn er funktioniert:",
            "Ruhige Verdauung.\nTiefer Schlaf.\nStabile Energie."
        ),
        render_text_slide(
            "Wenn er überreizt ist:",
            "Reizdarm. Schlafprobleme.\nErschöpfung. Innere Unruhe."
        ),
        render_quote_slide(
            "Du kannst deinen Vagusnerv\nnicht durch Willenskraft\nberuhigen. Aber du kannst\ndeinem Körper beibringen,\nes wieder zu tun."
        ),
        render_cta_slide(
            "Speicher dir das.",
            "Mehr zum Nervensystem\nin meinem Workbook."
        ),
    ]

    # Ordner erstellen
    post_dir = os.path.join(os.path.dirname(__file__), "../posts/post_01")
    os.makedirs(os.path.join(post_dir, "input/manual"), exist_ok=True)
    os.makedirs(os.path.join(post_dir, "input/unsplash"), exist_ok=True)
    os.makedirs(os.path.join(post_dir, "output"), exist_ok=True)

    export_slides(slides, 1)

    # Caption
    caption = """Der längste Nerv deines Körpers.

Er verbindet Gehirn, Herz, Lunge und Darm.
Er entscheidet, ob dein Körper zur Ruhe kommt.
Oder im Alarmmodus bleibt.

Speicher dir das.

#theresaross #nervensystem #vagusnerv #darmhirnachse #stressregulation #darmgesundheit"""

    caption_path = os.path.join(post_dir, "output/caption.txt")
    with open(caption_path, 'w') as f:
        f.write(caption)
    print(f"  Caption gespeichert: caption.txt")

if __name__ == "__main__":
    if '--demo' in sys.argv or '--post' not in sys.argv:
        print("Baue Demo-Post 01: Was ist der Vagusnerv?\n")
        build_demo_post()
    else:
        post_num = int(sys.argv[sys.argv.index('--post') + 1])
        print(f"Post {post_num:02d} bauen (noch nicht implementiert)")
        print("Nutze --demo für einen Beispiel-Post")
