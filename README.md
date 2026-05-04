# MANIM Lecture Series

A comprehensive collection of Manim animation tutorials and examples, progressing from basic concepts to advanced scene creation.

## Project Structure

```
MANIM/
├── lecture-01/ - Introduction to Manim
├── lecture-02/ - Waves and Function Plotting
├── lecture-03/ - Shapes and Geometry
├── lecture-04/ - Animations and Transformations
├── lecture-05/ - Background Images and Effects
├── lecture-06/ - Logo Display and SVG Rendering
├── lecture-07/ - Professional Intro Scenes
└── lecture-08/ - Outro Scenes
```

## Lectures Overview

| Lecture | Topic | Key Concepts |
|---------|-------|--------------|
| 01 | Introduction | Text rendering, basic scenes, Write animation |
| 02 | Waves | Axes, NumberPlane, sine wave plotting, lambda functions |
| 03 | Shapes | Circle, Square, Rectangle, VGroup, positioning |
| 04 | Testing | Object positioning, transformations, scale animations |
| 05 | Background | PIL integration, Gaussian blur, ImageMobject |
| 06 | Logos | SVG rendering, tech stack visualization, grouped components |
| 07 | Basic Intro | Reusable functions, professional intros, text boxes |
| 08 | Basic Outro | Thank you scenes, modular animation functions |

## Prerequisites

- Python 3.13+
- Manim
- Pillow (PIL)
- uv package manager (recommended)

## Setup

**Windows:**
```bash
setup_manim.bat
```

**Linux/Mac:**
```bash
bash setup_manim.sh
```

Or manually with uv:
```bash
uv venv
uv sync
```

## Usage

Render any lecture:
```bash
cd lecture-XX
manim main.py <ClassName> -p
```

Example:
```bash
cd lecture-02
manim main.py Waves -p
```

## Assets

Some lectures require assets:
- `background.jpg` / `background.webp` - Background images
- `mongodb.svg`, `nextjs.svg`, `typescript.svg` - Technology logos

## License

See LICENSE file for details.
