const ROUTES = new Map([
  ["/", "https://panta-rhei.site/"],
  ["/wp000", "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"],
  ["/wp-glance", "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"],
  ["/c001", "https://panta-rhei.site/program/about/standing-in-the-inquiry-of-being/"],
  ["/wp001", "https://panta-rhei.site/publications/anchor-documents/wp001-panta-rhei-research-program-executive-overview/"],
  ["/wp002", "https://panta-rhei.site/publications/anchor-documents/wp002-t-theory-executive-synopsis/"],
  ["/wp-theory", "https://panta-rhei.site/publications/anchor-documents/wp002-t-theory-executive-synopsis/"],
  ["/wp003", "https://panta-rhei.site/publications/anchor-documents/wp003-taulib-technical-overview/"],
  ["/wp-taulib", "https://panta-rhei.site/publications/anchor-documents/wp003-taulib-technical-overview/"],
  ["/wp004", "https://panta-rhei.site/publications/anchor-documents/wp004-public-research-observatory-blueprint/"],
  ["/wp-observatory", "https://panta-rhei.site/publications/anchor-documents/wp004-public-research-observatory-blueprint/"],
  ["/wp005", "https://panta-rhei.site/publications/anchor-documents/wp005-global-public-good-impact-overview/"],
  ["/wp-impact", "https://panta-rhei.site/publications/anchor-documents/wp005-global-public-good-impact-overview/"],
  ["/anchor-documents", "https://panta-rhei.site/publications/anchor-documents/"]
]);

function normalizedPath(pathname) {
  if (pathname === "/") return "/";
  return pathname.endsWith("/") ? pathname.slice(0, -1) : pathname;
}

export function shortRouteTarget(requestUrl) {
  const url = new URL(requestUrl);
  const target = ROUTES.get(normalizedPath(url.pathname));
  if (!target) return null;

  const targetUrl = new URL(target);
  targetUrl.search = url.search;
  return targetUrl.toString();
}

export default {
  async fetch(request) {
    const target = shortRouteTarget(request.url);
    if (target) {
      return Response.redirect(target, 301);
    }

    return new Response("Unknown Panta Rhei short route.", {
      status: 404,
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "Cache-Control": "public, max-age=300"
      }
    });
  }
};
