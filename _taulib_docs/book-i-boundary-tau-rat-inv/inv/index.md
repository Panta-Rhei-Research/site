---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/inv/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::TauRat.inv",
  "declaration_slug": "inv",
  "kind": "def",
  "name": "TauRat.inv",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 62,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L62-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L62-L65",
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/verify/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L62-L65)
- Source range: L62-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Multiplicative inverse on `TauRat`.  Requires a nonzero hypothesis
    (see `TauRat.is_nonzero`).

    Structure: the new numerator is either `⟨den, 0⟩` (when `q.num > 0`)
    or `⟨0, den⟩` (when `q.num < 0`), so the sign is carried in the
    TauInt representation.  The new denominator is `q.num.toInt.natAbs`,
    which is strictly positive by `Int.natAbs_pos.mpr h`. -/
```

## Source Excerpt

```lean
def TauRat.inv (q : TauRat) (h : q.is_nonzero) : TauRat :=
  { num := if 0 < q.num.toInt then ⟨q.den, 0⟩ else ⟨0, q.den⟩,
    den := q.num.toInt.natAbs,
    den_pos := Int.natAbs_pos.mpr h }
```
