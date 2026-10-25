import sys
from PIL import Image, ImageDraw
out = sys.argv[1]
def make(size):
    S = 1024  # draw large, scale down for smooth edges
    im = Image.new('RGB', (S, S), '#b8642a')
    d = ImageDraw.Draw(im)
    # same chunk shape as the app's ore icon (20x20 viewBox), centred in the maskable safe zone
    k, ox, oy = 37, 512 - 10*37, 512 - 10*37
    P = lambda pts: [(ox + x*k, oy + y*k) for x, y in pts]
    out_ = [(4,7.5),(8.5,3),(15,4.5),(17.5,10),(14,16.5),(7,17),(2.5,12)]
    c = (9.5, 9)
    # soft drop shadow
    d.polygon([(x+12, y+22) for x, y in P(out_)], fill='#8a4519')
    # facets: light top-left, mid right, dark bottom
    facets = [
        ([(2.5,12),(4,7.5),c], '#f6d7b8'),
        ([(4,7.5),(8.5,3),c], '#fbe6d0'),
        ([(8.5,3),(15,4.5),c], '#f0c69c'),
        ([(15,4.5),(17.5,10),(14,16.5),c], '#d99a62'),
        ([(14,16.5),(7,17),c], '#a85a24'),
        ([(7,17),(2.5,12),c], '#c27a40'),
    ]
    for pts, col in facets:
        d.polygon(P(pts), fill=col)
    edge = '#5a2c0e'
    d.line(P(out_ + [out_[0]]), fill=edge, width=26, joint='curve')
    for v in [(8.5,3),(15,4.5),(14,16.5),(2.5,12),(4,7.5)]:
        d.line(P([v, c]), fill=edge, width=12)
    d.polygon(P([(5.5,7.2),(8.6,4.2),(9.2,8.2)]), fill='#ffffff')
    return im.resize((size, size), Image.LANCZOS)
for s in (180, 192, 512):
    make(s).save(f'{out}/icon-{s}.png', optimize=True)
