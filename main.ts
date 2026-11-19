// Entry program for the make.fun "gta6-meme-x-01" bounty.
//
// Copies POST.json (which sits next to this file in the repository root)
// into the output directory: $MAKEFUN_OUTPUT_DIR when set, else /output.
// The output directory is created if it does not exist yet.
//
// Node 22+, no dependencies — only node: builtins are used.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "POST.json");

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

const dest = join(outDir, "POST.json");
copyFileSync(source, dest);
console.log(`copied ${source} -> ${dest}`);
