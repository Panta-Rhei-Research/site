---
{
  "projection_kind": "taulib_declaration",
  "title": "hubble_self_consistency",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-self-consistency/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::hubble_self_consistency",
  "declaration_slug": "hubble-self-consistency",
  "kind": "theorem",
  "name": "hubble_self_consistency",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 566,
  "source_line_end": 569,
  "registry_ids": [
    "V.P178"
  ],
  "related_registry_items": [
    {
      "id": "V.P178",
      "title": "Hubble Self-Consistency Check",
      "url": "/registry/object/V.P178/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L566-L569",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L566-L569",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L566-L569)
- Source range: L566-L569
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.P178` — Hubble Self-Consistency Check

## Immediate Comment / Docstring

```lean
/-- [V.P178] Self-consistency: h²·Ω_m = ω_m.
    h² × 100000 = 45363, Ω_m × 10000 = 3299, product / 10 = 14964.
    This should match ω_m(NLO) × 10000 = 14964. -/
```

## Source Excerpt

```lean
theorem hubble_self_consistency :
    hubble_derivation_data.h_x100000 = 67352 ∧
    hubble_derivation_data.w3_3 = 17 := by
  native_decide
```
