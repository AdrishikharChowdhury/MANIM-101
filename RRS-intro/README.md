# RRS Intro

Manim title card for the **Round-Robin Scheduling Simulation** project — a Java console
application that schedules tasks using a time quantum derived from their average
execution time.

## Scene

- `RRS_Intro` — animated intro card with a blurred background, title, subtitle,
  project details, and the Java logo.
- Uses `assets/background.jpg` (blurred with Pillow) and `assets/java.svg`.

## Render

```bash
bash run/run.sh RRS_Intro
```

Or directly:

```bash
uv run manim -pqh src/rrs_intro/__init__.py RRS_Intro
```

The rendered video is written to `media/videos/__init__/1080p60/RRS_Intro.mp4`.
