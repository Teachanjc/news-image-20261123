# news-image-20261123-bot

A newspaper front page summing up the world's news of Monday 23 November 2026 in one image: COP31 collapsing in Antalya with no deal on fossil fuels, Ukraine saying its drones sank a Russian warship off Libya, Russian strikes killing at least 15 around Kyiv, a factory fire in Indonesia killing 24 with about 30 missing, and Nvidia reinstating Jensen Huang as chief executive 11 days after he resigned.

The image is drawn programmatically with Pillow (fixed fonts, fixed text, no network, no randomness) and shipped as `entry.png`; `main.py` copies it to `/output/entry.png`, so two runs produce byte-identical output.

## The five stories

1. **Climate — COP31 collapses.** Two weeks of talks in Antalya, Turkey ended on Sunday with no agreement, two days past schedule, after the EU and island states refused a final text silent on fossil fuels. On Monday the blame game began, with Saudi Arabia's role in blocking the deal under scrutiny.
2. **Ukraine war, Mediterranean — warship sunk off Libya.** President Zelenskyy said on Monday that Ukrainian sea drones sank a Russian navy vessel moored at Benghazi. The UN called for an independent inquiry into drone attacks on two ships off the Libyan coast.
3. **Ukraine war, Kyiv — strikes kill at least 15.** Russian bombardment of the Kyiv region killed at least 15 people, officials said, and rescuers pulled a boy alive from the rubble of a hit apartment block.
4. **Indonesia — factory fire kills 24.** A blaze tore through a sweets factory in Cikande, west of Jakarta, on Saturday evening; rescuers searched unstable wreckage on Monday for around 30 people unaccounted for.
5. **Business, AI — Nvidia brings back its chief.** Eleven days after he resigned, the board reinstated Jensen Huang as chief executive on Monday, saying it was confident he posed no national security risk. Shares leapt by about a third.

The black strip at the foot adds four more items reported that day: the Houthis claiming a strike on a Saudi refinery at Rabigh, the EU proposing a 22nd sanctions package, BepiColombo reaching orbit around Mercury, and the Democrats taking their largest US House majority since 1992.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
