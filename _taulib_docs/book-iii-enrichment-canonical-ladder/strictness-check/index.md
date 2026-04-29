---
{
  "projection_kind": "taulib_declaration",
  "title": "strictness_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/strictness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::strictness_check",
  "declaration_slug": "strictness-check",
  "kind": "def",
  "name": "strictness_check",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 98,
  "source_line_end": 103,
  "registry_ids": [
    "III.T02"
  ],
  "related_registry_items": [
    {
      "id": "III.T02",
      "title": "Strictness Theorem",
      "url": "/registry/object/III.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L98-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L98-L103",
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
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L98-L103)
- Source range: L98-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T02` — Strictness Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T02] Strictness check: E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃.
    Combines the strictness_checker witnesses with the E₁ strictness
    witness (bipolar Hom decomposition). -/
```

## Source Excerpt

```lean
def strictness_check (bound db : TauIdx) : Bool :=
  strictness_checker .E0 bound db &&
  strictness_checker .E1 bound db &&
  strictness_checker .E2 bound db &&
  strictness_checker .E3 bound db &&
  e1_strictness_witness bound db
```
