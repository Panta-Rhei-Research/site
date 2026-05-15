---
{
  "projection_kind": "taulib_declaration",
  "title": "no_shrink_requires_maturity",
  "permalink": "/corpus/taulib/docs/book-v-gravity-schwarzschild/no-shrink-requires-maturity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::no_shrink_requires_maturity",
  "declaration_slug": "no-shrink-requires-maturity",
  "kind": "theorem",
  "name": "no_shrink_requires_maturity",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 245,
  "source_line_end": 246,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L245-L246",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L245-L246",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/corpus/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L245-L246)
- Source range: L245-L246
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No-Shrink requires maturity. -/
```

## Source Excerpt

```lean
theorem no_shrink_requires_maturity (p : NoShrinkProperty) :
    p.mass.is_mature = true := p.mature_proof
```
