import os
from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
PAPER = (250, 244, 230)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 64, 120)
GREY = (90, 86, 78)
LIGHT = (232, 224, 206)
TEAL = (16, 110, 110)
ORANGE = (214, 110, 20)

BASE = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(BASE, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap_text(text, fnt, max_w):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(d, x, y, text, fnt, max_w, leading, color=INK):
    lines = wrap_text(text, fnt, max_w)
    for line in lines:
        d.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(d, x, y, w, color=INK, thick=2):
    d.line([(x, y), (x + w, y)], fill=color, width=thick)


def kicker(d, x, y, label, color=RED):
    f = SANS_B(17)
    d.text((x, y), label, font=f, fill=color)
    return y + 26


def headline(d, x, y, text, size, max_w, leading, color=INK):
    f = SERIF_B(size)
    lines = wrap_text(text, f, max_w)
    for line in lines:
        d.text((x, y), line, font=f, fill=color)
        y += leading
    return y


def draw_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(158, 196, 222), outline=BLUE, width=4)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=TEAL, width=5)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=TEAL, width=5)
    d.line([(cx - r + 12, cy - 8), (cx - 6, cy + 14), (cx + 8, cy - 2), (cx + r - 14, cy + 26)], fill=RED, width=5)
    d.line([(cx - r + 30, cy + r - 18), (cx - 10, cy + r - 34), (cx + 4, cy + r - 12)], fill=RED, width=4)
    d.ellipse([cx - 52, cy - 58, cx - 6, cy - 26], fill=(74, 140, 90))
    d.ellipse([cx + 8, cy + 30, cx + 52, cy + 62], fill=(74, 140, 90))


