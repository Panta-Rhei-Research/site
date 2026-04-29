---
{
  "projection_kind": "taulib_declaration",
  "title": "unit_torus_vacuum",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/unit-torus-vacuum/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::unit_torus_vacuum",
  "declaration_slug": "unit-torus-vacuum",
  "kind": "def",
  "name": "unit_torus_vacuum",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 111,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L111-L119",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.GravitationalConstant",
        "url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L111-L119",
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

- Module: [TauLib.BookV.Gravity.GravitationalConstant](/verify/taulib/docs/book-v-gravity-gravitational-constant/)
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L111-L119)
- Source range: L111-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example torus vacuum with r = ι_τ, R = 1 (unit major radius).
    Shape ratio: ι_τ/1 = ι_τ. -/
```

## Source Excerpt

```lean
def unit_torus_vacuum : TorusVacuum where
  minor_numer := iota         -- r = ι_τ
  minor_denom := iotaD
  major_numer := iotaD        -- R = 1
  major_denom := iotaD
  minor_denom_pos := by simp [iotaD, iota_tau_denom]
  major_denom_pos := by simp [iotaD, iota_tau_denom]
  major_positive := by simp [iotaD, iota_tau_denom]
  shape_ratio := by simp [iota, iotaD, iota_tau_numer, iota_tau_denom]
```
