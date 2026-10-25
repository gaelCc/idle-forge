# Idle Forge Calc

A production calculator for War.app Idle: income, smelters, crafters and rates.

**Open it:** https://gaelcc.github.io/idle-forge/

## For friends: install on iPhone

1. Open the link above in **Safari** (it has to be Safari).
2. Tap the **Share** button (the square with an arrow).
3. Scroll down and tap **Add to Home Screen**, then **Add**.

It now opens from your home screen like an app, and works offline after the first visit.

**Your data stays on your phone.** Nothing is uploaded anywhere. Levels and recipes are saved in Safari's storage for this site, so if you clear Safari's website data, or the phone deletes it, your setup is gone.

**Back it up:** open the **Income** tab, scroll to **Export (backup)**, tap **Copy** and paste the text into Notes or a message to yourself. To restore it, or to move it to another phone, paste that text into **Import**, tap **Import** and confirm.

## For me: publishing an update

1. Edit `index.html`.
2. Open `sw.js` and bump the version on the first line, e.g. `const VERSION = 'v1';` → `'v2'`.
3. Commit and push:
   ```sh
   git add -A
   git commit -m "Describe the change"
   git push
   ```

GitHub Pages redeploys within a minute or two. The page is always fetched from the network first, so friends get the new version the next time they open the app while online. Bumping the version also refreshes the cached icons and manifest and deletes the old offline copy.

To redraw the icons: `python3 icons/make-icons.py icons` (needs Pillow).

The Scriptable version keeps working as before: when `window.__WIC` is set, data goes to the Scriptable file and the service worker is not used.
