// BlogPostTemplate.jsx
// One shared component for every SearchSarkariNaukri blog post.
// Content (title, body blocks, FAQs, related posts) is data-driven —
// this file is the shell + SEO/schema plumbing, not per-post markup.
//
// Expects a `post` object shaped like:
// {
//   slug, title, metaTitle, metaDescription, category, categorySlug,
//   author: { name, slug, bio, expertise: [], reviewedSources: [] },
//   publishedDate, updatedDate,
//   featuredImage: { url, alt, width, height },
//   quickFacts: [{ label, value }],
//   sections: [{ id, heading, level, html }],   // H2/H3 body blocks, pre-rendered HTML/JSX
//   faqs: [{ question, answer }],
//   tags: [{ label, slug }],
//   relatedPosts: [{ slug, title, image, category }],
//   latestPosts: [{ slug, title, image, category, publishedDate }],
// }

import { Helmet } from "react-helmet-async";
import { useMemo, useState } from "react";

const SITE_URL = "https://www.searchsarkarinaukri.com";
const ORG_LOGO = `${SITE_URL}/logo.png`;

function readingTime(sections) {
  const words = sections.reduce(
    (acc, s) => acc + (s.html || "").split(/\s+/).length,
    0
  );
  return Math.max(1, Math.round(words / 200));
}

function buildSchema(post) {
  const url = `${SITE_URL}/blogs/${post.slug}`;

  const blogPosting = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": post.title,
    "description": post.metaDescription,
    "image": [post.featuredImage.url],
    "author": {
      "@type": "Person",
      "name": post.author.name,
      "url": `${SITE_URL}/author/${post.author.slug}`,
    },
    "publisher": {
      "@type": "Organization",
      "name": "SearchSarkariNaukri",
      "logo": { "@type": "ImageObject", "url": ORG_LOGO },
    },
    "datePublished": post.publishedDate,
    "dateModified": post.updatedDate || post.publishedDate,
    "mainEntityOfPage": { "@type": "WebPage", "@id": url },
  };

  const breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL },
      { "@type": "ListItem", "position": 2, "name": "Blog", "item": `${SITE_URL}/blogs` },
      {
        "@type": "ListItem",
        "position": 3,
        "name": post.category,
        "item": `${SITE_URL}/blogs?category=${post.categorySlug}`,
      },
      { "@type": "ListItem", "position": 4, "name": post.title, "item": url },
    ],
  };

  const faqPage = post.faqs?.length
    ? {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": post.faqs.map((f) => ({
          "@type": "Question",
          "name": f.question,
          "acceptedAnswer": { "@type": "Answer", "text": f.answer },
        })),
      }
    : null;

  const imageObject = {
    "@context": "https://schema.org",
    "@type": "ImageObject",
    "url": post.featuredImage.url,
    "width": post.featuredImage.width,
    "height": post.featuredImage.height,
    "caption": post.featuredImage.alt,
  };

  return { blogPosting, breadcrumb, faqPage, imageObject };
}

