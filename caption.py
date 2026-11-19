#!/usr/bin/env python3
"""Draw meme captions onto meme-base.png and save the result as meme.png.

Layout (image is 1600x1600):
  - Two white headline lines across the sunset sky at the top, well above
    the ghost's head (the ghost starts around y=800).
  - A magenta "make.fun" tag on the dark street at the bottom-left,
    clear of the ghost (which occupies the center bottom).
"""

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BASE_IMAGE = "meme-base.png"
OUT_IMAGE = "meme.png"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 47, 179)  # #FF2FB3

MARGIN = 40  # minimum px between any caption and the image edge


def load_font(size):
    return ImageFont.truetype(FONT_PATH, size)


def fit_font(draw, text, start_size, max_width, stroke_width=0):
    """Shrink the font from start_size until text fits max_width.

    Width is measured including the stroke, so the visible outline
    (not just the glyph box) respects the caller's margins.
    """
    size = start_size
    while size > 10:
        font = load_font(size)
        box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    return load_font(size)


def draw_centered(draw, img_width, text, y, size, fill, stroke_width):
    font = fit_font(draw, text, size, img_width - 2 * MARGIN, stroke_width)
    draw.text(
        (img_width / 2, y),
        text,
        font=font,
        fill=fill,
        anchor="ma",  # middle horizontally, top of ascenders vertically
        stroke_width=stroke_width,
        stroke_fill=BLACK if fill == WHITE else WHITE,
    )
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return box[3] - box[1]  # rendered text height


def main():
    img = Image.open(BASE_IMAGE).convert("RGB")
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # --- Top headline, in the sky ---
    line1 = "WAITED 13 YEARS FOR GTA VI"
    line2 = "MY AI AGENT GOT PAID WAITING"

    y = 78
    h1 = draw_centered(draw, width, line1, y, 88, WHITE, stroke_width=7)
    y += h1 + 34
    draw_centered(draw, width, line2, y, 62, WHITE, stroke_width=6)

    # --- Bottom-left tag, on the dark street ---
    tag = "make.fun"
    tag_size = 58
    tag_font = fit_font(draw, tag, tag_size, width // 3, stroke_width=2)
    tag_box = draw.textbbox((0, 0), tag, font=tag_font, stroke_width=2)
    tag_h = tag_box[3] - tag_box[1]
    draw.text(
        (56, height - tag_h - 64),
        tag,
        font=tag_font,
        fill=MAGENTA,
        stroke_width=2,
        stroke_fill=WHITE,
    )

    img.save(OUT_IMAGE)
    print(f"saved {OUT_IMAGE}: {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
