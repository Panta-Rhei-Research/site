---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_existence_uniqueness_stability",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/vacuum-existence-uniqueness-stability/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::vacuum_existence_uniqueness_stability",
  "declaration_slug": "vacuum-existence-uniqueness-stability",
  "kind": "theorem",
  "name": "vacuum_existence_uniqueness_stability",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 221,
  "source_line_end": 225,
  "registry_ids": [
    "IV.T63"
  ],
  "related_registry_items": [
    {
      "id": "IV.T63",
      "title": "Vacuum Construction",
      "url": "/registry/object/IV.T63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L221-L225",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L221-L225",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L221-L225)
- Source range: L221-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T63` — Vacuum Construction

## Immediate Comment / Docstring

```lean
/-- [IV.T63] The physical vacuum exists, is unique (mod S¹), and is stable.

    Existence: V_n is bounded below and continuous on a compact domain.
    Uniqueness: The Mexican hat potential has a unique radial minimum.
    Stability: The Hessian at the minimum has all positive eigenvalues
    in the radial direction (the angular direction is flat = Goldstone). -/
```

## Source Excerpt

```lean
theorem vacuum_existence_uniqueness_stability :
    physical_vacuum.unique = true ∧
    physical_vacuum.stable = true ∧
    physical_vacuum.vev_MeV > 0 := by
  exact ⟨rfl, rfl, by native_decide⟩
```
