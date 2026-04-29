---
{
  "projection_kind": "taulib_declaration",
  "title": "yukawa_ordering",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-ordering/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::yukawa_ordering",
  "declaration_slug": "yukawa-ordering",
  "kind": "theorem",
  "name": "yukawa_ordering",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 230,
  "source_line_end": 237,
  "registry_ids": [
    "IV.P78"
  ],
  "related_registry_items": [
    {
      "id": "IV.P78",
      "title": "τ-Yukawa Hierarchy",
      "url": "/registry/object/IV.P78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L230-L237",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L230-L237",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L230-L237)
- Source range: L230-L237
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P78` — τ-Yukawa Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.P78] Yukawa couplings are ordered by generation, and the
    ordering follows the sector coupling hierarchy:
    y_top > y_bottom > y_charm > y_electron.

    Each generation step down multiplies the coupling by approximately
    ι_τ², reflecting the spectral gap of the torus T². -/
```

## Source Excerpt

```lean
theorem yukawa_ordering :
    yukawa_full_top.coupling_numer * yukawa_full_bottom.coupling_denom >
    yukawa_full_bottom.coupling_numer * yukawa_full_top.coupling_denom ∧
    yukawa_full_bottom.coupling_numer * yukawa_full_charm.coupling_denom >
    yukawa_full_charm.coupling_numer * yukawa_full_bottom.coupling_denom ∧
    yukawa_full_charm.coupling_numer * yukawa_full_electron.coupling_denom >
    yukawa_full_electron.coupling_numer * yukawa_full_charm.coupling_denom := by
  simp [yukawa_full_top, yukawa_full_bottom, yukawa_full_charm, yukawa_full_electron]
```
