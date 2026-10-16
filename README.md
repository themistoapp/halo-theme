# Halo Theme

A Home Assistant theme to go with [Halo Cards](https://github.com/themistoapp/halo-cards), so Home Assistant's own screens, cards, dialogs and sidebar match them.

![Halo theme, light and dark](images/preview.png)

- **Light:** warm white with a bright glow at the top left, deepening to soft sand.
- **Dark:** graphite deepening to midnight blue.
- Text, dividers and cards in the Halo cards' colours; 12px corners, Halo's soft shadow and no hairline border.
- Ink accent, with toggles and sliders in Halo blue.
- State colours (lights on, heating, cooling, locked, warnings) from the Halo palette.

## Install with HACS

1. HACS → ⋮ → **Custom repositories** → add `https://github.com/themistoapp/halo-theme`, category **Theme**.
2. Install **Halo Theme**.
3. Make sure `configuration.yaml` loads themes (once; restart Home Assistant after adding it):
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
4. Run the **frontend.reload_themes** action, then pick **Halo** under Profile → Theme, with the mode on Auto to follow day and night.

A Halo Backdrop card on a view paints its sky over the theme's background.

## Install by hand

Copy [themes/halo.yaml](themes/halo.yaml) (use the **Raw** button) to `config/themes/halo.yaml`, then follow steps 3 and 4.
