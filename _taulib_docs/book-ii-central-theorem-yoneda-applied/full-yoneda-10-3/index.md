---
{
  "projection_kind": "taulib_declaration",
  "title": "full_yoneda_10_3",
  "permalink": "/corpus/taulib/docs/book-ii-central-theorem-yoneda-applied/full-yoneda-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::full_yoneda_10_3",
  "declaration_slug": "full-yoneda-10-3",
  "kind": "theorem",
  "name": "full_yoneda_10_3",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/corpus/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 298,
  "source_line_end": 299,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L298-L299",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/corpus/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L298-L299",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/corpus/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L298-L299)
- Source range: L298-L299
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Full Yoneda applied [II.L14 + II.T39]
```

## Source Excerpt

```lean
theorem full_yoneda_10_3 :
    full_yoneda_applied_check 10 3 = true := by native_decide
```