def draw_ship(d, x, y, w, h):
    top = y + int(h * 0.55)
    d.polygon([(x, top), (x + w, top), (x + w - 14, y + h), (x + 14, y + h)], fill=(60, 60, 66))
    d.rectangle([x + 30, y + int(h * 0.2), x + w - 30, top], fill=(120, 120, 128))
    d.rectangle([x + w // 2 - 4, y, x + w // 2 + 4, y + int(h * 0.25)], fill=INK)
    d.line([(x + 10, y + h + 8), (x + w - 10, y + h + 8)], fill=BLUE, width=3)
    d.line([(x + 26, y + h + 15), (x + w - 26, y + h + 15)], fill=BLUE, width=3)
    d.ellipse([x + w - 58, y - 8, x + w - 36, y + 14], fill=ORANGE)
    d.line([(x + w - 47, y + 14), (x + w - 47, y + 28)], fill=ORANGE, width=3)
    d.line([(x + w - 54, y + 25), (x + w - 40, y + 25)], fill=ORANGE, width=3)


def draw_rubble(d, x, y, w, h):
    base = y + h
    d.rectangle([x, base - 6, x + w, base], fill=GREY)
    d.polygon([(x + 8, base - 6), (x + 44, y + 10), (x + 86, base - 6)], fill=(150, 142, 128))
    d.polygon([(x + 96, base - 6), (x + 128, y + 22), (x + 168, base - 6)], fill=(120, 112, 100))
    d.polygon([(x + 176, base - 6), (x + 210, y + 4), (x + 246, base - 6)], fill=(150, 142, 128))
    d.rectangle([x + 50, y + 26, x + 62, y + 38], fill=INK)
    d.rectangle([x + 138, y + 32, x + 150, y + 44], fill=INK)
    d.line([(x + 210, y + 4), (x + 224, y - 10)], fill=RED, width=4)


def draw_flame(d, cx, cy, s):
    d.polygon([(cx - s, cy + s), (cx - s // 2, cy - s // 3), (cx, cy - s), (cx + s // 3, cy - s // 4), (cx + s, cy + s)], fill=ORANGE)
    d.polygon([(cx - s // 2, cy + s), (cx - s // 5, cy), (cx + s // 4, cy + s // 2), (cx + s // 2, cy + s)], fill=(240, 200, 40))
    d.rectangle([cx - s - 14, cy + s + 6, cx + s + 14, cy + s + 12], fill=(70, 66, 60))


def draw_chip(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(20, 20, 26), outline=(90, 200, 120), width=3)
    d.rectangle([x + w // 4, y + h // 4, x + 3 * w // 4, y + 3 * h // 4], fill=(30, 90, 50), outline=(90, 200, 120), width=2)
    for i in range(4):
        px = x + 14 + i * (w - 28) // 3
        d.line([(px, y - 12), (px, y)], fill=(90, 200, 120), width=4)
        d.line([(px, y + h), (px, y + h + 12)], fill=(90, 200, 120), width=4)
    for j in range(2):
        py = y + 16 + j * (h - 32)
        d.line([(x - 12, py), (x, py)], fill=(90, 200, 120), width=4)
        d.line([(x + w, py), (x + w + 12, py)], fill=(90, 200, 120), width=4)


def masthead(d):
    d.text((36, 26), "THE WORLD TODAY", font=SERIF_B(66), fill=INK)
    rule(d, 36, 112, 952, INK, 4)
    d.text((36, 124), "MONDAY 23 NOVEMBER 2026", font=SANS_B(24), fill=RED)
    d.text((560, 124), "WORLD EDITION  •  FIVE STORIES", font=SANS_B(20), fill=INK)
    rule(d, 36, 158, 952, INK, 2)


def lead_story(d):
    y = 176
    y = kicker(d, 36, y, "CLIMATE  •  ANTALYA, TURKEY")
    y = headline(d, 36, y, "Climate talks collapse as fossil-fuel wording is dropped", 38, 600, 46)
    y = draw_para(d, 36, y + 8, "Two weeks of talks in Turkey ended on Sunday with no deal, two days past schedule, after the EU and island states refused a text silent on fossil fuels.", SANS(18), 600, 25)
    y = draw_para(d, 36, y + 6, "On Monday the blame game began, with Saudi Arabia's role in blocking the deal under scrutiny.", SANS(18), 600, 25)
    draw_globe(d, 830, 292, 92)
    d.text((738, 398), "COP31 ends in failure", font=SANS_B(16), fill=BLUE)
    rule(d, 36, 486, 952, INK, 2)


def middle_row(d):
    y0 = 504
    d.line([(512, 504), (512, 712)], fill=GREY, width=1)
    y = kicker(d, 36, y0, "UKRAINE WAR  •  MEDITERRANEAN")
    y = headline(d, 36, y, "Kyiv says its drones sank a Russian warship off Libya", 26, 440, 33)
    y = draw_para(d, 36, y + 6, "President Zelenskyy said on Monday that Ukrainian sea drones sank a Russian navy vessel moored at Benghazi. The UN called for an independent inquiry.", SANS(16), 440, 22)
    draw_ship(d, 110, 662, 260, 34)
    y = kicker(d, 548, y0, "UKRAINE WAR  •  KYIV")
    y = headline(d, 548, y, "Russian strikes kill at least 15 around Kyiv", 26, 440, 33)
    y = draw_para(d, 548, y + 6, "Russian bombardment of the Kyiv region killed at least 15 people, officials said. Rescuers pulled a boy alive from the rubble of a hit apartment block.", SANS(16), 440, 22)
    draw_rubble(d, 630, 664, 250, 40)
    rule(d, 36, 712, 952, INK, 2)


def bottom_row(d):
    y0 = 730
    d.line([(512, 730), (512, 918)], fill=GREY, width=1)
    y = kicker(d, 36, y0, "INDONESIA")
    y = headline(d, 36, y, "Factory fire kills 24; about 30 still missing", 25, 440, 31)
    y = draw_para(d, 36, y + 6, "A blaze tore through a sweets factory in Cikande, west of Jakarta, on Saturday evening. Rescuers searched unstable wreckage on Monday for around 30 people unaccounted for.", SANS(16), 440, 22)
    draw_flame(d, 250, 900, 16)
    y = kicker(d, 548, y0, "BUSINESS  •  ARTIFICIAL INTELLIGENCE")
    y = headline(d, 548, y, "Nvidia brings back Jensen Huang as chief executive", 25, 440, 31)
    y = draw_para(d, 548, y + 6, "Eleven days after he resigned, the board reinstated Huang on Monday, saying it was confident he posed no national security risk. Shares leapt by about a third.", SANS(16), 440, 22)
    draw_chip(d, 710, 894, 120, 24)


def ticker(d):
    d.rectangle([0, 930, 1024, 986], fill=INK)
    line = "ALSO TODAY  —  Houthis claim a strike on a Saudi refinery at Rabigh  •  EU proposes a 22nd sanctions package  •  BepiColombo reaches Mercury orbit  •  Democrats take largest US House majority since 1992"
    lines = wrap_text(line, SANS_B(15), 952)
    yy = 942
    for line in lines:
        d.text((36, yy), line, font=SANS_B(15), fill=(250, 244, 230))
        yy += 21
    d.text((36, 994), "Events of Monday 23 November 2026, as reported that day.", font=SANS(14), fill=GREY)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1023, 1023], outline=INK, width=4)
    masthead(d)
    lead_story(d)
    middle_row(d)
    bottom_row(d)
    ticker(d)
    return img


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    build().save(os.path.join(here, "entry.png"), optimize=True)
