---
{
  "projection_kind": "taulib_declaration",
  "title": "ScopeGradient",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/scope-gradient/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ScopeGradient",
  "declaration_slug": "scope-gradient",
  "kind": "structure",
  "name": "ScopeGradient",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 413,
  "source_line_end": 418,
  "registry_ids": [
    "IV.R119"
  ],
  "related_registry_items": [
    {
      "id": "IV.R119",
      "title": "Scope gradient across mass table",
      "url": "/registry/object/IV.R119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L413-L418",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L413-L418",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L413-L418)
- Source range: L413-L418
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R119` — Scope gradient across mass table

## Immediate Comment / Docstring

```lean
/-- [IV.R119] The mass table exhibits a clear scope gradient from
    tau-effective established (m_e, massless photon/gluon) through
    tau-effective structural (Koide, three generations) to
    conjectural (quark masses, W/Z/H masses). -/
```

## Source Excerpt

```lean
structure ScopeGradient where
  /-- Number of scope levels. -/
  levels : Nat := 4
  /-- Highest precision (ppm). -/
  best_ppm : Nat := 25
  deriving Repr
```
