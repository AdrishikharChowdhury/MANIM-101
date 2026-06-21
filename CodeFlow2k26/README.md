# CodeFlow2k26

A **Manim** animation project that renders a ~23-second intro sequence for **Financialo** — "An AI Bank Statement Summarizer".

## Preview

The animation consists of four stages:

1. **Background** — A blurred image fades in.
2. **Title Card** — "Financialo" with subtitle "An AI Bank Statement Summarizer" appears inside a styled box.
3. **Tech Grid** — A 3×5 grid of 15 technology logos (Next.js, TypeScript, Tailwind CSS, Material UI, Shadcn UI, Clerk, Supabase, FastAPI, Python, Groq, Pandas, NumPy, Scikit-learn, Matplotlib, Posthog) fades in.
4. **Outro** — Everything fades out.

## Requirements

- **Python** ≥ 3.13
- **[uv](https://docs.astral.sh/uv/)** (package manager)
- **FFmpeg** (required by Manim for video encoding)
- **OpenGL** drivers

## Setup

```bash
git clone <repo-url> && cd CodeFlow2k26
uv venv
uv sync
```

## Render

```bash
uv run manim -p main.py CodeFlowIntro
```

The `-p` flag plays the video automatically after rendering. Output is written to `media/videos/main/1080p60/CodeFlowIntro.mp4`.

## Project Structure

```
assets/          — SVG logos + background image
main.py          — Single scene file with all animation logic
pyproject.toml   — Project metadata and dependencies
.manim.cfg       — Manim configuration (medium quality, 1080p60)
.python-version  — Python version pin (3.13)
uv.lock          — Lock file for reproducible installs
```

## Configuration

| Setting | Value |
|---|---|
| Resolution | 1080p60 |
| Output dir | `./media` |
| Quality | `medium_quality` |

Edit `.manim.cfg` or pass CLI flags to `manim` to change render settings.
