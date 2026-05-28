import type { QuartzComponent, QuartzComponentProps, QuartzComponentConstructor } from "@quartz-community/types"

const DISPLAY_NAMES: Record<string, string> = {
  powerbi: "Power BI",
  css: "CSS",
  "claude-code": "Claude Code",
  obsidian: "Obsidian",
  bases: "Bases",
  productivity: "Productivity",
}

function pathToRoot(slug: string): string {
  const depth = (slug ?? "").split("/").filter(Boolean).length
  return depth === 0 ? "." : Array(depth).fill("..").join("/")
}

interface Options {
  maxPills: number
}

export default ((opts?: Partial<Options>) => {
  const maxPills = opts?.maxPills ?? 5

  const SiteNav: QuartzComponent = ({ fileData, allFiles, cfg }: QuartzComponentProps) => {
    const base = pathToRoot(fileData.slug as string)

    // Count tag frequencies across all files
    const tagCounts: Record<string, number> = {}
    for (const f of allFiles) {
      const tags = (f.frontmatter?.tags ?? []) as string[]
      for (const tag of tags) {
        const t = tag.toLowerCase().replace(/\s+/g, "-")
        tagCounts[t] = (tagCounts[t] ?? 0) + 1
      }
    }

    const topTags = Object.entries(tagCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, maxPills)
      .map(([slug]) => ({ slug, label: DISPLAY_NAMES[slug] ?? slug }))

    return (
      <div class="site-nav">
        <a class="site-nav-logo" href={`${base}/`}>
          <img src={`${base}/static/icon.png`} alt="logo" width="28" height="28" />
          <span>{cfg?.pageTitle ?? "LeanProductivity"}</span>
        </a>
        <nav class="site-nav-pills">
          {topTags.map(({ slug, label }) => (
            <a key={slug} class="site-nav-pill" href={`${base}/tags/${slug}`}>
              {label}
            </a>
          ))}
        </nav>
      </div>
    )
  }

  SiteNav.css = `
    .site-nav {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex: 1;
      min-width: 0;
    }

    .site-nav-logo {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      text-decoration: none;
      font-weight: 700;
      font-size: 1rem;
      color: var(--dark);
      white-space: nowrap;
    }

    .site-nav-logo img {
      border-radius: 4px;
    }

    .site-nav-pills {
      display: flex;
      gap: 0.5rem;
      flex-wrap: nowrap;
      overflow: hidden;
    }

    .site-nav-pill {
      padding: 0.25rem 0.75rem;
      border-radius: 999px;
      border: 1px solid var(--lightgray);
      font-size: 0.85rem;
      text-decoration: none;
      color: var(--dark);
      white-space: nowrap;
    }

    .site-nav-pill:hover {
      background: var(--highlight);
      border-color: var(--secondary);
    }
  `

  return SiteNav
}) satisfies QuartzComponentConstructor<Partial<Options>>
