---
{
  "projection_kind": "taulib_declaration",
  "title": "fiber_base_homology_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/fiber-base-homology-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::fiber_base_homology_conj",
  "declaration_slug": "fiber-base-homology-conj",
  "kind": "theorem",
  "name": "fiber_base_homology_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1646,
  "source_line_end": 1649,
  "registry_ids": [
    "IV.D361"
  ],
  "related_registry_items": [
    {
      "id": "IV.D361",
      "title": "Fiber-Base Homology of τ³",
      "url": "/registry/object/IV.D361/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1646-L1649",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1646-L1649",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1646-L1649)
- Source range: L1646-L1649
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D361` — Fiber-Base Homology of τ³

## Immediate Comment / Docstring

```lean
/-- [IV.D361] Fiber-base homology conjunction (formalized). -/
```

## Source Excerpt

```lean
theorem fiber_base_homology_conj :
    (default : FiberBaseHomology).rank_fiber = 2 ∧
    (default : FiberBaseHomology).rank_base = 1 :=
  ⟨rfl, rfl⟩
```
