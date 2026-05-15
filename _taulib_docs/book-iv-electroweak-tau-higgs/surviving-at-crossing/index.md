---
{
  "projection_kind": "taulib_declaration",
  "title": "surviving_at_crossing",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs/surviving-at-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::surviving_at_crossing",
  "declaration_slug": "surviving-at-crossing",
  "kind": "theorem",
  "name": "surviving_at_crossing",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 242,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L242-L245",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L242-L245",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/corpus/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L242-L245)
- Source range: L242-L245
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The surviving mode is at the crossing point with σ = +1. -/
```

## Source Excerpt

```lean
theorem surviving_at_crossing :
    sigma_polarity.at_crossing = true ∧
    sigma_polarity.sigma = 1 := by
  exact ⟨rfl, rfl⟩
```
