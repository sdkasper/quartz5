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

// src/components/HomepageNav.tsx
var LINKS = [
  { label: "Downloads", url: "https://kspr.me/store" },
  { label: "YouTube", url: "https://www.youtube.com/@leanproductivity" },
  { label: "Bluesky", url: "https://bsky.app/profile/sascha-kasper.com" },
  { label: "LinkedIn", url: "https://linkedin.com/in/saschakasper" },
  { label: "Substack", url: "https://skasper.substack.com/" },
  { label: "X", url: "https://twitter.com/skasper" },
  { label: "Instagram", url: "https://instagram.com/_leanproductivity" }
];
var HomepageNav_default = (() => {
  const HomepageNav = ({ fileData }) => {
    if (fileData.slug !== "index") return null;
    return /* @__PURE__ */ u2("div", { class: "homepage-nav", children: /* @__PURE__ */ u2("ul", { children: LINKS.map(({ label, url }) => /* @__PURE__ */ u2("li", { children: /* @__PURE__ */ u2("a", { href: url, target: "_blank", rel: "noopener noreferrer", children: label }) }, label)) }) });
  };
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
  `;
  return HomepageNav;
});

export { HomepageNav_default as HomepageNav };
//# sourceMappingURL=index.js.map
//# sourceMappingURL=index.js.map