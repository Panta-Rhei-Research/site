---
{
  "projection_kind": "taulib_declaration",
  "title": "make_fluid_data",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/make-fluid-data/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::make_fluid_data",
  "declaration_slug": "make-fluid-data",
  "kind": "def",
  "name": "make_fluid_data",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 53,
  "source_line_end": 56,
  "registry_ids": [
    "III.D36"
  ],
  "related_registry_items": [
    {
      "id": "III.D36",
      "title": "τ-Admissible Fluid Data",
      "url": "/registry/object/III.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L53-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.FluidData",
        "url": "/verify/taulib/docs/book-iii-physics-fluid-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L53-L56",
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

- Module: [TauLib.BookIII.Physics.FluidData](/verify/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L53-L56)
- Source range: L53-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D36` — τ-Admissible Fluid Data

## Immediate Comment / Docstring

```lean
/-- [III.D36] Construct fluid data at depth k from bound: assigns each
    residue class its own value (the canonical assignment). -/
```

## Source Excerpt

```lean
def make_fluid_data (k : TauIdx) : FluidData :=
  let pk := primorial k
  if pk == 0 then ⟨k, []⟩
  else ⟨k, List.range pk⟩
```
