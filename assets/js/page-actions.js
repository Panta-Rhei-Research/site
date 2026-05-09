// =====================================================================
// page-actions.js — shared page-tools action handlers
// =====================================================================
// Used by all three "This Page" variants: rail (desktop right-rail card),
// bottom (above-footer inspection panel), and drawer (mobile this-page
// drawer in the header). Briefing reference:
//   atlas/website/briefings/v4/27_v4_share_component_desktop.md
//
// Conventions:
//   - Each action element carries `data-page-action="{name}"`.
//   - The wrapper element carries `data-page-tools` and the data payload
//     (data-title, data-url, data-status, data-review-angle, data-description).
//   - Inline confirmation toast lives in `.page-tools__status` inside the
//     same wrapper, with `aria-live="polite"`.
//   - Copy actions use `navigator.clipboard.writeText()` (HTTPS / secure
//     context required); fall back to `window.prompt()` if unavailable.
//   - Share uses `navigator.share()` only as progressive enhancement.
// =====================================================================

(function() {
  'use strict';

  var TOAST_DURATION_MS = 2200;

  function findStatus(scope) {
    if (!scope) return null;
    return scope.querySelector('.page-tools__status') || scope.querySelector('.page-tool-toast');
  }

  function showStatus(scope, message) {
    var status = findStatus(scope);
    if (!status) {
      // Legacy mobile-drawer fallback: drawer-internal toast lived under
      // .page-drawer-tools and was created on demand. The new page-tools
      // include always renders a `.page-tools__status` span, so this branch
      // is only hit by the legacy drawer path during the transition cycle.
      var drawerTools = scope && scope.querySelector ? scope.querySelector('.page-drawer-tools') : null;
      if (drawerTools) {
        status = drawerTools.querySelector('.page-tool-toast');
        if (!status) {
          status = document.createElement('p');
          status.className = 'page-tool-toast';
          status.setAttribute('role', 'status');
          status.setAttribute('aria-live', 'polite');
          drawerTools.appendChild(status);
        }
      }
    }
    if (!status) return;
    status.textContent = message;
    window.clearTimeout(status._timer);
    status._timer = window.setTimeout(function() { status.textContent = ''; }, TOAST_DURATION_MS);
  }

  function copyText(scope, value, successMessage) {
    if (!value) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(value).then(function() {
        showStatus(scope, successMessage);
      }).catch(function() {
        window.prompt('Copy this text', value);
      });
    } else {
      window.prompt('Copy this text', value);
    }
  }

  // ── Reviewer-note + citation templates (briefing §11) ─────────────

  function buildReviewerNote(payload) {
    // Briefing-canonical wording. Status + review-angle default to generic
    // public-research-page values when the page hasn't declared them.
    var title = payload.title || document.title;
    var description = payload.description || '';
    var status = payload.status || 'Public research page';
    var reviewAngle = payload.reviewAngle || 'General inspection';
    var url = payload.url || window.location.href;

    var lines = [];
    lines.push('Panta Rhei Research Program — ' + title);
    lines.push('');
    if (description) {
      lines.push(description);
      lines.push('');
    }
    lines.push('Status: ' + status);
    lines.push('Suggested review angle: ' + reviewAngle);
    lines.push('URL: ' + url);
    lines.push('');
    lines.push('Shared not as an endorsement, but as a page that may be worth expert inspection.');
    return lines.join('\n');
  }

  function buildCitation(payload) {
    var title = payload.title || document.title;
    var url = payload.url || window.location.href;
    var date = new Date();
    var iso = date.getFullYear() + '-' + String(date.getMonth() + 1).padStart(2, '0') + '-' + String(date.getDate()).padStart(2, '0');
    return 'Panta Rhei Research Program. "' + title + '." Public research observatory. Accessed ' + iso + '. ' + url;
  }

  function buildEmailDraft(payload) {
    var title = payload.title || document.title;
    var url = payload.url || window.location.href;
    var subject = 'Possibly worth inspection: ' + title;
    var bodyLines = [
      'Hi,',
      '',
      'I came across this page from the Panta Rhei Research Program and thought it might intersect with your work:',
      '',
      url,
      '',
      'The project presents itself as an independent open research program, with public corpus pages, registry objects, prior-art notes, and verification surfaces.',
      '',
      'I am not endorsing the claims, but this page looked potentially worth expert inspection.',
      '',
      'Best,'
    ];
    return 'mailto:?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(bodyLines.join('\n'));
  }

  // ── Action dispatcher ─────────────────────────────────────────────

  function getPayload(scope, action) {
    // Each wrapper carries the data; individual actions can override via
    // their own data attributes (legacy drawer pattern).
    return {
      title: action.getAttribute('data-share-title') || (scope && scope.getAttribute('data-title')) || document.title,
      description: (scope && scope.getAttribute('data-description')) || '',
      url: action.getAttribute('data-share-url')
        || action.getAttribute('data-copy-value')
        || (scope && scope.getAttribute('data-url'))
        || window.location.href,
      status: (scope && scope.getAttribute('data-status')) || 'Public research page',
      reviewAngle: (scope && scope.getAttribute('data-review-angle')) || 'General inspection'
    };
  }

  function handleAction(scope, action, event) {
    var name = action.getAttribute('data-page-action');
    if (!name) return;

    var payload = getPayload(scope, action);

    if (name === 'copy-link') {
      event.preventDefault();
      copyText(scope, payload.url, 'Link copied.');
      return;
    }
    if (name === 'copy-citation') {
      event.preventDefault();
      var citation = action.getAttribute('data-copy-value') || buildCitation(payload);
      copyText(scope, citation, 'Citation copied.');
      return;
    }
    if (name === 'copy-reviewer-note') {
      event.preventDefault();
      copyText(scope, buildReviewerNote(payload), 'Reviewer note copied.');
      return;
    }
    if (name === 'email-expert') {
      // Anchor with mailto href was rendered server-side too as fallback;
      // when JS is available we still let the browser handle the click.
      // Compute href dynamically so the date-of-access is current.
      action.setAttribute('href', buildEmailDraft(payload));
      return;
    }
    if (name === 'share') {
      event.preventDefault();
      if (navigator.share) {
        navigator.share({ title: payload.title, url: payload.url }).catch(function() {});
      } else {
        copyText(scope, payload.url, 'Share link copied.');
      }
      return;
    }
    // 'reviewer-note' (legacy: opens GitHub Issues prefilled — handled by
    // the anchor's href; no preventDefault needed) and dossier-pdf /
    // markdown / dossier (legacy aliases) fall through with default
    // browser behavior (anchor download).
  }

  // Single delegated listener at document level catches all three variants.
  document.addEventListener('click', function(event) {
    var action = event.target.closest('[data-page-action]');
    if (!action || action.disabled) return;
    var scope = action.closest('[data-page-tools]') || action.closest('.header-page-drawer') || action.closest('.header-toc-dropdown');
    handleAction(scope, action, event);
  });

  // Pre-compute mailto hrefs on page load so right-click/middle-click
  // works without JS-runtime dispatch.
  document.addEventListener('DOMContentLoaded', function() {
    var emailLinks = document.querySelectorAll('a[data-page-action="email-expert"]');
    Array.prototype.forEach.call(emailLinks, function(link) {
      var scope = link.closest('[data-page-tools]') || link.closest('.header-page-drawer');
      var payload = getPayload(scope, link);
      link.setAttribute('href', buildEmailDraft(payload));
    });
  });

})();
