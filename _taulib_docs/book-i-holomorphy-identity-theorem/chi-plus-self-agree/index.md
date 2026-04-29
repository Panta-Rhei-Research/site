---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_self_agree",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/chi-plus-self-agree/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::chi_plus_self_agree",
  "declaration_slug": "chi-plus-self-agree",
  "kind": "theorem",
  "name": "chi_plus_self_agree",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 217,
  "source_line_end": 219,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L217-L219",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L217-L219",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L217-L219)
- Source range: L217-L219
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verification: χ₊ agrees with itself at all stages. -/
```

## Source Excerpt

```lean
theorem chi_plus_self_agree (n k : TauIdx) :
    agree_at chi_plus_stage chi_plus_stage n k :=
  ⟨rfl, rfl⟩
```
