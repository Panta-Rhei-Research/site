---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L112",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/example-l112/",
  "summary_short": "`example` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::#eval:112",
  "declaration_slug": "example-l112",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 112,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L112-L112",
  "formal_status": "example",
  "declaration_role": "example check",
  "formal_status_label": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L112-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "role": "example check",
      "status": "example"
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/corpus/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L112-L112)
- Source range: L112-L112
- Kind: `example`
- Public role: `example check`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- ROUND-TRIP VERIFICATION
-- ============================================================

-- prime_index ∘ nthPrime = id (verified for k = 0..5)
```

## Source Excerpt

```lean
example : prime_index (nthPrime 0) = 0 := by native_decide
```
