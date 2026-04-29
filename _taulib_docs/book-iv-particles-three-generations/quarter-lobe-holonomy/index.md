---
{
  "projection_kind": "taulib_declaration",
  "title": "quarter_lobe_holonomy",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/quarter-lobe-holonomy/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::quarter_lobe_holonomy",
  "declaration_slug": "quarter-lobe-holonomy",
  "kind": "def",
  "name": "quarter_lobe_holonomy",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1964,
  "source_line_end": 1966,
  "registry_ids": [
    "IV.D363"
  ],
  "related_registry_items": [
    {
      "id": "IV.D363",
      "title": "Quarter-Lobe Holonomy: ι_τ Exponent -1/4 = -1/(2·|lobes|)",
      "url": "/registry/object/IV.D363/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1964-L1966",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1964-L1966",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1964-L1966)
- Source range: L1964-L1966
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D363` — Quarter-Lobe Holonomy: ι_τ Exponent -1/4 = -1/(2·|lobes|)

## Immediate Comment / Docstring

```lean
/-- [IV.D363] Quarter-Lobe Holonomy.
    Exponent −1/4 = −1/(2·|lobes|). Quarter-revolution of lobe holonomy for CP. -/
```

## Source Excerpt

```lean
def quarter_lobe_holonomy : String :=
  "−1/4 = −1/(2·|lobes|) = −1/(2·2). " ++
  "CP violation requires partial traversal: (ι_τ⁻¹)^{1/4}."
```
