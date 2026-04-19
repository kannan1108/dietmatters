with open("/Users/kayz/sites/dietmatters/index.html","r") as f:
    c=f.read()
c=c.replace('<div class="photo-card">','<div class="photo-card" style="position:relative"><span style="position:absolute;bottom:12px;left:14px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.85);background:rgba(0,0,0,.4);padding:4px 10px;z-index:2">Before · Sept 2025 · 193 lbs</span>',1)
c=c.replace('<div class="photo-card">','<div class="photo-card" style="position:relative"><span style="position:absolute;bottom:12px;left:14px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.85);background:rgba(0,0,0,.4);padding:4px 10px;z-index:2">After · March 2026 · 167 lbs</span>',1)
with open("/Users/kayz/sites/dietmatters/index.html","w") as f:
    f.write(c)
print("Done")
