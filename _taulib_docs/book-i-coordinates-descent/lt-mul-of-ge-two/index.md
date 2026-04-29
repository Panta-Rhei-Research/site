---
{
  "projection_kind": "taulib_declaration",
  "title": "lt_mul_of_ge_two",
  "permalink": "/verify/taulib/docs/book-i-coordinates-descent/lt-mul-of-ge-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Descent`.",
  "declaration_id": "TauLib.BookI.Coordinates.Descent::lt_mul_of_ge_two",
  "declaration_slug": "lt-mul-of-ge-two",
  "kind": "theorem",
  "name": "lt_mul_of_ge_two",
  "module_name": "TauLib.BookI.Coordinates.Descent",
  "module_url": "/verify/taulib/docs/book-i-coordinates-descent/",
  "source_line_start": 38,
  "source_line_end": 41,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L38-L41",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Descent",
        "url": "/verify/taulib/docs/book-i-coordinates-descent/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L38-L41",
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

- Module: [TauLib.BookI.Coordinates.Descent](/verify/taulib/docs/book-i-coordinates-descent/)
- Source path: [`TauLib/BookI/Coordinates/Descent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L38-L41)
- Source range: L38-L41
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A product a * b with a ≥ 2 is strictly larger than b (when b ≥ 1). -/
```

## Source Excerpt

```lean
theorem lt_mul_of_ge_two {a b : Nat} (ha : a ≥ 2) (hb : b ≥ 1) :
    b < a * b := by
  have : a * b ≥ 2 * b := Nat.mul_le_mul_right b ha
  omega
```
