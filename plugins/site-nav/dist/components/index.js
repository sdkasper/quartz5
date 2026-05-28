// node_modules/preact/dist/preact.mjs
var l;
l = { __e: function(n2, l2, u3, t2) {
  for (var i2, r2, o2; l2 = l2.__; ) if ((i2 = l2.__c) && !i2.__) try {
    if ((r2 = i2.constructor) && null != r2.getDerivedStateFromError && (i2.setState(r2.getDerivedStateFromError(n2)), o2 = i2.__d), null != i2.componentDidCatch && (i2.componentDidCatch(n2, t2 || {}), o2 = i2.__d), o2) return i2.__E = i2;
  } catch (l3) {
    n2 = l3;
  }
  throw n2;
} }, "function" == typeof Promise ? Promise.prototype.then.bind(Promise.resolve()) : setTimeout, Math.random().toString(8);

// node_modules/preact/jsx-runtime/dist/jsxRuntime.mjs
var f2 = 0;
function u2(e2, t2, n2, o2, i2, u3) {
  t2 || (t2 = {});
  var a2, c2, p2 = t2;
  if ("ref" in p2) for (c2 in p2 = {}, t2) "ref" == c2 ? a2 = t2[c2] : p2[c2] = t2[c2];
  var l2 = { type: e2, props: p2, key: n2, ref: a2, __k: null, __: null, __b: 0, __e: null, __c: null, constructor: void 0, __v: --f2, __i: -1, __u: 0, __source: i2, __self: u3 };
  if ("function" == typeof e2 && (a2 = e2.defaultProps)) for (c2 in a2) void 0 === p2[c2] && (p2[c2] = a2[c2]);
  return l.vnode && l.vnode(l2), l2;
}

// src/components/SiteNav.tsx
var DISPLAY_NAMES = {
  powerbi: "Power BI",
  css: "CSS",
  "claude-code": "Claude Code",
  obsidian: "Obsidian",
  bases: "Bases",
  productivity: "Productivity"
};
function pathToRoot(slug) {
  const depth = (slug ?? "").split("/").filter(Boolean).length;
  return depth === 0 ? "." : Array(depth).fill("..").join("/");
}
var SiteNav_default = ((opts) => {
  const maxPills = opts?.maxPills ?? 5;
  const SiteNav = ({ fileData, allFiles, cfg }) => {
    const base = pathToRoot(fileData.slug);
    const tagCounts = {};
    for (const f3 of allFiles) {
      const tags = f3.frontmatter?.tags ?? [];
      for (const tag of tags) {
        const t2 = tag.toLowerCase().replace(/\s+/g, "-");
        tagCounts[t2] = (tagCounts[t2] ?? 0) + 1;
      }
    }
    const topTags = Object.entries(tagCounts).sort((a2, b2) => b2[1] - a2[1]).slice(0, maxPills).map(([slug]) => ({ slug, label: DISPLAY_NAMES[slug] ?? slug }));
    return /* @__PURE__ */ u2("div", { class: "site-nav", children: [
      /* @__PURE__ */ u2("a", { class: "site-nav-logo", href: `${base}/`, children: [
        /* @__PURE__ */ u2("img", { src: `${base}/static/icon.png`, alt: "logo", width: "28", height: "28" }),
        /* @__PURE__ */ u2("span", { children: cfg?.pageTitle ?? "LeanProductivity" })
      ] }),
      /* @__PURE__ */ u2("nav", { class: "site-nav-pills", children: topTags.map(({ slug, label }) => /* @__PURE__ */ u2("a", { class: "site-nav-pill", href: `${base}/tags/${slug}`, children: label }, slug)) })
    ] });
  };
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
  `;
  return SiteNav;
});

export { SiteNav_default as SiteNav };
//# sourceMappingURL=index.js.map
//# sourceMappingURL=index.js.map