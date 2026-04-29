---
{
  "projection_kind": "taulib_declaration",
  "title": "BaseTau1",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/base-tau1/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::BaseTau1",
  "declaration_slug": "base-tau1",
  "kind": "structure",
  "name": "BaseTau1",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 44,
  "source_line_end": 47,
  "registry_ids": [
    "II.D05"
  ],
  "related_registry_items": [
    {
      "id": "II.D05",
      "title": "Base tau^1",
      "url": "/registry/object/II.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L44-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L44-L47",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/verify/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L44-L47)
- Source range: L44-L47
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D05` — Base tau^1

## Immediate Comment / Docstring

```lean
/-- [II.D05] Base τ¹: the (D, A) coordinate space.
    D = radial depth (α-channel), A = prime direction (π-channel).
    Constraint: A ∈ ℙ_τ ∪ {1}, all prime factors of D < A. -/
```

## Source Excerpt

```lean
structure BaseTau1 where
  d : TauIdx  -- radial depth
  a : TauIdx  -- prime direction
  deriving Repr, DecidableEq
```
