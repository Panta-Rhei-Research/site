---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaTail",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/omega-tail/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::OmegaTail",
  "declaration_slug": "omega-tail",
  "kind": "structure",
  "name": "OmegaTail",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 36,
  "source_line_end": 40,
  "registry_ids": [
    "I.D25"
  ],
  "related_registry_items": [
    {
      "id": "I.D25",
      "title": "Omega-Tail (Compatible Tower)",
      "url": "/registry/object/I.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L36-L40",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/verify/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L36-L40",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/verify/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L36-L40)
- Source range: L36-L40
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D25` — Omega-Tail (Compatible Tower)

## Immediate Comment / Docstring

```lean
/-- [I.D25] Truncated omega-tail up to depth d: components x_k for k = 1..d.
    Represented as a list of TauIdx values, where the k-th entry is x_k ∈ Z/M_kZ.
    Compatibility: x_k = x_ℓ mod M_k for k ≤ ℓ. -/
```

## Source Excerpt

```lean
structure OmegaTail where
  depth : TauIdx
  components : List TauIdx
  depth_eq : components.length = depth
  deriving Repr
```
