---
{
  "projection_kind": "taulib_declaration",
  "title": "closing_identity_canonical",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-canonical/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::closing_identity_canonical",
  "declaration_slug": "closing-identity-canonical",
  "kind": "def",
  "name": "closing_identity_canonical",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 118,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L118-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ClosingIdentity",
        "url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L118-L126",
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

- Module: [TauLib.BookV.GravityField.ClosingIdentity](/verify/taulib/docs/book-v-gravity-field-closing-identity/)
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L118-L126)
- Source range: L118-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical closing identity with tree-level chi = 1. -/
```

## Source Excerpt

```lean
def closing_identity_canonical : ClosingIdentityData where
  alpha_exponent := 18
  exp_is_18 := by rfl
  chi_numer := 1
  chi_denom := 1
  chi_denom_pos := by omega
  kn_numer := kn_required_numer   -- 34399723
  kn_denom := kn_required_denom   -- 10000000
  kn_denom_pos := by simp [kn_required_denom]
```
