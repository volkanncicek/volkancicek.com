// Open links that leave the site in a new tab. Scoped to article bodies, so nav and
// footer links keep the target attributes their templates set.
document.querySelectorAll('.article-content a[href^="http"]').forEach(function (link) {
  if (!link.href.includes(location.hostname)) {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
  }
});
