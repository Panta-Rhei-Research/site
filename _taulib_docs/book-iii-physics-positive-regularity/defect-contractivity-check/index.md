---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_contractivity_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/defect-contractivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::defect_contractivity_check",
  "declaration_slug": "defect-contractivity-check",
  "kind": "def",
  "name": "defect_contractivity_check",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 145,
  "source_line_end": 159,
  "registry_ids": [
    "III.P14"
  ],
  "related_registry_items": [
    {
      "id": "III.P14",
      "title": "Defect Contractivity",
      "url": "/registry/object/III.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L145-L159",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L145-L159",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L145-L159)
- Source range: L145-L159
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P14` — Defect Contractivity

## Immediate Comment / Docstring

```lean
/-- [III.P14] Defect contractivity: defect at level k+1 ≤ defect at
    level k. Combined with defect ≥ 0, forces eventual stabilization.
    For canonical BNF, defect is 0 everywhere. -/
```

## Source Excerpt

```lean
def defect_contractivity_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let d_k := defect_functional k
      let d_k1 := defect_functional (k + 1)
      -- Contractivity: d_{k+1} ≤ d_k
      let contract := d_k1 <= d_k
      -- Non-trivial: defect is genuinely zero (exercises defect_functional)
      let genuinely_zero := d_k == 0 && d_k1 == 0
      contract && genuinely_zero && go (k + 1) (fuel - 1)
  termination_by fuel
```
