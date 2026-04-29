---
{
  "projection_kind": "taulib_declaration",
  "title": "dvd_mul_right'",
  "permalink": "/verify/taulib/docs/book-i-coordinates-no-tie/dvd-mul-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::dvd_mul_right'",
  "declaration_slug": "dvd-mul-right",
  "kind": "theorem",
  "name": "dvd_mul_right'",
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/verify/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 73,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L73-L73",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NoTie",
        "url": "/verify/taulib/docs/book-i-coordinates-no-tie/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L73-L73",
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

- Module: [TauLib.BookI.Coordinates.NoTie](/verify/taulib/docs/book-i-coordinates-no-tie/)
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L73-L73)
- Source range: L73-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- a divides a * b. -/
```

## Source Excerpt

```lean
private theorem dvd_mul_right' (a b : Nat) : a ∣ a * b := ⟨b, rfl⟩
```
