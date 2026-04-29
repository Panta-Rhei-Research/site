---
{
  "projection_kind": "taulib_declaration",
  "title": "InternalRandomness",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/internal-randomness/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::InternalRandomness",
  "declaration_slug": "internal-randomness",
  "kind": "structure",
  "name": "InternalRandomness",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 654,
  "source_line_end": 661,
  "registry_ids": [
    "VII.D59"
  ],
  "related_registry_items": [
    {
      "id": "VII.D59",
      "title": "Internal Randomness",
      "url": "/registry/object/VII.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L654-L661",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L654-L661",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L654-L661)
- Source range: L654-L661
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D59` — Internal Randomness

## Immediate Comment / Docstring

```lean
/-- [VII.D59] Internal Randomness (ch40). No external source of
    randomness: all apparent randomness is internal complexity.
    A sequence is random iff its Kolmogorov complexity ≥ its length.
    Randomness is an emergent property of deterministic kernel structure. -/
```

## Source Excerpt

```lean
structure InternalRandomness where
  /-- No external source. -/
  no_external_source : Bool := true
  /-- Complexity-as-randomness. -/
  complexity_as_randomness : Bool := true
  /-- Deterministic kernel. -/
  deterministic_kernel : Bool := true
  deriving Repr
```
