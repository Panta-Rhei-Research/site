---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_max_parity_violation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/weak-max-parity-violation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::weak_max_parity_violation",
  "declaration_slug": "weak-max-parity-violation",
  "kind": "theorem",
  "name": "weak_max_parity_violation",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 236,
  "source_line_end": 242,
  "registry_ids": [
    "IV.T51"
  ],
  "related_registry_items": [
    {
      "id": "IV.T51",
      "title": "Parity Violation in the A-Sector",
      "url": "/registry/object/IV.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L236-L242",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L236-L242",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L236-L242)
- Source range: L236-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T51` — Parity Violation in the A-Sector

## Immediate Comment / Docstring

```lean
/-- [IV.T51] The weak interaction maximally violates parity:
    V(A) = 100 (maximal) while V(D) = V(B) = V(C) = V(omega) = 0.
    This is structural: the A-sector balanced polarity (pol = 1)
    means sigma_A acts non-trivially, selecting one chirality. -/
```

## Source Excerpt

```lean
theorem weak_max_parity_violation :
    pv_weak.violation = 100 ∧
    pv_gravity.violation = 0 ∧
    pv_em.violation = 0 ∧
    pv_strong.violation = 0 ∧
    pv_higgs.violation = 0 := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩
```
