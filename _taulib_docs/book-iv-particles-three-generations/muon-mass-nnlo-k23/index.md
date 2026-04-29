---
{
  "projection_kind": "taulib_declaration",
  "title": "muon_mass_nnlo_k23",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-mass-nnlo-k23/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::muon_mass_nnlo_k23",
  "declaration_slug": "muon-mass-nnlo-k23",
  "kind": "def",
  "name": "muon_mass_nnlo_k23",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1542,
  "source_line_end": 1544,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1542-L1544",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1542-L1544",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1542-L1544)
- Source range: L1542-L1544
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- m_μ/m_e = ι_τ^(-124/25)·(1-ι_τ^(23/3)) at +43 ppm. k=23/3.
    Structural: 23=W₃(4)+W₃(3)+1=5+17+1 (first Window-algebra NNLO exponent).
    Best rational: k=45/6=7.5=(3×W₃(4))/2 at -8.2 ppm. -/
```

## Source Excerpt

```lean
def muon_mass_nnlo_k23 : String :=
  "m_μ/m_e = ι_τ^(-124/25)·(1-ι_τ^(23/3)) at +43 ppm. " ++
  "23=W₃(4)+W₃(3)+1=5+17+1. Best: k=7.5=(3W₃(4))/2 at -8.2 ppm."
```
