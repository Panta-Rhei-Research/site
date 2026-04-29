---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_book_v_connection",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/remark-book-v-connection/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::remark_book_v_connection",
  "declaration_slug": "remark-book-v-connection",
  "kind": "def",
  "name": "remark_book_v_connection",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 338,
  "source_line_end": 339,
  "registry_ids": [
    "IV.R40"
  ],
  "related_registry_items": [
    {
      "id": "IV.R40",
      "title": "Honesty About Precision",
      "url": "/registry/object/IV.R40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L338-L339",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L338-L339",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L338-L339)
- Source range: L338-L339
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R40` — Honesty About Precision

## Immediate Comment / Docstring

```lean
/-- [IV.R40] Book V (Categorical Macrocosm) extends the EW synthesis
    to the gravitational sector. The closing identity
    α_G = α¹⁸ · √3 · (1 − (3/π)·α) connects the EW fine structure
    constant to Newton's gravitational constant G via 18 powers of α. -/
```

## Source Excerpt

```lean
def remark_book_v_connection : String :=
  "Book V extends to gravity: alpha_G = alpha^18 * sqrt(3) * (1 - (3/pi)*alpha)"
```
