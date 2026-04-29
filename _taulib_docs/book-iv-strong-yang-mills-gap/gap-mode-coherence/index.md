---
{
  "projection_kind": "taulib_declaration",
  "title": "GapModeCoherence",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/gap-mode-coherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::GapModeCoherence",
  "declaration_slug": "gap-mode-coherence",
  "kind": "structure",
  "name": "GapModeCoherence",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 217,
  "source_line_end": 224,
  "registry_ids": [
    "IV.P106"
  ],
  "related_registry_items": [
    {
      "id": "IV.P106",
      "title": "Gap mode coherence",
      "url": "/registry/object/IV.P106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L217-L224",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L217-L224",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L217-L224)
- Source range: L217-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P106` — Gap mode coherence

## Immediate Comment / Docstring

```lean
/-- [IV.P106] Gap mode coherence: rho(g_{n+1}) = g_n for n >= 3.
    The lightest excitation at successive stages is consistent. -/
```

## Source Excerpt

```lean
structure GapModeCoherence where
  /-- Restriction preserves gap mode. -/
  restriction_preserves : Bool := true
  /-- Active from depth 3. -/
  activation_depth : Nat := 3
  /-- Projective limit is well-defined. -/
  limit_defined : Bool := true
  deriving Repr
```
