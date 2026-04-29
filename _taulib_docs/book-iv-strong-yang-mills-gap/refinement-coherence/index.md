---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementCoherence",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/refinement-coherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::RefinementCoherence",
  "declaration_slug": "refinement-coherence",
  "kind": "structure",
  "name": "RefinementCoherence",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 148,
  "source_line_end": 153,
  "registry_ids": [
    "IV.P104"
  ],
  "related_registry_items": [
    {
      "id": "IV.P104",
      "title": "Refinement coherence",
      "url": "/registry/object/IV.P104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L148-L153",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L148-L153",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L148-L153)
- Source range: L148-L153
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P104` — Refinement coherence

## Immediate Comment / Docstring

```lean
/-- [IV.P104] Refinement coherence:
    rho(Gamma_s^*[n+1]) = Gamma_s^*[n] for all n >= 3. -/
```

## Source Excerpt

```lean
structure RefinementCoherence where
  /-- Restriction preserves vacuum. -/
  restriction_preserves : Bool := true
  /-- Active from depth 3. -/
  activation_depth : Nat := 3
  deriving Repr
```
