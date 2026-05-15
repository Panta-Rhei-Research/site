---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_1_eq",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/eta-1-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.IteratedPrime`.",
  "declaration_id": "TauLib.BookI.Coordinates.IteratedPrime::eta_1_eq",
  "declaration_slug": "eta-1-eq",
  "kind": "theorem",
  "name": "eta_1_eq",
  "module_name": "TauLib.BookI.Coordinates.IteratedPrime",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/",
  "source_line_start": 184,
  "source_line_end": 184,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L184-L184",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.IteratedPrime",
        "url": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L184-L184",
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

- Module: [TauLib.BookI.Coordinates.IteratedPrime](/corpus/taulib/docs/book-i-coordinates-iterated-prime/)
- Source path: [`TauLib/BookI/Coordinates/IteratedPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L184-L184)
- Source range: L184-L184
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- η₁ = 5 (first value of η-orbit). -/
```

## Source Excerpt

```lean
theorem eta_1_eq : towerVal 3 1 = 5 := by native_decide
```
