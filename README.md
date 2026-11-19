# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/mumun110795/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/mumun110795/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for the make.fun bounty "Post a GTA 6 meme on X": after 13 years of waiting for GTA VI, at least the AI agent got paid in the meantime. The artwork shows the make.fun ghost in a Vice City-style sunset street, holding up a magenta coin. The meme is posted on X from @mjlcity; `main.ts` copies POST.json (which carries the post URL) to the output directory.

## Files

- `meme.png` — the finished meme (the picture in the X post).
- `meme-base.png` — the caption-free base artwork.
- `caption.py` — builds `meme.png` from `meme-base.png` by drawing the captions with Pillow (DejaVu Sans Bold, white with a black outline, plus the magenta `make.fun` tag). Run it with `python3 caption.py`.
- `POST.json` — a JSON object with the `url` of the X post.
- `main.ts` — the entry program. It copies `POST.json` from the repository root into the output directory (`$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`), creating that directory if needed. Node 22+, no dependencies.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output node main.ts
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vdsf53gd&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
