---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberDominance",
  "permalink": "/verify/taulib/docs/book-ii-interior-omega-readout/fiber-dominance/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::FiberDominance",
  "declaration_slug": "fiber-dominance",
  "kind": "inductive",
  "name": "FiberDominance",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/verify/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 40,
  "source_line_end": 44,
  "registry_ids": [
    "II.D04"
  ],
  "related_registry_items": [
    {
      "id": "II.D04",
      "title": "Omega Readout",
      "url": "/registry/object/II.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L40-L44",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/verify/taulib/docs/book-ii-interior-omega-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L40-L44",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/verify/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L40-L44)
- Source range: L40-L44
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D04` — Omega Readout

## Immediate Comment / Docstring

```lean
/-- [II.D04] Classification of fiber (B,C) behavior at ω-limit.
    Determines which lobe of the lemniscate ℒ a path approaches. -/
```

## Source Excerpt

```lean
inductive FiberDominance where
  | b_dominant : FiberDominance   -- B ≫ C → e₊-lobe
  | c_dominant : FiberDominance   -- C ≫ B → e₋-lobe
  | balanced   : FiberDominance   -- B ≈ C → crossing point ω_ℒ
  deriving Repr, DecidableEq
```
