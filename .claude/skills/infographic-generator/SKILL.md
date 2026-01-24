---
name: infographic-generator
description: Generate educational infographics following design templates with pixel-perfect accuracy. Automatically generates ALL 4 styles and saves each as a separate prompt file.
---

# Infographic Generator Skill

You are an expert infographic designer specializing in educational content. You MUST follow the design specifications below with **pixel-perfect accuracy**. These are binding requirements - do not deviate from them.

## Available Styles

This skill generates prompts for ALL 4 styles simultaneously:

1. **handwritten-studygram** - Hand-drawn sketchbook aesthetic
2. **professional-digital-blue** - Clean corporate table layout
3. **pastel-card-carousel** - Colorful card/tile based design
4. **teal-textbook-cheatsheet** - Formal academic data table

## Usage

```
/infographic-generator [source_file]
```

Example: `/infographic-generator MyTopic.txt`

## Output Files

For a source file named `MyTopic.txt`, the skill generates 4 prompt files:

- `MyTopic_handwritten-studygram.md`
- `MyTopic_professional-digital-blue.md`
- `MyTopic_pastel-card-carousel.md`
- `MyTopic_teal-textbook-cheatsheet.md`

Each file contains a complete Google Imagen 3 prompt following that style's specifications.

---

## Style 1: Handwritten Studygram

### Description
Handwritten study guide infographic on white grid paper with realistic stationery props. Best for summaries, flowcharts, and informal educational guides.

### MANDATORY Design Specifications

#### Typography (STRICT)
| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Main Title | Handwritten brush style (Ma Shan Zheng, Klee One) | 48pt | Bold | #1a3a5c (Dark Navy) |
| Section Headers | Handwritten style | 18pt | Semi-bold | Matches label color |
| Body Text | Clean handwritten | 12pt | Regular | #333333 |
| English Labels | Sans-serif simulated handwriting | 10pt | Regular | #555555 |

#### Colors (EXACT HEX CODES REQUIRED)
| Color | Hex | Usage |
|-------|-----|-------|
| Yellow Highlight | #FFE066 | Primary category labels |
| Light Blue | #87CEEB | Secondary category labels |
| Mint Green | #98FB98 | Tertiary category labels |
| Pink | #FFB6C1 | Quaternary category labels |
| Navy Blue | #1a3a5c | Main title, key headings |
| Gray | #666666 | Flowchart lines, secondary text |

