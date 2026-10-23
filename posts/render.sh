#!/usr/bin/env bash
# Renderiza um carrossel (seções .slide de 1080x1350) em slide-N.png.
# Uso: posts/render.sh posts/01-ecossistema/carrossel.html
set -euo pipefail
html="$(realpath "$1")"; dir="$(dirname "$html")"
n=$(grep -c '<section class="slide' "$html")
tmp="$(mktemp -d)"
# o modo headless tira 87px do viewport em relação à janela
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1080,$((n*1350+87)) \
  --screenshot="$tmp/full.png" "file://$html" 2>/dev/null
python3 -I - "$tmp/full.png" "$dir" "$n" <<'PY'
import sys
from PIL import Image
full, out, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(full).convert("RGB")
for i in range(n):
    im.crop((0, i * 1350, 1080, (i + 1) * 1350)).save(f"{out}/slide-{i + 1}.png")
print(f"{n} slides em {out}")
PY
rm -rf "$tmp"