export default function BlogPostTemplate({ post }) {
  const [tocOpen, setTocOpen] = useState(false);
  const rt = useMemo(() => readingTime(post.sections), [post.sections]);
  const schema = useMemo(() => buildSchema(post), [post]);
  const url = `${SITE_URL}/blogs/${post.slug}`;

  return (
    <>
      <Helmet>
        <title>{post.metaTitle}</title>
        <meta name="description" content={post.metaDescription} />
        <link rel="canonical" href={url} />
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />

        <meta property="og:type" content="article" />
        <meta property="og:title" content={post.metaTitle} />
        <meta property="og:description" content={post.metaDescription} />
        <meta property="og:url" content={url} />
        <meta property="og:image" content={post.featuredImage.url} />
        <meta property="article:published_time" content={post.publishedDate} />
        <meta property="article:modified_time" content={post.updatedDate || post.publishedDate} />
        <meta property="article:author" content={post.author.name} />
        <meta property="article:section" content={post.category} />
        {post.tags?.map((t) => (
          <meta property="article:tag" content={t.label} key={t.slug} />
        ))}

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={post.metaTitle} />
        <meta name="twitter:description" content={post.metaDescription} />
        <meta name="twitter:image" content={post.featuredImage.url} />

        {/* Schema — inline in the same head pass bots/prerender see */}
        <script type="application/ld+json">{JSON.stringify(schema.blogPosting)}</script>
        <script type="application/ld+json">{JSON.stringify(schema.breadcrumb)}</script>
        <script type="application/ld+json">{JSON.stringify(schema.imageObject)}</script>
        {schema.faqPage && (
          <script type="application/ld+json">{JSON.stringify(schema.faqPage)}</script>
        )}
      </Helmet>

      <article className="blog-post">
        {/* ---- Hero ---- */}
        <nav aria-label="Breadcrumb" className="breadcrumb">
          <a href={SITE_URL}>Home</a> ›{" "}
          <a href={`${SITE_URL}/blogs`}>Blog</a> ›{" "}
          <a href={`${SITE_URL}/blogs?category=${post.categorySlug}`}>{post.category}</a> ›{" "}
          <span aria-current="page">{post.title}</span>
        </nav>

        <h1>{post.title}</h1>

        <div className="meta-row">
          <a href={`${SITE_URL}/author/${post.author.slug}`}>By {post.author.name}</a>
          <span>· Published {formatDate(post.publishedDate)}</span>
          {post.updatedDate && post.updatedDate !== post.publishedDate && (
            <span>· Updated {formatDate(post.updatedDate)}</span>
          )}
          <span>· {rt} min read</span>
          <span>· {post.category}</span>
        </div>

        <ShareButtons url={url} title={post.title} />

        <img
          src={post.featuredImage.url}
          alt={post.featuredImage.alt}
          width={post.featuredImage.width}
          height={post.featuredImage.height}
          fetchpriority="high"
        />

        {/* ---- Quick Facts ---- */}
        {post.quickFacts?.length > 0 && (
          <aside className="quick-facts" aria-label="Quick facts">
            <h2>Quick Facts</h2>
            <ul>
              {post.quickFacts.map((f) => (
                <li key={f.label}>
                  <strong>{f.label}:</strong> {f.value}
                </li>
              ))}
            </ul>
          </aside>
        )}

        {/* ---- Table of Contents ---- */}
        <nav className="toc" aria-label="Table of contents">
          <button onClick={() => setTocOpen((o) => !o)} className="toc-toggle">
            Table of Contents {tocOpen ? "▲" : "▼"}
          </button>
          <ul hidden={!tocOpen} className="toc-list-mobile">
            {post.sections
              .filter((s) => s.level === "h2")
              .map((s) => (
                <li key={s.id}>
                  <a href={`#${s.id}`}>{s.heading}</a>
                </li>
              ))}
          </ul>
          {/* Desktop: always visible, sticky via CSS, not JS-gated */}
          <ul className="toc-list-desktop">
            {post.sections
              .filter((s) => s.level === "h2")
              .map((s) => (
                <li key={s.id}>
                  <a href={`#${s.id}`}>{s.heading}</a>
                </li>
              ))}
          </ul>
        </nav>

        {/* ---- Body ---- */}
        <div className="content">
          {post.sections.map((s) => {
            const Heading = s.level === "h2" ? "h2" : "h3";
            return (
              <section key={s.id} id={s.id}>
                <Heading>{s.heading}</Heading>
                <div dangerouslySetInnerHTML={{ __html: s.html }} />
              </section>
            );
          })}
        </div>

        {/* ---- FAQ ---- */}
        {post.faqs?.length > 0 && (
          <section aria-label="Frequently asked questions">
            <h2>Frequently Asked Questions</h2>
            {post.faqs.map((f) => (
              <details key={f.question}>
                <summary>{f.question}</summary>
                <p>{f.answer}</p>
              </details>
            ))}
          </section>
        )}

        {/* ---- Tags ---- */}
        {post.tags?.length > 0 && (
          <div className="tags">
            {post.tags.map((t) => (
              <a href={`${SITE_URL}/blogs?tag=${t.slug}`} key={t.slug} className="tag-chip">
                #{t.label}
              </a>
            ))}
          </div>
        )}

        {/* ---- Author box ---- */}
        <section className="author-box" aria-label="About the author">
          <h2>About the Author</h2>
          <p>
            <strong>{post.author.name}</strong>
          </p>
          <p>{post.author.bio}</p>
          {post.author.expertise?.length > 0 && (
            <p>Expertise: {post.author.expertise.join(", ")}</p>
          )}
          {post.author.reviewedSources?.length > 0 && (
            <p>Reviewed sources: {post.author.reviewedSources.join(", ")}</p>
          )}
        </section>

        {/* ---- Related Articles ---- */}
        {post.relatedPosts?.length > 0 && (
          <section aria-label="Related articles">
            <h2>Related Articles</h2>
            <div className="related-grid">
              {post.relatedPosts.map((r) => (
                <a href={`${SITE_URL}/blogs/${r.slug}`} key={r.slug} className="related-card">
                  <img src={r.image.url} alt={r.image.alt} loading="lazy" />
                  <span>{r.title}</span>
                </a>
              ))}
            </div>
          </section>
        )}

        {/* ---- Latest Posts widget ---- */}
        {post.latestPosts?.length > 0 && (
          <aside aria-label="Latest posts">
            <h2>Latest Posts</h2>
            <ul>
              {post.latestPosts.map((l) => (
                <li key={l.slug}>
                  <a href={`${SITE_URL}/blogs/${l.slug}`}>{l.title}</a>
                  <span> — {formatDate(l.publishedDate)}</span>
                </li>
              ))}
            </ul>
          </aside>
        )}

        {/* ---- Category strip ---- */}
        <div className="category-strip">
          <a href={`${SITE_URL}/blogs?category=${post.categorySlug}`}>
            More in {post.category} →
          </a>
        </div>

        {/* ---- Comments (shell — wire to your moderation API) ---- */}
        <section aria-label="Comments" className="comments">
          <h2>Discussion</h2>
          <CommentSection postSlug={post.slug} />
        </section>

        {/* ---- Bottom CTA ---- */}
        <section className="cta-block">
          <h2>Get Daily Government Job Alerts</h2>
          <a href="https://wa.me/..." rel="nofollow">
            Join WhatsApp
          </a>
          <a href="https://t.me/..." rel="nofollow">
            Join Telegram
          </a>
        </section>
      </article>
    </>
  );
}

function ShareButtons({ url, title }) {
  const encoded = encodeURIComponent(url);
  const text = encodeURIComponent(title);
  return (
    <div className="share-buttons" aria-label="Share this article">
      <a href={`https://wa.me/?text=${text}%20${encoded}`} rel="nofollow noopener">
        WhatsApp
      </a>
      <a href={`https://t.me/share/url?url=${encoded}&text=${text}`} rel="nofollow noopener">
        Telegram
      </a>
      <a href={`https://twitter.com/intent/tweet?text=${text}&url=${encoded}`} rel="nofollow noopener">
        X
      </a>
      <button onClick={() => navigator.clipboard.writeText(url)}>Copy Link</button>
    </div>
  );
}

// Minimal comment shell — replace with real fetch to your moderation API.
// IMPORTANT: fetch and render approved comments server-side / in the
// prerendered HTML if you want them to count toward crawlable content depth.
function CommentSection({ postSlug }) {
  return (
    <div className="comment-form-shell" data-post={postSlug}>
      <p>Comments are reviewed before publishing.</p>
      {/* form + list wired to backend */}
    </div>
  );
}

function formatDate(iso) {
  return new Date(iso).toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
}
