---
{
  "projection_kind": "taulib_declaration",
  "title": "pentagon_dark_coupling",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pentagon-dark-coupling/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::pentagon_dark_coupling",
  "declaration_slug": "pentagon-dark-coupling",
  "kind": "def",
  "name": "pentagon_dark_coupling",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1993,
  "source_line_end": 1995,
  "registry_ids": [
    "IV.D364"
  ],
  "related_registry_items": [
    {
      "id": "IV.D364",
      "title": "Pentagon Dark Coupling: κ_D Exponent 5/4 = |gen|/(2·|lobes|)",
      "url": "/registry/object/IV.D364/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1993-L1995",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1993-L1995",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1993-L1995)
- Source range: L1993-L1995
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D364` — Pentagon Dark Coupling: κ_D Exponent 5/4 = |gen|/(2·|lobes|)

## Immediate Comment / Docstring

```lean
/-- [IV.D364] Pentagon Dark Coupling.
    Exponent 5/4 = |generators|/(2·|lobes|) = 5/4 on κ_D. -/
```

## Source Excerpt

```lean
def pentagon_dark_coupling : String :=
  "5/4 = |generators|/(2·|lobes|) = 5/(2·2). " ++
  "Each of 5 generators contributes κ_D^{1/4}."
```
