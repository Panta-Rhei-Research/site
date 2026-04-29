---
{
  "projection_kind": "taulib_declaration",
  "title": "non_emptiness_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/non-emptiness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::non_emptiness_check",
  "declaration_slug": "non-emptiness-check",
  "kind": "def",
  "name": "non_emptiness_check",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 43,
  "source_line_end": 47,
  "registry_ids": [
    "III.T01"
  ],
  "related_registry_items": [
    {
      "id": "III.T01",
      "title": "Non-Emptiness Theorem",
      "url": "/registry/object/III.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L43-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L43-L47",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L43-L47)
- Source range: L43-L47
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T01` — Non-Emptiness Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T01] Non-emptiness check: every enrichment layer is inhabited.
    Uses existence_checker from Functor.lean for each level. -/
```

## Source Excerpt

```lean
def non_emptiness_check (bound db : TauIdx) : Bool :=
  existence_checker .E0 bound db &&
  existence_checker .E1 bound db &&
  existence_checker .E2 bound db &&
  existence_checker .E3 bound db
```
