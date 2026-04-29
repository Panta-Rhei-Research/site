---
{
  "projection_kind": "taulib_declaration",
  "title": "three_gen_closure",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/three-gen-closure/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::three_gen_closure",
  "declaration_slug": "three-gen-closure",
  "kind": "def",
  "name": "three_gen_closure",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 593,
  "source_line_end": 596,
  "registry_ids": [
    "IV.P185"
  ],
  "related_registry_items": [
    {
      "id": "IV.P185",
      "title": "Three-Generation Winding Closure",
      "url": "/registry/object/IV.P185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L593-L596",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L593-L596",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L593-L596)
- Source range: L593-L596
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P185` — Three-Generation Winding Closure

## Immediate Comment / Docstring

```lean
/-- [IV.P185] Three primitive winding classes on T² host particle families.
    Classes: (1,0), (0,1), (1,1). Composite classes (2,0), (2,1) etc. are
    suppressed by additional ι_τ² spectral gap factor, producing masses
    ≥ ι_τ^{-2} × m_τ ≈ 29,850 m_e, exceeding the dark-matter mass tower cutoff. -/
```

## Source Excerpt

```lean
def three_gen_closure : String :=
  "Winding classes (1,0), (0,1), (1,1) are primitive on T^2. " ++
  "Composite (2,0) etc. produce masses ~ iota^{-2} * m_tau ~ 29850 m_e, " ++
  "exceeding dark matter mass tower cutoff."
```
