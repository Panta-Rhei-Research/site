---
layout: program-doc
title: "Publication Notifications: Orientation"
title_plain: "Publication Notifications: Orientation"
lane: discover
v2_lane: discover
permalink: /discover/follow-the-research/
type: "Research Stream"
status: "Canonical"
summary_short: "An entry surface for Research Notes, publication notifications, and factual release records."
hero_ctas:
  - label: "Research Notes"
    url: /publications/research-notes/
    primary: true
  - label: "Subscribe"
    url: /engage/follow-the-research/
  - label: "Changelog"
    url: /changelog/
right_rail:
  related:
    - title: "Research Notes"
      url: /publications/research-notes/
    - title: "Engage: Publication Notifications"
      url: /engage/follow-the-research/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Research Stream"
    status: "Canonical"
    updated: "April 2026"
---

## Two Ongoing Streams

The site has two different public update streams.

### Research Notes

[Research Notes]({{ '/publications/research-notes/' | relative_url }}) are outward-facing, dated research artifacts. They are not blog posts and not changelog entries. They belong canonically to Publications, but Discover and Engage route readers toward them.

### Changelog

[Changelog]({{ '/changelog/' | relative_url }}) tracks changes to the site, corpus, release state, and infrastructure. It is supporting research infrastructure, not a publication stream.

## Publication Notifications

For email delivery of new Research Note release notices, use [Engage: Publication Notifications]({{ '/engage/follow-the-research/' | relative_url }}).

Research Notes may comment on new developments in Core Semantics, the Structural Challenge Ledger, Construction Spine, Results, or Verify. White papers and media briefs are released under Publications; Research Notes are the ongoing dated scholarly stream.

## Recent Research Notes

{% assign notes = site.research_notes | sort: 'date' | reverse %}
{% for note in notes limit: 4 %}
<div class="v2-tile">
  <h3><a href="{{ note.url | relative_url }}">{{ note.title }}</a></h3>
  <p>{{ note.summary_short | default: note.summary_medium }}</p>
  <div class="v2-badge-row">
    <span class="v2-badge">{{ note.date | date: "%B %-d, %Y" }}</span>
    {% if note.note_type %}<span class="v2-badge">{{ note.note_type }}</span>{% endif %}
  </div>
</div>
{% endfor %}

## Cross-links

- [Publications: Research Notes]({{ '/publications/research-notes/' | relative_url }})
- [Engage: Publication Notifications]({{ '/engage/follow-the-research/' | relative_url }})
- [Changelog]({{ '/changelog/' | relative_url }})
