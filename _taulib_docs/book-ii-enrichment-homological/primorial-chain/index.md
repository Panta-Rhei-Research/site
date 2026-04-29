---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_chain",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/primorial-chain/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::primorial_chain",
  "declaration_slug": "primorial-chain",
  "kind": "def",
  "name": "primorial_chain",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 54,
  "source_line_end": 56,
  "registry_ids": [
    "II.D84"
  ],
  "related_registry_items": [
    {
      "id": "II.D84",
      "title": "Chain Complex",
      "url": "/registry/object/II.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L54-L56",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L54-L56",
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
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L54-L56)
- Source range: L54-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D84` — Chain Complex

## Immediate Comment / Docstring

```lean
/-- [II.D84] The primorial chain complex: d_n(x) = x mod M_{n-1}.
    This maps Z/M_n Z → Z/M_{n-1} Z via the canonical projection. -/
```

## Source Excerpt

```lean
def primorial_chain : ChainComplex :=
  { max_degree := 5
  , boundary := fun n x => if n == 0 then 0 else reduce x (n - 1) }
```
