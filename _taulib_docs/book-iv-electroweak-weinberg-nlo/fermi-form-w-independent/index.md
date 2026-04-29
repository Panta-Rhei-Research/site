---
{
  "projection_kind": "taulib_declaration",
  "title": "fermi_form_w_independent",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-w-independent/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::fermi_form_w_independent",
  "declaration_slug": "fermi-form-w-independent",
  "kind": "theorem",
  "name": "fermi_form_w_independent",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 152,
  "source_line_end": 159,
  "registry_ids": [
    "IV.T135"
  ],
  "related_registry_items": [
    {
      "id": "IV.T135",
      "title": "Fermi Form w-Independence",
      "url": "/registry/object/IV.T135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L152-L159",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L152-L159",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L152-L159)
- Source range: L152-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T135` — Fermi Form w-Independence

## Immediate Comment / Docstring

```lean
/-- [IV.T135] The Fermi form ingredient list has exactly 6 entries,
    none of which is w = M_W/m_n. The w-independence is structural:
    G_F is measured directly from muon decay. -/
```

## Source Excerpt

```lean
theorem fermi_form_w_independent :
    fermiForm.g_fermi ≠ "w" ∧
    fermiForm.m_neutron ≠ "w" ∧
    fermiForm.v_ud ≠ "w" ∧
    fermiForm.g_axial ≠ "w" ∧
    fermiForm.phase_space ≠ "w" ∧
    fermiForm.delta_r ≠ "w" := by
  exact ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩
```
