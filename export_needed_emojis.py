import fitz, os

os.makedirs('build_assets/png_icons', exist_ok=True)

emojis = {
    'droplet': '1f4a7',       # 💧 Ch1 / Water
    'brick': '1f9f1',         # 🧱 Ch2 / Membrane
    'sugar': '1f36c',         # 🍬 Ch3 / Candy / Carbohydrates
    'bread': '1f35e',         # 🍞 Ch4 / Polysaccharides
    'dna': '1f9ec',           # 🧬 Ch8 & Ch9 / DNA
    'meat': '1f969',          # 🥩 Ch5 & Ch6 / Protein / Amino acids
    'blood': '1fa78',         # 🩸 Ch7 / Hemeproteins / Blood
    'oil': '1fad2',           # 🫒 Ch10 / Lipids / Oil
    'lightning': '26a1',      # ⚡ Ch11 / Enzymes / Energy
    'pill': '1f48a',          # 💊 Ch12 / Vitamins
    'chart': '1f4ca',         # 📊 Summary
    'checklist': '2705',      # ✅ Checklist
    'target': '1f3af',        # 🎯 Analogy
    'key': '1f511',           # 🔑 Tip
    'warning': '26a0',        # ⚠️ Warning
    'bulb': '1f4a1',          # 💡 Mnemonic
    'pin': '1f4cc',           # 📌 Summary Box
    'star': '2b50',           # ⭐ Star
}

for name, code in emojis.items():
    svg_file = f'build_assets/twemoji/package/{code}.svg'
    if os.path.exists(svg_file):
        doc = fitz.open(svg_file)
        pix = doc[0].get_pixmap(dpi=300)
        out_png = f'build_assets/png_icons/{name}.png'
        pix.save(out_png)
        print(f"Exported {name} -> {out_png}")
    else:
        print(f"NOT FOUND: {svg_file}")

print("All icons exported.")
