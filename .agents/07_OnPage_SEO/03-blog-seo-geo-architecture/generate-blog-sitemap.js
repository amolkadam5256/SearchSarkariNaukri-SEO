/**
 * generate-blog-sitemap.js
 *
 * Regenerates sitemap-blogs.xml from the published-posts table.
 * Run this on: publish webhook, CMS save hook, and as a nightly cron
 * fallback in case a webhook is missed.
 *
 * Usage:
 *   node generate-blog-sitemap.js
 *
 * Requires a `getPublishedPosts()` implementation wired to your DB —
 * stub below shows the expected shape.
 */

const fs = require("fs");
const path = require("path");

const SITE_URL = "https://www.searchsarkarinaukri.com";
const OUTPUT_PATH = path.join(__dirname, "public", "sitemap-blogs.xml");
const MAX_URLS_PER_FILE = 45000; // safety margin under the 50,000 spec limit

/**
 * Replace with your real DB call. Must return only posts that are:
 *  - published (not draft)
 *  - not noindex
 * Shape: { slug, updatedAt, createdAt }
 */
async function getPublishedPosts() {
  // Example (Prisma-style pseudocode):
  // return prisma.post.findMany({
  //   where: { status: "published", noindex: false },
  //   select: { slug: true, updatedAt: true, createdAt: true },
  // });
  throw new Error("Wire getPublishedPosts() to your DB before running.");
}

function toIsoDate(d) {
  return new Date(d).toISOString().split("T")[0];
}

function buildUrlEntry(post) {
  const lastmod = toIsoDate(post.updatedAt || post.createdAt);
  return `  <url>
    <loc>${SITE_URL}/blogs/${post.slug}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>`;
}

async function main() {
  const posts = await getPublishedPosts();

  if (posts.length > MAX_URLS_PER_FILE) {
    console.warn(
      `⚠ ${posts.length} posts exceeds the single-file safety margin (${MAX_URLS_PER_FILE}). ` +
        `Split into sitemap-blogs-1.xml, sitemap-blogs-2.xml, etc., and list both in sitemap.xml.`
    );
  }

  const urls = posts.map(buildUrlEntry).join("\n");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>
`;

  fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
  fs.writeFileSync(OUTPUT_PATH, xml, "utf8");
  console.log(`✓ Wrote ${posts.length} URLs to ${OUTPUT_PATH}`);
}

main().catch((err) => {
  console.error("Failed to generate blog sitemap:", err);
  process.exit(1);
});

/**
 * sitemap.xml (the index file) does NOT need to change when this runs —
 * it already references sitemap-blogs.xml by filename per your current
 * setup. Only the contents of sitemap-blogs.xml need regenerating.
 *
 * Wire this into:
 *   1. Your publish/update API route — call generateBlogSitemap() after
 *      a post's status flips to "published" or its content is edited.
 *   2. A nightly cron as a safety net.
 *   3. (Optional) GSC Sitemaps report → "Resubmit" after a bulk import,
 *      to nudge faster recrawl — not required for normal operation.
 */