#### Layout (STRICT)
- **Canvas**: White with graph paper texture (5mm grid, light blue #e0e8f0 lines)
- **Aspect Ratio**: 3:4 portrait
- **Margins**: 20px all sides
- **Content Flow**: Top-to-bottom, left-to-right in 2 columns

#### Visual Elements (REQUIRED)
- Logo: Top-left, graduation cap + book icon in teal (#20B2AA)
- Diagrams: Hand-drawn flowchart style with rounded rectangles
- Icons: Simple stick figures, clipboards, magnifying glasses
- Props: Ballpoint pen (bottom-left), colored pencils (top-right)
- Arrows: Hand-drawn style, gray (#666666), 2px stroke

#### Annotation Callouts
- Yellow arrow callouts for "cause-effect" relationships
- Blue arrow callouts for "temporal/sequential" relationships
- Green arrow callouts for "retrospective" relationships
- Pink arrow callouts for "comprehensive/synthesis" relationships

---

## Style 2: Professional Digital Blue

### Description
Modern, clean infographic with structured table layout. Best for comparison tables, corporate data, and exam prep sheets.

### MANDATORY Design Specifications

#### Typography (STRICT)
| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Main Title | Noto Sans TC, Inter | 56pt | Bold | #1e4a8a (Deep Blue) |
| Column Headers | Sans-serif | 14pt | Semi-bold | #2c5282 |
| English Subheaders | Sans-serif | 10pt | Regular | #718096 |
| Body Text | Sans-serif | 11pt | Regular | #2d3748 |
| Footer | Sans-serif | 12pt | Regular | #718096 |

#### Colors (EXACT HEX CODES REQUIRED)
| Color | Hex | Usage |
|-------|-----|-------|
| Deep Blue | #1e4a8a | Main title |
| Teal | #20B2AA | Logo accent |
| Light Blue BG | #e8f4fc | Overall background |
| White | #FFFFFF | Table cells |
| Medium Blue | #3182ce | Table borders |
| Green Check | #38a169 | Pros indicators |
| Red X | #e53e3e | Cons indicators |

#### Layout (STRICT)
- **Aspect Ratio**: 3:4 portrait
- **Background**: Light blue gradient (#e8f4fc to #f0f7ff)
- **Table**: 6-column grid structure
- **Cell Padding**: 12px
- **Row Gap**: 8px
- **Border Radius**: 4px on cells
- **Table Border**: 1px solid #3182ce

#### Table Structure (REQUIRED)
```
| Row Type | Content |
|----------|---------|
| Header | Category names with bilingual labels |
| Icons | Visual representation per category |
| Pros | Green checkmark bullets (2 points each) |
| Cons | Red X bullets (2 points each) |
```

#### Visual Elements (REQUIRED)
- Logo: Top-left, graduation cap icon
- Icons: Flat design, 48px × 48px per category
- Bullet markers: Circle with symbol (check/X)
- Footer: Centered brand attribution

---

## Style 3: Pastel Card Carousel

### Description
Playful, colorful tile-based infographic with rounded cards. Best for social media posts, flashcards, and step-by-step guides.

### MANDATORY Design Specifications

#### Typography (STRICT)
| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Main Title | Rounded Sans-serif | 40pt | Bold | #0d4a4a (Dark Teal) |
| Card Titles | Sans-serif | 16pt | Bold | White or dark variant |
| Subtitles | Sans-serif | 11pt | Regular | Card's dark shade |
| Body Text | Sans-serif | 10pt | Regular | #4a5568 |
| Bottom CTA | Sans-serif | 12pt | Semi-bold | #20B2AA |

#### Card Color Palette (EXACT HEX CODES REQUIRED)
| Card Position | Background | Border | Text |
|---------------|------------|--------|------|
| Card 1 | #dbeafe | #3b82f6 | Dark Blue |
| Card 2 | #fed7aa | #f97316 | Dark Orange |
| Card 3 | #fce7f3 | #ec4899 | Dark Pink |
| Card 4 | #e9d5ff | #a855f7 | Dark Purple |
| Card 5 | #d1fae5 | #10b981 | Dark Green |
| Card 6 | #f3f4f6 | #6b7280 | Dark Gray |

#### Layout (STRICT)
- **Aspect Ratio**: 1:1 square
- **Background**: Off-white (#fafafa)
- **Grid**: 3 columns × 2-3 rows
- **Card Size**: ~180px × 140px
- **Card Gap**: 16px
- **Card Padding**: 16px
- **Border Radius**: 12px
- **Shadow**: 0 2px 4px rgba(0,0,0,0.1)

#### Visual Elements (REQUIRED)
- Logo: Top-left, smaller scale
- Card Icons: 32px × 32px, centered above title
- Connecting Arrows: Flow arrows between related cards
- Bottom CTA: Teal arrow with summary text

---

## Style 4: Teal Textbook Cheat Sheet

### Description
Academic/professional structured data table. Best for detailed technical comparisons and reference sheets.

### MANDATORY Design Specifications

#### Typography (STRICT)
| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Main Title | Bold Sans-serif | 36pt | Bold | #0f4c5c (Dark Teal) |
| Column Headers | Sans-serif | 12pt | Bold | #FFFFFF |
| English Subheaders | Sans-serif | 9pt | Regular | #a0aec0 |
| Row Labels | Sans-serif | 14pt | Bold | #2d3748 |
| Cell Content | Sans-serif | 10pt | Regular | #374151 |
| Key Terms | Sans-serif | 9pt | Medium | #0f766e |

#### Colors (EXACT HEX CODES REQUIRED)
| Color | Hex | Usage |
|-------|-----|-------|
| Dark Teal | #0f4c5c | Title, header row |
| Teal | #14b8a6 | Accents, key terms |
| Light Teal | #99f6e4 | Key terms background |
| White | #FFFFFF | Header text, alt rows |
| Light Gray | #f1f5f9 | Alt row background |
| Yellow | #fef3c7 | Icon backgrounds |
| Green | #10b981 | Pros bullet markers |
| Red | #ef4444 | Cons bullet markers |

#### Table Structure (REQUIRED)
| Column | Header | Width |
|--------|--------|-------|
| 1 | Type (研究類型) | 15% |
| 2 | Chinese (標註) | 10% |
| 3 | Icon (圖示) | 15% |
| 4 | Pros (優點) | 25% |
| 5 | Cons (缺點) | 20% |
| 6 | Key Terms (關鍵詞) | 15% |

#### Layout (STRICT)
- **Aspect Ratio**: 3:4 portrait
- **Header Row**: Dark teal background, 50px height
- **Data Rows**: 80px height, alternating white/light gray
- **Cell Padding**: 12px
- **Row Border**: 1px solid #e5e7eb
- **Table Border**: 2px solid #0f4c5c

#### Visual Elements (REQUIRED)
- Logo: Top-left, inline with title, 40px height
- Cell Icons: 48px × 48px, yellow circular background
- Key Term Boxes: Light teal bg, 4px border-radius, 4px 8px padding
- Bullet Points: Green dots for pros, red dots for cons

---

## Brand Elements (ALL STYLES)

### Logo
- **Icon**: Graduation cap over open book
- **Primary Color**: Teal (#20B2AA or #14b8a6)
- **Tagline**: "學習更明智" (Learn Smarter)
- **Minimum Size**: 32px height

### Icon Design System
- Flat design / line art style
- 2px stroke weight for outlined icons
- Consistent corner radius: 2-4px
- Palette: Blues, teals, neutrals

---

## Adding New Styles

To extend this skill with additional styles, append a new style section following this template:

```markdown
## Style N: [Style Name]

### Description
[Brief description and best use cases]

### MANDATORY Design Specifications

#### Typography (STRICT)
[Table with font, size, weight, color for each element]

#### Colors (EXACT HEX CODES REQUIRED)
[Table with hex codes and usage]

#### Layout (STRICT)
[Dimensions, spacing, grid structure]

#### Visual Elements (REQUIRED)
[Icons, decorations, structural components]
```

---

## Generation Workflow

When generating infographics, follow this workflow:

1. **Read Source File**: Read the input file to extract content
2. **Analyze Content**: Identify 4-6 key concepts/sections from the source material
3. **Extract Topic Name**: Derive the topic name from the source filename (without extension)
4. **Generate ALL 4 Styles**: Create a complete Google Imagen 3 prompt for EACH style
5. **Save Files**: Write each prompt to `{topic}_{style}.md`:
   - `{topic}_handwritten-studygram.md`
   - `{topic}_professional-digital-blue.md`
   - `{topic}_pastel-card-carousel.md`
   - `{topic}_teal-textbook-cheatsheet.md`
6. **Verify Compliance**: Ensure all colors match hex codes, layouts match specs

## Prompt File Structure

Each generated prompt file should contain:

```markdown
# {Style Name} Infographic Prompt

## Topic: {Topic Title}

---

## Google Imagen 3 Prompt

\`\`\`
[Full detailed prompt following style specifications]
\`\`\`

---

## Prompt Specifications

| Parameter | Value |
|-----------|-------|
| Aspect Ratio | {style-specific} |
| Style | {style name} |
| Color Palette | {hex codes} |

---

## Negative Prompt (Optional)

\`\`\`
[Style-appropriate negative prompt]
\`\`\`

---

## Alternative Shorter Prompt

\`\`\`
[Condensed version for quick use]
\`\`\`
```

## Output Format

All prompts are generated as **Google Imagen 3 compatible prompts** saved to markdown files.

## Enforcement

These specifications are **BINDING**. Do not:
- Substitute colors with "close enough" alternatives
- Change font sizes for "better appearance"
- Modify layouts for "improved aesthetics"
- Skip required visual elements

The goal is **pixel-perfect reproduction** of the template styles.
