---
{
  "projection_kind": "taulib_declaration",
  "title": "les_exactness_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/les-exactness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::les_exactness_check",
  "declaration_slug": "les-exactness-check",
  "kind": "def",
  "name": "les_exactness_check",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 159,
  "source_line_end": 160,
  "registry_ids": [
    "II.P19"
  ],
  "related_registry_items": [
    {
      "id": "II.P19",
      "title": "Long Exact Sequence",
      "url": "/registry/object/II.P19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L159-L160",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L159-L160",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L159-L160)
- Source range: L159-L160
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P19` — Long Exact Sequence

## Immediate Comment / Docstring

```lean
/-- [II.P19] Long exact sequence: connecting homomorphism exists.
    The snake lemma gives δ : H_n(C) → H_{n-1}(A). -/
```

## Source Excerpt

```lean
def les_exactness_check (k : Nat) : Bool :=
  ses_check k && boundary_coherence_check k
```
