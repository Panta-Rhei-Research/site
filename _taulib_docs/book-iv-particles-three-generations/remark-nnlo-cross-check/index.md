---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_nnlo_cross_check",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/remark-nnlo-cross-check/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::remark_nnlo_cross_check",
  "declaration_slug": "remark-nnlo-cross-check",
  "kind": "def",
  "name": "remark_nnlo_cross_check",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1052,
  "source_line_end": 1053,
  "registry_ids": [
    "IV.R401"
  ],
  "related_registry_items": [
    {
      "id": "IV.R401",
      "title": "Cross-Check: 1/21 in p-n Mass Difference = 1/(4·W₃(4)+1); n=7 Higgs at +8 ppm",
      "url": "/registry/object/IV.R401/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1052-L1053",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1052-L1053",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1052-L1053)
- Source range: L1052-L1053
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R401` — Cross-Check: 1/21 in p-n Mass Difference = 1/(4·W₃(4)+1); n=7 Higgs at +8 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.R401] NNLO cross-check remark: p-n uses 4W+1=21, Higgs uses n=7, Window universal. -/
```

## Source Excerpt

```lean
def remark_nnlo_cross_check : String :=
  "NNLO cross-checks: p-n 4W₃(4)+1=21, Higgs n=7=2·lobes+sectors, Window universal in all."
```
