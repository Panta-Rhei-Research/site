---
{
  "projection_kind": "taulib_declaration",
  "title": "LemniscateModeClass",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/lemniscate-mode-class/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::LemniscateModeClass",
  "declaration_slug": "lemniscate-mode-class",
  "kind": "inductive",
  "name": "LemniscateModeClass",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 59,
  "source_line_end": 66,
  "registry_ids": [
    "IV.D196"
  ],
  "related_registry_items": [
    {
      "id": "IV.D196",
      "title": "Three mode classes on lemniscate",
      "url": "/registry/object/IV.D196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L59-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L59-L66",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L59-L66)
- Source range: L59-L66
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D196` — Three mode classes on lemniscate

## Immediate Comment / Docstring

```lean
/-- [IV.D196] The three topological mode classes on L = S¹ ∨ S¹.
    Each class corresponds to a fermion generation. -/
```

## Source Excerpt

```lean
inductive LemniscateModeClass where
  /-- Generation 1: crossing-point modes (localized near p_ω). -/
  | crossingPoint
  /-- Generation 2: single-lobe modes (winding around one lobe). -/
  | singleLobe
  /-- Generation 3: full-lemniscate modes (winding around both lobes). -/
  | fullLemniscate
  deriving Repr, DecidableEq, BEq
```
