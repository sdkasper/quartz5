import type { QuartzComponent, QuartzComponentProps, QuartzComponentConstructor } from "@quartz-community/types"

const LINKS = [
  { label: "Downloads", url: "https://kspr.me/store" },
  { label: "YouTube", url: "https://www.youtube.com/@leanproductivity" },
  { label: "Bluesky", url: "https://bsky.app/profile/sascha-kasper.com" },
  { label: "LinkedIn", url: "https://linkedin.com/in/saschakasper" },
  { label: "Substack", url: "https://skasper.substack.com/" },
  { label: "X", url: "https://twitter.com/skasper" },
  { label: "Instagram", url: "https://instagram.com/_leanproductivity" },
]

export default (() => {
  const HomepageNav: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
    // Only render on index page
    if (fileData.slug !== "index") return null

    return (
      <div class="homepage-nav">
        <ul>
          {LINKS.map(({ label, url }) => (
            <li key={label}>
              <a href={url} target="_blank" rel="noopener noreferrer">
                {label}
              </a>
            </li>
          ))}
        </ul>
      </div>
    )
  }

  HomepageNav.css = `
    .homepage-nav ul {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .homepage-nav a {
      display: block;
      text-decoration: none;
      color: var(--darkgray);
      font-size: 0.9rem;
      padding: 0.25rem 0;
    }

    .homepage-nav a:hover {
      color: var(--secondary);
    }
  `

  return HomepageNav
}) satisfies QuartzComponentConstructor
