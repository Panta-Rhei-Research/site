---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalRelaxation",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/topological-relaxation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::TopologicalRelaxation",
  "declaration_slug": "topological-relaxation",
  "kind": "structure",
  "name": "TopologicalRelaxation",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 133,
  "source_line_end": 144,
  "registry_ids": [
    "V.D64"
  ],
  "related_registry_items": [
    {
      "id": "V.D64",
      "title": "Topological relaxation",
      "url": "/registry/object/V.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L133-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L133-L144",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L133-L144)
- Source range: L133-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D64` — Topological relaxation

## Immediate Comment / Docstring

```lean
/-- [V.D64] Topological relaxation: the topology change from
    orthodox S^2 to tau-native T^2 above a critical mass threshold. -/
```

## Source Excerpt

```lean
structure TopologicalRelaxation where
  /-- The critical mass threshold numerator. -/
  threshold_numer : Nat
  /-- The critical mass threshold denominator. -/
  threshold_denom : Nat
  /-- Denominator positive. -/
  denom_pos : threshold_denom > 0
  /-- Below threshold: topology approx S^2 (orthodox). -/
  below_topology : String := "S2 (orthodox)"
  /-- Above threshold: topology = T^2 (tau-native). -/
  above_topology : String := "T2 (tau-native)"
  deriving Repr
```
