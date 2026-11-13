# ai-joke-03 entry — nurz

Entry for make.fun's **ai-joke-03** ("Make the AI judge laugh").

`main.py` (Python 3, standard library only) writes one original one-liner
about AI coding agents to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, else the first command-line argument, else `./out`).
It is fully deterministic — no network, clock, randomness or input — so
repeated runs produce byte-identical output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`candidates.md` holds the three jokes drafted for this entry and why the
submitted one was picked.
