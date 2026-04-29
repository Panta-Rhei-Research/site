---
{
  "projection_kind": "taulib_declaration",
  "title": "AgencyExtension",
  "permalink": "/verify/taulib/docs/book-vi-agency-agency-sector/agency-extension/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.AgencySector`.",
  "declaration_id": "TauLib.BookVI.Agency.AgencySector::AgencyExtension",
  "declaration_slug": "agency-extension",
  "kind": "structure",
  "name": "AgencyExtension",
  "module_name": "TauLib.BookVI.Agency.AgencySector",
  "module_url": "/verify/taulib/docs/book-vi-agency-agency-sector/",
  "source_line_start": 101,
  "source_line_end": 110,
  "registry_ids": [
    "VI.T18"
  ],
  "related_registry_items": [
    {
      "id": "VI.T18",
      "title": "Agency as π-Base Extension",
      "url": "/registry/object/VI.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L101-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.AgencySector",
        "url": "/verify/taulib/docs/book-vi-agency-agency-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L101-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookVI.Agency.AgencySector](/verify/taulib/docs/book-vi-agency-agency-sector/)
- Source path: [`TauLib/BookVI/Agency/AgencySector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/AgencySector.lean#L101-L110)
- Source range: L101-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T18` — Agency as π-Base Extension

## Immediate Comment / Docstring

```lean
/-- [VI.T18] Agency = π-Base Extension Theorem.
    An agency Life loop is a persistence loop extended by
    nontrivial π-winding on the base. -/
```

## Source Excerpt

```lean
structure AgencyExtension where
  /-- Winding number on alpha (temporal). -/
  winding_alpha : Nat := 1
  /-- Winding number on pi (spatial). -/
  winding_pi : Nat
  /-- Pi-winding is nontrivial (≥ 1). -/
  pi_nontrivial : winding_pi ≥ 1
  /-- Extends persistence. -/
  extends_persistence : Bool := true
  deriving Repr
```
