---
{
  "projection_kind": "taulib_declaration",
  "title": "surviving_is_spin0",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/surviving-is-spin0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::surviving_is_spin0",
  "declaration_slug": "surviving-is-spin0",
  "kind": "theorem",
  "name": "surviving_is_spin0",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 235,
  "source_line_end": 239,
  "registry_ids": [
    "IV.T64"
  ],
  "related_registry_items": [
    {
      "id": "IV.T64",
      "title": "Higgs Scalarity Theorem",
      "url": "/registry/object/IV.T64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L235-L239",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L235-L239",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L235-L239)
- Source range: L235-L239
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T64` — Higgs Scalarity Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T64] After Goldstone bosons are eaten by W± and Z,
    the single surviving excitation is spin-0 (the Higgs boson).

    Counting: 4 real components − 3 Goldstones = 1 physical scalar. -/
```

## Source Excerpt

```lean
theorem surviving_is_spin0 :
    fiber_spin_decomposition.spin0_count = 1 ∧
    fiber_spin_decomposition.spin1_count = 3 ∧
    fiber_spin_decomposition.total = 4 := by
  exact ⟨rfl, rfl, rfl⟩
```
