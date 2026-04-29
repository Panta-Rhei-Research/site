---
{
  "projection_kind": "taulib_declaration",
  "title": "all_links_have_level",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/all-links-have-level/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::all_links_have_level",
  "declaration_slug": "all-links-have-level",
  "kind": "theorem",
  "name": "all_links_have_level",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 345,
  "source_line_end": 350,
  "registry_ids": [
    "III.P30"
  ],
  "related_registry_items": [
    {
      "id": "III.P30",
      "title": "Sector Instantiation Lemma",
      "url": "/registry/object/III.P30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L345-L350",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.DependencyChain",
        "url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L345-L350",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Hinge.DependencyChain](/verify/taulib/docs/book-iii-hinge-dependency-chain/)
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L345-L350)
- Source range: L345-L350
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P30` — Sector Instantiation Lemma

## Immediate Comment / Docstring

```lean
/-- [III.P30] Structural: every link maps to a valid enrichment level. -/
```

## Source Excerpt

```lean
theorem all_links_have_level (link : ChainLink) :
    link.toEnrLevel = .E0 \/
    link.toEnrLevel = .E1 \/
    link.toEnrLevel = .E2 \/
    link.toEnrLevel = .E3 := by
  cases link <;> simp [ChainLink.toEnrLevel]
```
