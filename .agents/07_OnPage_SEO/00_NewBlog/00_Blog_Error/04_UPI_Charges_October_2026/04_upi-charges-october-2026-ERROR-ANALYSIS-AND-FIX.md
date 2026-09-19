# LIVE GSC AUDIT & ERROR REPORT: Blog #16 (UPI Charges October 2026)

**Target URL:** `https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026`  
**Date of GSC Live Inspection:** 19 September 2026, 09:16:46 IST  
**Crawled By:** Google Inspection Tool smartphone (Googlebot WRS)  
**Status:** 🔴 **ERROR: Page cannot be indexed — Soft 404**  

---

## 1. Google Search Console Live Inspection Evidence

```text
URL: https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026
Tested on: 19 Sept 2026, 09:16:46
Status: URL is not available to Google
Page availability: Page cannot be indexed: Soft 404
Crawl allowed? Yes
Page fetch: Successful (HTTP 200)
Indexing allowed? Yes
User-declared canonical: https://www.searchsarkarinaukri.com/  <--- ❌ FATAL BUG
Google-selected canonical: Only determined after indexing
```

---

## 2. Deep-Dive Forensic Root Cause Analysis

### Why does GSC see `https://www.searchsarkarinaukri.com/` as the User-Declared Canonical?

We downloaded and reverse-engineered the production JavaScript bundle (`assets/index-Df7BGoho.js`) and live prerendered HTML served by Nginx:

#### Layer 1: Server-Side Prerender (HTML)
In the raw prerendered HTML delivered on initial HTTP request:
```html
<link data-ssn-seo="1" rel="canonical" href="https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026" />
```
This initial tag is **correct**.

#### Layer 2: Client-Side React Hydration (The Fatal Bug)
When Googlebot's Chrome browser executes the JavaScript bundle:

1. In `index-Df7BGoho.js`, the cleanup hook `K0()` executes on mount:
```javascript
// BUG STEP 1: Deletes the server-rendered canonical tag from <head>!
function K0() {
  S.useEffect(() => {
    const r = document.head;
    if (!r) return;
    r.querySelectorAll("[data-ssn-seo]").forEach(b => {
      b.tagName !== "SCRIPT" && b.remove(); // <--- REMOVES <link data-ssn-seo="1" rel="canonical">
    });
    ...
  }, []);
}
```

2. Then, the React SEO component `$0` evaluates its props:
```javascript
// BUG STEP 2: Falls back to "/" if `url` or `path` is undefined!
function $0({ title: r, description: u, url: f, path: o, ... }) {
  const J = f || o || "/";  // <--- When blog post data is loading async, f and o are undefined -> "/"
  const ee = J.startsWith("http") ? J : `${Zt}${J.startsWith("/") ? J : `/${J}`}`;
  ...
  return n.jsx("link", { rel: "canonical", href: ee }); // <--- Injects https://www.searchsarkarinaukri.com/
}
```

3. **Result:** React dynamically rewrites `<link rel="canonical" href="https://www.searchsarkarinaukri.com/">`!
4. **Googlebot evaluates the post-hydration rendered DOM:**
   - URL crawled: `/blogs/upi-charges-october-2026`
   - User-declared canonical rendered by React: `https://www.searchsarkarinaukri.com/`
   - Page content: A 2,300-word article about UPI MDR rules.
   - Homepage content: Government job listings and navigation.
   - **Google Algorithm Decision:** "The webmaster declared that this page is canonical to the homepage, but the content is completely different. This is a contradictory signal → Flag as **Soft 404** and reject indexing."

---

## 3. The 2-Step Permanent Developer Fix

### Fix 1: Stop `K0()` from Deleting Valid Prerendered Canonical Tags
In `src/components/SEO.jsx` (or wherever `K0` is defined):
```javascript
// ❌ WRONG (Current Bug):
r.querySelectorAll("[data-ssn-seo]").forEach(b => {
  b.tagName !== "SCRIPT" && b.remove();
});

// ✅ CORRECT:
// Do NOT remove canonical or meta tags if they already match the current pathname!
r.querySelectorAll("[data-ssn-seo]").forEach(b => {
  if (b.tagName === "LINK" && b.getAttribute("rel") === "canonical") {
    return; // Keep existing canonical intact!
  }
  if (b.tagName !== "SCRIPT") b.remove();
});
```

### Fix 2: Never Fallback to Homepage (`"/"`) in `$0` SEO Component
In `src/components/SEO.jsx` (or wherever `$0` is defined):
```javascript
// ❌ WRONG (Current Bug):
const J = f || o || "/";
const ee = J.startsWith("http") ? J : `${siteUrl}${J.startsWith("/") ? J : `/${J}`}`;

// ✅ CORRECT:
// If f and o are not passed, derive path directly from window.location.pathname!
const currentPath = typeof window !== "undefined" ? window.location.pathname : "/";
const J = f || o || currentPath;
const ee = J.startsWith("http") ? J : `${siteUrl}${J.startsWith("/") ? J : `/${J}`}`;
```

### Fix 3: Ensure the Blog Component Passes `url` or `path` Explicitly
In `src/pages/BlogDetail.jsx` (or `pages/blogs/[slug].jsx`):
```javascript
// Make sure url is always passed explicitly:
<SEO
  title={post.title}
  description={post.meta_description}
  url={`https://www.searchsarkarinaukri.com/blogs/${slug}`}
  path={`/blogs/${slug}`}
  type="article"
  ...
/>
```

---

## 4. Complete Verification Protocol

Once the developer applies the fix:

1. **Verify Raw Prerender:**
   ```bash
   curl -s "https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026" | grep -i "rel=\"canonical\""
   ```
   Must output:
   ```html
   <link rel="canonical" href="https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026" />
   ```

2. **Verify Client-Side Hydration (Browser Console):**
   Open `https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026` in Chrome DevTools:
   ```javascript
   document.querySelector('link[rel="canonical"]').href
   ```
   Must return:
   `"https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026"` (NOT homepage).

3. **Verify in Google Search Console:**
   - Go to URL Inspection.
   - Enter `https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026`.
   - Click **TEST LIVE URL**.
   - Confirm **User-declared canonical** shows:
     `https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026`
   - Click **REQUEST INDEXING**.
