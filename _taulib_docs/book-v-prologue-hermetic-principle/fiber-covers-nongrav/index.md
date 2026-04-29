---
{
  "projection_kind": "taulib_declaration",
  "title": "fiber_covers_nongrav",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/fiber-covers-nongrav/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::fiber_covers_nongrav",
  "declaration_slug": "fiber-covers-nongrav",
  "kind": "theorem",
  "name": "fiber_covers_nongrav",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 104,
  "source_line_end": 112,
  "registry_ids": [
    "V.T06"
  ],
  "related_registry_items": [
    {
      "id": "V.T06",
      "title": "Fiber Completeness --- IV.T32",
      "url": "/registry/object/V.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L104-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.HermeticPrinciple",
        "url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L104-L112",
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

- Module: [TauLib.BookV.Prologue.HermeticPrinciple](/verify/taulib/docs/book-v-prologue-hermetic-principle/)
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L104-L112)
- Source range: L104-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T06` — Fiber Completeness --- IV.T32

## Immediate Comment / Docstring

```lean
/-- [V.T06] The boundary holonomy algebra restricted to fiber sectors
    B, C, Omega covers all non-gravitational physics.

    Fiber sectors provide:
    - B (EM): photon transport, Maxwell equations, fine structure
    - C (Strong): color holonomy, confinement, mass gap
    - Omega (Higgs): mass generation, chirality crossing

    The fiber carrier type assignment agrees with sector physics. -/
```

## Source Excerpt

```lean
theorem fiber_covers_nongrav :
    em_sector.generator = .gamma ∧
    strong_sector.generator = .eta ∧
    higgs_sector.generator = .omega ∧
    -- All three are spatial (depth >= 2 or crossing)
    em_sector.depth >= 2 ∧
    strong_sector.depth >= 2 ∧
    higgs_sector.depth >= 2 := by
  exact ⟨rfl, rfl, rfl, by decide, by decide, by decide⟩
```
