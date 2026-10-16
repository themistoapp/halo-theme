# Writes themes/halo.yaml: python3 tools/build.py themes/halo.yaml. Shared colours live in SHARED; each theme only sets its page, card and shadow.
import sys
SHARED = {
  "light": {
    "primary-text-color": "#1b1b1f", "secondary-text-color": "#5c5c66", "text-primary-color": "#ffffff", "disabled-text-color": "#9a9aa4",
    "divider-color": "rgba(0, 0, 0, .10)",
    "primary-color": "#1b1b1f", "accent-color": "#2f7bff", "switch-checked-color": "#2f7bff", "slider-color": "#2f7bff",
    "card-background-color": "#ffffff", "ha-card-background": "#ffffff",
    "app-header-text-color": "#1b1b1f", "sidebar-text-color": "#1b1b1f", "sidebar-icon-color": "#5c5c66",
    "sidebar-selected-icon-color": "#1b1b1f", "sidebar-selected-text-color": "#1b1b1f",
    "state-icon-color": "#5c5c66", "state-light-active-color": "#c28a0c", "state-switch-active-color": "#2f7bff",
    "state-climate-heat-color": "#e8742f", "state-climate-cool-color": "#2f86cf", "state-lock-locked-color": "#1f9d63", "state-lock-unlocked-color": "#d6453d",
    "success-color": "#1f9d63", "warning-color": "#b45f06", "error-color": "#c2362b", "info-color": "#2f7bff",
  },
  "dark": {
    "primary-text-color": "#ececf0", "secondary-text-color": "#9a9aa6", "disabled-text-color": "#5e6270",
    "divider-color": "rgba(255, 255, 255, .10)",
    "primary-color": "#ececf0", "accent-color": "#6aa3ff", "switch-checked-color": "#6aa3ff", "slider-color": "#6aa3ff",
    "ha-card-box-shadow": "0 14px 36px -4px rgba(0, 0, 0, .55), 0 3px 8px rgba(0, 0, 0, .35)",
    "app-header-text-color": "#ececf0", "sidebar-text-color": "#ececf0", "sidebar-icon-color": "#9a9aa6",
    "sidebar-selected-icon-color": "#ececf0", "sidebar-selected-text-color": "#ececf0",
    "state-icon-color": "#9a9aa6", "state-light-active-color": "#f2b84a", "state-switch-active-color": "#6aa3ff",
    "state-climate-heat-color": "#ff9a5c", "state-climate-cool-color": "#6cc3ec", "state-lock-locked-color": "#4cc9a0", "state-lock-unlocked-color": "#ff7b72",
    "success-color": "#4cc9a0", "warning-color": "#f4a36a", "error-color": "#ff7b72", "info-color": "#6aa3ff",
  },
}
def page(bar, second, bg, card=None, shadow=None, text_on=None):
  d = {"primary-background-color": bar, "secondary-background-color": second, "lovelace-background": bg + " fixed",
       "app-header-background-color": bar, "sidebar-background-color": bar}
  if card: d["card-background-color"] = card; d["ha-card-background"] = card
  if shadow: d["ha-card-box-shadow"] = shadow
  if text_on: d["text-primary-color"] = text_on
  return d
THEMES = [
  ("Halo - Bloom", "Halo's own bloom. Light: a peach glow top left and lilac bottom right on near white. Dark: graphite with an aurora green glow top left and midnight blue bottom left.",
   page("#f7f3f2", "#efeaea", "radial-gradient(ellipse 75% 60% at 0% 0%, #fbd9bd 0%, transparent 70%), radial-gradient(ellipse 80% 70% at 100% 100%, #d9d2f5 0%, transparent 70%), linear-gradient(160deg, #fcf9f7 0%, #f5f2f6 100%)",
        shadow="0 14px 36px -4px rgba(60, 30, 50, .14), 0 3px 8px rgba(60, 30, 50, .07)"),
   page("#11151a", "#171c22", "radial-gradient(ellipse 80% 55% at 0% 0%, #0f5a4a 0%, transparent 70%), radial-gradient(ellipse 85% 60% at 0% 100%, #16377a 0%, transparent 70%), linear-gradient(160deg, #1a1d23 0%, #12161d 55%, #0e1219 100%)",
        card="#1a1d24", text_on="#11151a")),
  ("Halo - Basic", "Quiet and neutral. Light: almost white with the faintest grey corner. Dark: plain graphite, lighter at the top left.",
   page("#f6f6f7", "#ececef", "radial-gradient(ellipse 80% 60% at 100% 100%, #e3e5e9 0%, transparent 70%), linear-gradient(160deg, #ffffff 0%, #f6f6f8 60%, #eceef1 100%)",
        shadow="0 14px 36px -4px rgba(20, 20, 40, .12), 0 3px 8px rgba(20, 20, 40, .06)"),
   page("#141517", "#1c1d21", "radial-gradient(ellipse 85% 55% at 10% 0%, #2c2d32 0%, transparent 72%), linear-gradient(160deg, #1c1d21 0%, #131417 55%, #0b0b0d 100%)",
        card="#1d1e22", text_on="#141517")),
]
q = lambda v: '"' + v + '"'
out = ["# Halo themes for Home Assistant, to go with Halo Cards (https://github.com/themistoapp/halo-cards).",
       "# Each theme appears separately under Profile → Theme. Use mode Auto to follow day and night.", "#",
       "# Install with HACS (category Theme), or copy this file to config/themes/. configuration.yaml needs:",
       "#   frontend:", "#     themes: !include_dir_merge_named themes", "# A Halo Backdrop card on a view paints its sky over these backgrounds.", ""]
for name, note, light, dark in THEMES:
  out += [f"# {note}", f"{q(name)}:", "  ha-card-border-radius: 12px", "  ha-card-border-width: 0px", "  modes:"]
  for mode, own in (("light", light), ("dark", dark)):
    vals = {**SHARED[mode], **own}
    out.append(f"    {mode}:")
    out += [f"      {k}: {q(v)}" for k, v in vals.items()]
  out.append("")
open(sys.argv[1], "w").write("\n".join(out))
